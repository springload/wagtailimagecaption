# Wagtail Image Caption

> Images captions for Wagtail

*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

## Quickstart

```sh
pip install git+https://github.com/springload/wagtailimagecaption.git
```

Add wagtailimagecaption to your settings.py in the INSTALLED_APPS section:

```python
...
    'modelcluster',
    'core',
    'wagtailimagecaption',
    'wagtail.contrib.wagtailsitemaps',
...
```

Run migrations:

```sh
./manage.py migrate wagtailimagecaption

```

Enjoy!
