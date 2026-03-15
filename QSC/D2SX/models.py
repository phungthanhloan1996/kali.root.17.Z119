from django.db import models



class ProductGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductItem(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=10000)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='steps')
    estimated_hours = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.PositiveIntegerField()
    department_in_charge = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.item.name})"


class Product(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='products')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def total_progress(self):
        steps = self.item.steps.all()
        progresses = self.progresses.all()

        total_estimated = sum(step.estimated_hours for step in steps)
        if total_estimated == 0:
            return 0

        weighted_sum = 0
        for step in steps:
            step_progress = progresses.filter(step=step).first()
            progress_percent = step_progress.progress_percent if step_progress else 0
            weighted_sum += progress_percent * step.estimated_hours

        return round(weighted_sum / total_estimated, 2)
from django.utils import timezone
class ProductStepProgress(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='progresses')
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    progress_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)
    planned_progress_percent = models.FloatField(default=0)
    department_in_charge = models.CharField(max_length=100, blank=True, null=True)
    completed_date = models.DateTimeField(default=timezone.now)
    note_actual = models.TextField(blank=True, null = True)
    note_planned = models.TextField(blank=True, null = True)
    class Meta:
        unique_together = ('product', 'step')

    def save(self, *args, **kwargs):
        if self.progress_percent:
            self.completed_date = timezone.now()
        super().save(*args, **kwargs)



#thay doi models cua Note de hien thi len sum
from DKQSZ119.models import CustomUser
class ProductNote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_notes')

    def __str__(self):
        return f"Note: {self.product.name} - {self.created_by.username if self.created_by else 'Ẩn danh'}"


from django.db import models
from django.conf import settings
from DKQSZ119.models import Z119group

class OrderForm(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Đã gửi'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối'),
        ('forwarded', 'Phòng Kế hoạch đã chuyển'),
    ]

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order_forms'
    )
    ordering_unit = models.ForeignKey(
        Z119group,
        related_name='order_forms_created',
        on_delete=models.CASCADE
    )
    norm_unit = models.ForeignKey(
        Z119group,
        related_name='order_forms_normed',
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    executing_unit = models.ForeignKey(
        Z119group,
        related_name='order_forms_received',
        on_delete=models.CASCADE
    )
    order_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='submitted'
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='reviewed_orders'
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        norm_unit_name = self.norm_unit.name if self.norm_unit else "Chưa xác định"
        return f"Phiếu #{self.id} - {self.ordering_unit.name} → {norm_unit_name} → {self.executing_unit.name}"


from django.utils import timezone

class OrderItem(models.Model):
    order_form = models.ForeignKey(OrderForm, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)  # số việc
    due_date = models.DateField()  # ngày phải xong (theo yêu cầu đơn vị đặt)
    completed_date = models.DateField(null=True, blank=True)  # ngày hoàn thành thực tế
    note = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} - SL: {self.quantity}"

from django.db import models
from django.utils import timezone

class ProductDailyProgress(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='daily_progress')
    progress_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    planned_progress_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    date = models.DateField(default=timezone.now)

    # === Các trạng thái nghiệm thu ===
    approved_factory = models.BooleanField(default=False, verbose_name="Nghiệm thu Nhà máy")
    approved_department = models.BooleanField(default=False, verbose_name="Nghiệm thu Cục")
    approved_qc = models.BooleanField(default=False, verbose_name="Nghiệm thu QC")
    handed_over = models.BooleanField(default=False, verbose_name="Bàn giao đơn vị")
    

    #created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        unique_together = ('product', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.product.name} - {self.date} - {self.progress_percent}%"
