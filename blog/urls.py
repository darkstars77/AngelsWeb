from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^show_write_form/$', views.show_write_form),
    url(r'^DoWriteBoard/$', views.DoWriteBoard),
    url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
]