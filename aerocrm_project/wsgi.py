import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aerocrm_project.settings')
application = get_wsgi_application()



if os.environ.get("DJANGO_SUPERUSER_AUTO_CREATE", "") == "true":
    try:
        from scripts.create_superuser import run
        run()
    except Exception as e:
        print("❗ Ошибка при создании суперпользователя:", e)
