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

@csrf_exempt
def set_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate required fields
            username = data.get("username")
            password = data.get("password")  # Ensure it's a string ID
            email = data.get("email", None)  # Optional date

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            # Create the new task in Appwrite
            new_user = databases.create_document(
                database_id=DATABASE_ID,
                collection_id=COLLECTION_USERS,
                document_id=ID.unique(),  # Generate unique ID
                data={
                    "username": username,
                    "password": password,
                    "email": email
                }
            )

            return JsonResponse({'user': new_user}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e),'datos': username+password+email}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt  # Disable CSRF for simplicity
def set_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate required fields
            task_name = data.get("name")
            id_user = data.get("id_user")  # Ensure it's a string ID
            due_to = data.get("due_to", None)  # Optional date
            is_complete = data.get("isComplete", False)  # Default to False description = data.get("description", "")

            if not task_name or not id_user:
                return JsonResponse({'error': 'Task name and user ID are required'}, status=400)

            # Validate `due_to` date format (if provided)
            if due_to:
                try:
                    due_to = datetime.strptime(due_to, "%Y-%m-%d").isoformat()
                except ValueError:
                    return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

            # Create the new task in Appwrite
            new_task = databases.create_document(
                database_id=DATABASE_ID,
                collection_id=COLLECTION_ID,
                document_id=ID.unique(),  # Generate unique ID
                data={
                    "name": task_name,
                    "description": description,
                    "isComplete": is_complete,
                    "id_user": id_user,
                    "due_to": due_to
                }
            )

            return JsonResponse({'task': new_task}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500) 
    return JsonResponse({'error': 'Invalid request method'}, status=400)
