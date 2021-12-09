##Quick Start

Install requirements:

```commandline
pip install -r requirements.txt
```

Create a config.json with fields "ST_SITE_REFERENCE", "ST_JWT_USER" and "ST_JWT_SECRET":

```json
{
        "ST_SITE_REFERENCE": "test_fitzwilliamsports95287",
        "ST_JWT_USER": "jwt@fitzwilliamsports.com",
        "ST_JWT_SECRET": "<secret>"
}
```

Make sure the file is read in at the top of settings.py:

```python
with open("/etc/config.json") as f:
    CONFIG = json.loads(f.read())
```

Run the dev server:

```commandline
python manage.py runserver
```
