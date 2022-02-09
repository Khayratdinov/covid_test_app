from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('client_list/', views.client_list, name='client_list'),
    path('client_detail/<slug:slug>/', views.client_detail, name='client_detail'),
    path('client_pdf_view/<int:pk>/', views.client_pdf_view, name='client_pdf_view'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
