from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^show_write_form/$', views.show_write_form),
    url(r'^DoWriteBoard/$', views.DoWriteBoard),
    url(r'^product/(?P<product_id>\d+)$', views.single_product, name='view_single_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''prefix 설정 예시
urlpatterns = patterns('photo.views',
    url(r'^photo/$', 'single_photo'),
    url(r'^photo/2$', 'single_photo2'),
    url(r'^photo/3$', 'single_photo3'),
    url(r'^photo/4$', 'single_photo4'),

urlpatterns += patterns('image.views',
    url(r'^photo/5$', 'single_photo5'),
    url(r'^photo/6$', 'single_photo6'),
    url(r'^photo/7$', 'single_photo7'),
    url(r'^photo/8$', 'single_photo8'),
)
'''