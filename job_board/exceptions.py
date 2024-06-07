# jobboard/exceptions.py
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Add status code to the response data
        response.data['status_code'] = response.status_code

        # Format error messages
        formatted_errors = []
        for key, value in response.data.items():
            if isinstance(value, list):
                formatted_errors.append(f"{key}: {' '.join(value)}")
            else:
                formatted_errors.append(f"{key}: {value}")
        response.data['errors'] = formatted_errors

        # Remove original keys if you only want the formatted errors
        for key in list(response.data.keys()):
            if key not in ['status_code', 'errors']:
                del response.data[key]

    return response
