from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('getandsaveformdata/', views.get_and_save_form_data, name='getandsaveformdata'),
    path('getandsearchformdata/', views.get_and_search_form_data, name='getandsearchformdata'), 
    path('edit/<int:task_id>/', views.task_edit, name='taskedit'),  
    path('complete/<int:task_id>/', views.task_complete, name='taskcomplete'),
    path('delete/<int:task_id>/', views.task_delete, name='deletetask'),
    path('uncomplete/<int:task_id>', views.task_uncomplete, name='mark_uncomplete'),
]