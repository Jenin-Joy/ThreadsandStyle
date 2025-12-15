from django.urls import path
from Admin import views
app_name='Admin'
urlpatterns = [
    path('district/', views.district,name="district"),
    path('handleDistrict/<int:id>', views.handleDistrict,name="handleDistrict"),

    path('place/', views.place,name="place"),
    path('handlePlace/<int:id>', views.handlePlace,name="handlePlace"),

    path('brand/', views.brand,name="brand"),
    path('handleBrand/<int:id>', views.handleBrand,name="handleBrand"),

    path('category/', views.category,name="category"),
    path('handleCategory/<int:id>', views.handleCategory,name="handleCategory"),

    path('type/', views.type,name="type"),
    path('handleType/<int:id>', views.handleType,name="handleType"),

    path('size/', views.size,name="size"),
    path('handleSize/<int:id>', views.handleSize,name="handleSize"),

    path('color/', views.color,name="color"),
    path('handleColor/<int:id>', views.handleColor,name="handleColor"),

    path('subcategory/', views.subcategory,name="subcategory"),
    path('handleSubcategory/<int:id>', views.handleSubcategory,name="handleSubcategory"),

    path('sellerverification/', views.sellerverification,name="sellerverification"),
    path('handleSellerverification/<int:id>/<int:status>', views.handleSellerverification,name="handleSellerverification"),

    path('deliveryboyverification/', views.deliveryboyverification,name="deliveryboyverification"),
    path('handleDeliveryboyverification/<int:id>/<int:status>', views.handleDeliveryboyverification,name="handleDeliveryboyverification"),
]