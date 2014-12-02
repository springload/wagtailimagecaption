from wagtail.wagtailcore import hooks
from django.conf.urls import include, url
from wagtailimagecaption import images_urls
from django.utils.html import format_html_join, format_html
from django.conf import settings
from django.core.urlresolvers import reverse


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^captions/', include(images_urls)),
    ]


@hooks.register('insert_editor_css')
def editor_css():
    """
    Add extra CSS files to the admin
    """
    css_files = [
        'wagtailadmin/css/caption.css',
    ]

    css_includes = format_html_join(
        '\n', '<link rel="stylesheet" href="{0}{1}">', ((settings.STATIC_URL, filename) for filename in css_files))
    return css_includes


@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin
    """
    js_files = [
        'wagtailimagecaption/js/image-editor.js',
    ]

    js_includes = format_html_join(
        '\n', '<script src="{0}{1}"></script>', ((settings.STATIC_URL, filename) for filename in js_files))

    js_includes = js_includes + format_html("""
            <script>
                window.chooserUrls.imageCaption = '{0}';
            </script>
        """, reverse('imagecaption_set')
    )

    return js_includes
