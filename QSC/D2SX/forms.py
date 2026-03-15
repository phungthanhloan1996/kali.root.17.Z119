from django import forms
from .models import ProductGroup, ProductItem, Product, Step, ProductStepProgress
# Form tạo nhóm sản phẩm
class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['name']
# Form tạo mặt hàng sản phẩm
class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ['name', 'group']
# Form tạo sản phẩm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'item', 'start_date','end_date']
# Form tạo bước sản phẩm
class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['name', 'item', 'estimated_hours', 'order']
# Form để cập nhật tiến độ sản phẩm
class ProgressForm(forms.ModelForm):
    class Meta:
        model = ProductStepProgress
        fields = ['product', 'step', 'progress_percent']
    def __init__(self, *args, **kwargs):
        # Nhận product và step từ kwargs để có thể hiển thị chính xác
        product = kwargs.get('initial', {}).get('product')
        steps = Step.objects.filter(item=product.item) if product else Step.objects.none()
        super().__init__(*args, **kwargs)
        # Tạo trường nhập cho từng bước
        for step in steps:
            self.fields[f'progress_{step.id}'] = forms.DecimalField(
                initial=self.get_initial_progress(product, step),
                max_digits=5,
                decimal_places=2,
                required=False,
                label=f"{step.name} (Tiến độ)"
            )
    def get_initial_progress(self, product, step):
        # Lấy tiến độ của bước tương ứng với sản phẩm
        progress = ProductStepProgress.objects.filter(product=product, step=step).first()
        return progress.progress_percent if progress else 0