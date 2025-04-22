from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentTypeViewSet, DocumentViewSet, PersonalDocumentViewSet

router = DefaultRouter()
router.register(r'types', DocumentTypeViewSet, basename='document-type')
router.register(r'personal', PersonalDocumentViewSet, basename='personal-document')
router.register(r'', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]


