from django.urls import path
from User import views
app_name='User'
urlpatterns = [
    path('profile/',views.profile,name="profile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('viewproduct/',views.viewproduct,name="viewproduct"),
]