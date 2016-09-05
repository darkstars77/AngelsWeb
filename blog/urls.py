from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^product/(?P<product_id>\d+)$', views.single_product, name='view_single_product'),
    url(r'^search_product/$', views.search_product),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
