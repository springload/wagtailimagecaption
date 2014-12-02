import json

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist

from wagtail.wagtailadmin.modal_workflow import render_modal_workflow
from wagtail.wagtailimages.models import Image
from wagtailimagecaption.models import ImageCaption
from wagtailimagecaption.forms import *


@permission_required('wagtailadmin.access_admin')
def imagecaption_set(request):
    if request.GET.get('image_id'):
        image_id = request.GET.get('image_id')
        try:
            image = Image.objects.get(id=image_id)
            caption = None
            if image.imagecaption.count() > 0:
                imagecaption = image.imagecaption.all()[0]
                caption = imagecaption.caption
                form = CaptionForm(initial={'caption': caption})
            else:
                form = CaptionForm()
            return render_modal_workflow(
                request,
                "wagtailimagecaption/chooser/caption.html",
                "wagtailimagecaption/chooser/caption.js",
                {
                    'image_id': image.id,
                    'caption': caption,
                    'form': form
                }
            )
        except ObjectDoesNotExist:
            return None


@permission_required('wagtailadmin.access_admin')
def imagecaption_chosen(request, image_id):
    if request.POST:
        form = CaptionForm(request.POST)
        if form.is_valid():
            try:
                if request.POST.get('caption'):
                    image = Image.objects.get(id=image_id)
                    if image.imagecaption.count() > 0:
                        imagecaption = image.imagecaption.all()[0]
                        imagecaption.caption = request.POST.get('caption')
                        imagecaption.save()
                    else:
                        image.imagecaption.add(ImageCaption(image=image, caption=request.POST.get('caption')))
                    return render_modal_workflow(request, None, "wagtailimagecaption/chooser/caption_chosen.js", {
                        'response': json.dumps({'status': True}),
                    })
            except ObjectDoesNotExist:
                return None
    else:
        form = CaptionForm()
    return render_modal_workflow(
        request,
        "wagtailimagecaption/chooser/caption.html",
        "wagtailimagecaption/chooser/caption.js",
        {
            'image_id': image_id,
            'form': form
        }
    )
