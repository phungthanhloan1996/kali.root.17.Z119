from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
def empty_favicon(request):
    return HttpResponse(status=204)
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add_worker_view, name='add_worker'),
    path('edit_all_worker/', views.edit_all_worker, name='edit_all_worker'),
    path('delete_worker/', views.delete_worker, name='delete_worker'),
    path('director/', views.director_dashboard, name='director_dashboard'),
    path('api/realtime/', views.get_realtime_attendance, name='get_realtime_attendance'),
    path('logout/', views.logout_view, name='logout'),
    path('chamcong/', views.chamcong, name='chamcong'),
    path('base/', views.base, name='base'),
    path('export/excel/', views.export_attendance_excel, name='export_attendance_excel'),
    path('history/', views.history_attendance, name='history'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='password_change_done'),
    path('chamcongngay/', views.chamcongngay, name='chamcongngay'),
    path('favicon.ico', empty_favicon),
]
