from django.urls import path
from . import views

urlpatterns = [

    path('', views.design_list, name='all-designs'),
    path('add-design/',views.add_design, name='adddesign'),
    path('update-design/<str:id>', views.update_design, name="update"),
    path('delete/<str:id>', views.delete_design, name="delete")
]