from django.urls import path, include
from . import views

from rest_framework import routers
from .views import ClassViewSet

router = routers.SimpleRouter()
router.register(r'', ClassViewSet)

urlpatterns = [
    path('', views.home, name='student-home'),
    path('about/', views.about, name='student-about'),
    path('profile/', views.profile, name='student-profile'),
    path('login/', views.login, name='student-login'),
    path('createstudent/', views.createstudent, name='student-list'),

    path('createclass/', views.createclass, name='class-list'),
    path('delete/<int:id>', views.deleteclass, name='delete-class'),
    path('edit/<int:id>', views.editclass, name='edit-class'),

    path('api/v1/class/', include(router.urls)),
]
