from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static




app_name = "course"

urlpatterns = [
    path('reg', views.startReg, name="reg"),
    path('', views.dashboard, name="index"),
    path('accounts/changepassword', views.changePassword, name='changepassword'),
    path('print', views.printCopy, name="print"),
    path('coursemain', views.courseMain, name="coursemain"),
    path('register', views.register, name="register"),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),
    path('accounts/login/', views.login_view, name="login_view"),
    path('accounts/logout/', views.logout, name="logout"),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/done/', views.password_reset_request, name='password_reset_done'),
    path('reset/done/', views.password_reset_confirm, name='password_reset_complete'),


    path('instructor/dashboard', views.adminDashboard, name='instructor_dashboard'),
    path('404', views.F404, name='f404')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
 # path('pdf', views.generatePDF, name='pdf'),