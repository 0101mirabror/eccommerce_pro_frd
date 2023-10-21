from django.urls import path, include
from django.contrib import admin
from core import apiviews as core_apiviews
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from rest_framework import routers
from ecommerce.apiviews import ProductModelViewSet, UserModelViewSet

# for first model class  
router1 = routers.DefaultRouter()
router1.register(r'products', ProductModelViewSet)
#  for second users model clas
router2 = routers.DefaultRouter()
router2.register(r'users', UserModelViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    # django url routes
    path('api/', include(router2.urls)),  
    path('api/', include(router1.urls)),  
    path('contact/', core_apiviews.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
    path('api-com/', include('ecommerce.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = router.urls
