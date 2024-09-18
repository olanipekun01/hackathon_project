from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('coursemain', views.courseMain, name="coursemain"),
    path('register', views.register, name="register"),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),
]