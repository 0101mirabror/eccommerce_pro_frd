from django.urls import path, include
from django.contrib import admin
from core import views as core_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# for first model class  
router1 = routers.DefaultRouter()

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
    path('api/', include(router1.urls)),  
]