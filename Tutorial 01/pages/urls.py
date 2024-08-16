from django.urls import path
from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/create/', ProductCreateView.as_view(), name='form'),
]
