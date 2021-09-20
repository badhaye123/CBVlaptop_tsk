from django.urls import path
from .views import LaptopListView, LaptopCreateView, LaptopUpdateView, LaptopDeleteView,homeview

urlpatterns = [
    path('create/', LaptopCreateView.as_view(), name='create'),
    path('show/', LaptopListView.as_view(), name='show'),
    path('update/<int:pk>', LaptopUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', LaptopDeleteView.as_view(), name='delete'),
    path('',homeview,name='home')

]