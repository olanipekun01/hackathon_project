from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = "course"

urlpatterns = [
    path('reg', views.startReg, name="reg"),
    path('', views.dashboard, name="index"),
    path('print', views.printCopy, name="print"),
    path('coursemain', views.courseMain, name="coursemain"),
    path('register', views.register, name="register"),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),
    path('accounts/login/', views.login_view, name="login_view"),
]

 # path('pdf', views.generatePDF, name='pdf'),