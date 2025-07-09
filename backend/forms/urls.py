from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import FeedbackViewSet  # ✅ import your ViewSet
from django.views.generic import TemplateView

# Create a router and register the FeedbackViewSet
router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ✅ add this line
    path('', TemplateView.as_view(template_name="index.html")),  # React root
]


