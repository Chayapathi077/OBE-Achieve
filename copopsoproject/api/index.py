from django.core.wsgi import get_wsgi_application
import os
import sys

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copopsoproject.settings')

# Get the WSGI application
application = get_wsgi_application()

def handler(event, context):
    """Handle the Vercel serverless function request"""
    try:
        from django.core.handlers.wsgi import WSGIHandler
        from django.core.handlers.wsgi import WSGIRequest
        from io import BytesIO
        import json

        # Create a WSGI environment
        environ = {
            'REQUEST_METHOD': event.get('httpMethod', 'GET'),
            'PATH_INFO': event.get('path', '/'),
            'QUERY_STRING': event.get('queryStringParameters', {}),
            'wsgi.input': BytesIO(),
            'wsgi.url_scheme': 'https',
            'wsgi.errors': sys.stderr,
            'wsgi.version': (1, 0),
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'SERVER_NAME': 'localhost',
            'SERVER_PORT': '80',
            'CONTENT_TYPE': event.get('headers', {}).get('Content-Type', ''),
            'CONTENT_LENGTH': event.get('headers', {}).get('Content-Length', ''),
        }

        # Add headers
        for key, value in event.get('headers', {}).items():
            environ[f'HTTP_{key.upper().replace("-", "_")}'] = value

        # Create WSGI request
        request = WSGIRequest(environ)
        
        # Get response
        response = application.get_response(request)
        
        # Return response
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.content.decode('utf-8')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'type': type(e).__name__
            })
        } 