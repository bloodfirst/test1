import os
import sys

try:
    import django
    django.setup()
except AttributeError:
    pass

sys.path.append("D:/Develop/Python27/Test/Website")
sys.path.append("D:/Develop/Python27/Test/Website/testapp")
sys.path.append("D:/Develop/Python27/Test/Website/testapp/testapp")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi  
application = django.core.handlers.wsgi.WSGIHandler() 
