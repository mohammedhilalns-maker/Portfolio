

from django.urls import path
from .import views





urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_view_about/', views.admin_view_about, name='admin_view_about'),
    path('view_contact/', views.view_contact, name='view_contact'),

    path('about/', views.about, name='about'),

    path('resume/', views.resume, name='resume'),

    path('add_about/', views.add_about, name='add_about'),
    path('update_about/<int:id>/', views.update_about, name='update_about'),
    path('add_personal_details/', views.add_personal_details, name='add_personal_details'),
    path('add_education/', views.add_education, name='add_education'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('add_certificate/', views.add_certificate, name='add_certificate'),
    path('add_language/', views.add_language, name='add_language'),
    path('add_skill/', views.add_skill, name='add_skill'),

    path('contacts/', views.contacts, name='contacts'),
]
