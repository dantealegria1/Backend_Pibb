from django.shortcuts import render

# Create your views here.
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

@csrf_exempt  # Disable CSRF for simplicity
def delete_user(request):
     if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data.get('id_user')
            databases.delete_document(DATABASE_ID, COLLECTION_USERS, id_user)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500) 
     return JsonResponse({'error': 'Invalid request method'}, status=400)   

@csrf_exempt  # Disable CSRF for simplicity
def delete_task(request):
     if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data.get('id_task')
            databases.delete_document(DATABASE_ID, COLLECTION_USERS, id_task)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500) 
     return JsonResponse({'error': 'Invalid request method'}, status=400)
