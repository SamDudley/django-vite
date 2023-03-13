# django-vite

## Quick start

### Django

1. Add `django_vite` to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    "django_vite",
]
```

2. Add the following to your settings file:

```python
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "dist",
]

# Vite
# https://vitejs.dev/guide/backend-integration.html

# Set to False in production environments!
VITE_DEV = True
VITE_DEV_SERVER_URL = "http://localhost:5173"
VITE_MANIFEST_PATH = BASE_DIR / "frontend" / "dist" / "manifest.json"
```

3. Load the template tags and add the dev client plus any css and js:

```html
{% load vite %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>django-vite</title>
    {% vite_css "main.css" %}
  </head>
  <body>
    <h1>django-vite</h1>
    {% vite_dev_client %} {% vite_js "main.js" %}
  </body>
</html>
```

### Vite

https://vitejs.dev/guide/backend-integration.html

Check out the following in the example project:

- vite.config.js
- templates/base.html
- frontend/main.js
