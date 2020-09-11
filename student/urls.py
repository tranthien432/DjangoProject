from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('about/', views.about, name='student-about'),
    path('profile/', views.profile, name='student-profile'),
    path('login/', views.login, name='student-login'),
    path('createstudent/', views.createstudent, name='student-list'),

    path('createclass/', views.createclass, name='class-list'),
    path('delete/<int:id>', views.deleteclass, name='delete-class'),
    path('edit/<int:id>', views.editclass, name='edit-class'),
]
