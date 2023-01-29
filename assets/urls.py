from django.urls import path
from .views import CompanyViewSet, EmployeeViewSet


urlpatterns = [
    path('company/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company'),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='company'),
    
    path('employee/', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee'),
    path('employee/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='employee'),

]
