import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'build/static'))