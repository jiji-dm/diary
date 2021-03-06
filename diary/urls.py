from django.urls import path
from .import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #/diary
    #汎用ビューを使用する際には、as_view()を記載しなければならない。
    path('add/', views.AddView.as_view(), name='add'), #/diary/add
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]