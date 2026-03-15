from django.contrib import admin
from .models import ProductGroup, ProductItem, Product, Step, ProductStepProgress

class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'start_date')
    list_filter = ('item__group', 'item')
    search_fields = ('name',)

class StepAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'estimated_hours', 'order', 'department_in_charge')
    list_filter = ('item',)
    search_fields = ('name',)
    ordering = ('item', 'order')

class ProductStepProgressAdmin(admin.ModelAdmin):
    list_display = ('product', 'step', 'progress_percent', 'last_updated', 'department_in_charge')  # thêm ở đây
    list_filter = ('step__item', 'product', 'department_in_charge')  # thêm nếu muốn lọc theo phòng ban
    search_fields = ('product__name', 'step__name', 'department_in_charge')  # thêm để tìm kiếm theo tên phòng ban
    readonly_fields = ('last_updated',)

from django.contrib import admin
from .models import OrderForm, OrderItem

@admin.register(OrderForm)
class OrderFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordering_unit', 'norm_unit', 'executing_unit', 'order_date', 'status', 'created_by', 'reviewed_by', 'reviewed_at', 'created_at')
    list_filter = ('status', 'order_date', 'ordering_unit', 'executing_unit')
    search_fields = ('ordering_unit__name', 'executing_unit__name', 'created_by__username')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','item_name', 'quantity', 'product', 'due_date', 'order_form')
    list_filter = ('due_date',)
    search_fields = ('item_name', 'product__name')

admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(ProductStepProgress, ProductStepProgressAdmin)
from django.contrib import admin
# Đảm bảo bạn import đúng từ file models của ứng dụng
from .models import ProductNote, ProductDailyProgress 


# --- Cấu hình cho ProductNote ---
@admin.register(ProductNote)
class ProductNoteAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách (list view)
    list_display = ('product', 'content_snippet', 'created_by', 'created_at')
    # Các trường dùng để tìm kiếm
    search_fields = ('product__name', 'content', 'created_by__username')
    # Các trường dùng để lọc
    list_filter = ('created_at', 'created_by')
    # Trường chỉ đọc
    readonly_fields = ('created_at',)
    
    # Hiển thị một phần nội dung thay vì toàn bộ
    def content_snippet(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_snippet.short_description = "Nội dung"


# --- Cấu hình cho ProductDailyProgress ---
@admin.register(ProductDailyProgress)
class ProductDailyProgressAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách (list view)
    list_display = [
        'product',
        'date',
        'progress_percent',
        'planned_progress_percent',
        'approved_factory',
        'approved_department',
        'approved_qc',
        'handed_over'
    ]
    # Các trường dùng để tìm kiếm
    search_fields = ('product__name', 'date')
    # Các trường dùng để lọc
    list_filter = ('date', 'approved_factory', 'approved_department', 'approved_qc', 'handed_over')
    # Sắp xếp mặc định
    ordering = ('-date', 'product__name')
    # Cho phép chỉnh sửa trực tiếp trên list view
    list_editable = (
        'progress_percent', 
        'planned_progress_percent', 
        'approved_factory', 
        'approved_department', 
        'approved_qc', 
        'handed_over'
    )