from django.urls import path
from . import views
urlpatterns = [
    path('create_product_group/', views.create_product_group, name='create_product_group'),
    path('create_product_item/', views.create_product_item, name='create_product_item'),
    path('create_product/', views.create_product, name='create_product'),
    path('product_group_list/', views.product_group_list, name='product_group_list'),
    path('product_item_list/', views.product_item_list, name='product_item_list'),
    path('progress_list/', views.progress_list, name='progress_list'),
    path('products/group/', views.product_list_by_group, name='product_list_by_group'),
    path('progress/update/<int:product_id>/', views.update_progress, name='update_progress'),
    # 01/6/2025 update dùng cho việc các Phân xưởng đặt hàng
    path('Pxdathang/', views.order_form, name='PXdathang'), # tao ra cai dat hang
    path('danhsach/', views.order_list, name='order_list'), # tap hop danh sach don vi da dat
    path('chitiet/<int:pk>/', views.order_detail, name='order_detail'), # chi tiet tran thai
    path('orders/review/', views.order_review_list, name='order_review_list'), #tap hop danh sach cho B1 duyet
    path('orders/<int:pk>/review/', views.order_review_detail, name='order_review_detail'), # trang duyet tung phieu cua B1
    path('orders/execution/', views.order_execution_list, name='order_execution_list'), # tap hop cac phieu duoc yeu cau
    path('orders/<int:pk>/execution/', views.order_execution_detail, name='order_execution_detail'),# xem noi dung phieu
    path('orders/norm/', views.order_norm_list, name='order_norm_list'),  # Danh sách phiếu cho đơn vị định mức
    path('orders/norm/<int:pk>/', views.order_norm_detail, name='order_norm_detail'),  # Chi tiết phiếu cho đơn vị định mức
    path('products/', views.product_list_view, name='product_list'),
    path('products/<int:product_id>/orders/', views.order_items_by_product, name='order_items_by_product'),
    path('orders/<int:order_form_id>/', views.order_form_detail, name='order_form_detail'),
    path('dashboard_sum/', views.dashboard_sum, name='dashboard_sum'),
    path('enter-product-progress/', views.enter_product_progress, name='enter_product_progress'),

]
