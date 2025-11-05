import requests
from django.http import JsonResponse

def chat(request):
    user_msg = request.GET.get("q", "")
    res = requests.post("http://ai:8000/chat", json={"message": user_msg})
    return JsonResponse(res.json())