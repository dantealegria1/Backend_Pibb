import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Appwrite client
client = Client()
client.set_endpoint(os.getenv("APPWRITE_ENDPOINT"))
client.set_project(os.getenv("APPWRITE_PROJECT"))
client.set_key(os.getenv("APPWRITE_API_KEY"))

# Initialize Appwrite database service
databases = Databases(client)

# Database & Collection IDs from .env
DATABASE_ID = os.getenv("APPWRITE_DATABASE_ID")
COLLECTION_ID = os.getenv("APPWRITE_COLLECTION_ID")
COLLECTION_USERS = os.getenv("APPWRITE_USER_COLLECTION_ID")

def get_task_by_user(request):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            user = data.get('username')

            if not username:
                return JsonResponse({'error': 'Username are required'}, status=400)
            task_by_user = databases.list_documents(database_id=DATABASE_ID, collection_id=COLLECTION_ID)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)
    return JsonResponse({'error':'Invalid request method'}, status=400)

def get_user(request):
    if request.method == 'GET':
        try:
            users = databases.list_documents(database_id=DATABASE_ID,collection_id=COLLECTION_USERS)
            return JsonResponse({'Users': users['documents']}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_task(request):
    if request.method == 'GET':
        try:
            todos = databases.list_documents(database_id=DATABASE_ID, collection_id=COLLECTION_ID)
            return JsonResponse({'tasks': todos['documents']}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

