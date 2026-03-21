#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**requirements.txt:**
```
Django>=5.2
gunicorn
whitenoise