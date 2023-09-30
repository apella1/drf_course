from django.urls import path
from . import views

# mapped to /api/products/
urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),
    # path("", views.ProductMixinsView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product-detail"),
    # path("<int:pk>/", views.ProductMixinsView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view(), name="product-edit"),
    # path("<int:pk>/update/", views.ProductMixinsView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view()),
    # path("<int:pk>/delete/", views.ProductMixinsView.as_view()),
    # path("<int:pk>", views.product_detail_api_view)
]
