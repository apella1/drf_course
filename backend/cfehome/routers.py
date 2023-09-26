"""Application routers"""
from rest_framework.routers import DefaultRouter

# from products.viewsets import ProductViewSet
from products.viewsets import ProductGenericViewSet

# Creating an instance of the default router
router = DefaultRouter()

router.register("products-abc", ProductGenericViewSet, "products")

urlpatterns = router.urls
print(urlpatterns)
