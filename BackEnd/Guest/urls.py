from django.urls import path
from Guest import views
app_name='Guest'
urlpatterns = [
    path('user/',views.user, name="user"),   
    path('deliveryboy/',views.deliveryboy, name="deliveryboy"),   
    path('seller/',views.seller, name="seller"),   
    path('login/',views.login, name="login"),   
]