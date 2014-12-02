from django.conf.urls import url

from wagtailimagecaption.views import chooser
from wagtailimagecaption.views import remover


urlpatterns = [
    url(r'^chooser/imagecaption/$', chooser.imagecaption_set, name='imagecaption_set'),
    url(r'^chooser/imagecaption/(\d+)/$', chooser.imagecaption_chosen, name='imagecaption_chosen'),

    url(r'^remover/imagecaption/(\d+)/$', remover.imagecaption_remove, name='imagecaption_remove'),
]
