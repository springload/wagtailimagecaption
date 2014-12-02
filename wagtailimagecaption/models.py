from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class ImageCaption(models.Model):
    """
    Represents a relationship among an Embed object (of type Video) and an Image
    """
    image = models.ForeignKey(
        related_name='imagecaption',
        blank=True,
        to='wagtailimages.Image',
        null=True,
        unique=True
    )
    caption = models.CharField(max_length=255, blank=False, null=False)


#  Pre Save signals to remove existing instance of the same embed
@receiver(pre_save, sender=ImageCaption)
def pre_imagecaption_save(sender, instance, **kwargs):
    try:
        existing_object = ImageCaption.objects.get(image=instance.image)
        existing_object.delete()
    except ObjectDoesNotExist:
        return
