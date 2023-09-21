from django.urls import path
from . import views

# mapped to /api/products/
urlpatterns = [
    # path("<int:pk>", views.product_detail_api_view)
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("", views.ProductListCreateAPIView.as_view()),
    # path("all/", views.ProductListAPIView.as_view())
]
