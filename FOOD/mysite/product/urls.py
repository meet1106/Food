from django.conf.urls import url,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf import settings


urlpatterns=[
    url('resturent', resturent_data,name='rest_data'),
    # url(r'^resturent/(?P<pk>\d+)/$', resturent_data,name='rest_data_with_pk'),
    url('(?P<id>\d+)/$',product_data,name='pro_data'),
    # url('^ad/(?P<product_id>\d+)$',cart_data,name='cart_datas'),
    # url('cart',cart_view,name='cart_s
    # url('updates/(?P<n1>\d+)/(?P<n2>\d+)$',update_quantity,name='update_view'),
    # url('updates/$',update_quantity,name='update_view')
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

]
