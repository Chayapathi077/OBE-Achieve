"""
WSGI config for Vercel deployment
"""

import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copopsoproject.settings')
    application = get_wsgi_application()
    app = application
except Exception as e:
    logger.error(f"Error setting up WSGI application: {str(e)}")
    raise 