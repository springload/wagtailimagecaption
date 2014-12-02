import json

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required

from wagtail.wagtailadmin.modal_workflow import render_modal_workflow
from wagtail.wagtailimages.models import Image


@permission_required('wagtailadmin.access_admin')
def imagecaption_remove(request, image_id):
    print image_id
    try:
        image = Image.objects.get(id=image_id)
        if image.imagecaption.count() > 0:
            imagecaption = image.imagecaption.all()[0]
            imagecaption.delete()

        return render_modal_workflow(
            request,
            None,
            "wagtailimagecaption/remover/imagecaption_removed.js",
            {
                'response': json.dumps({
                    'status': True,
                    'image_id': image_id,
                })
            }
        )
    except ObjectDoesNotExist:
        return None
