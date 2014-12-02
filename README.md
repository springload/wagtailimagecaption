wagtailimagecaption
==================

Images captions for Wagtail

# Quickstart

``` $ pip install wagtailimagecaption [GITHUB SSH URI]```

add wagtailimagecaption to your settings.py in the INSTALLED_APPS section:

```
...
    'modelcluster',
    'core',
    'wagtailimagecaption',
    'wagtail.contrib.wagtailsitemaps',
...
```

Run migrations:

```
./manage.py migrate wagtailimagecaption

```

Enjoy!