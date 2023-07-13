from django.urls import path
from myapp.views import kaynak_list, kaynak_edit, kaynak_delete

urlpatterns = [
    path('', kaynak_list, name='kaynak_list'),
    path('edit/<int:pk>/', kaynak_edit, name='kaynak_edit'),
    path('delete/<int:pk>/', kaynak_delete, name='kaynak_delete'),
]
