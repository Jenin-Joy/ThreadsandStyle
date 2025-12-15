from django.urls import path
from Seller import views
app_name='Seller'
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('changepassword/', views.changepassword, name="changepassword"),

    path('product/', views.product, name="product"),
    path('handleProduct/<int:id>', views.handleProduct, name="handleProduct"),

    path('productcolor/', views.productcolor, name="productcolor"),
    path('handleProductcolor/<int:id>', views.handleProductcolor, name="handleProductcolor"),

    path('productsize/', views.productsize, name="productsize"),
    path('handleProductsize/<int:id>', views.handleProductsize, name="handleProductsize"),

    path('stock/', views.stock, name="stock"),
    path('handleStock/<int:id>', views.handleStock, name="handleStock"),

    path('gallery/', views.gallery, name="gallery"),
    path('handleGallery/<int:id>', views.handleGallery, name="handleGallery"),
]