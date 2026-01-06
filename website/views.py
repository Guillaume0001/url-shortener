from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from dotenv import load_dotenv
from .models import URL
import json
import os

load_dotenv

def index(request, id):
    url = get_object_or_404(URL, id=id)
    return redirect(url.link)

def check_token(request):
    token = request.headers.get("X-API-KEY")
    if token != os.getenv("API_KEY"):
        return False
    return True

@csrf_exempt
def create_url(request):
    if not check_token(request):
        return HttpResponseForbidden("Unauthorized")
    if request.method == "POST":
        data = json.loads(request.body)
        link = data.get("short_url")
        if not link:
            return JsonResponse({"error": "Missing short_url"}, status=400)
        url = URL.objects.create(link=link)
        return JsonResponse({"url": f"https://{request.build_absolute_uri()}/{url.id}"})

def list_urls(request):
    urls = [{"id": u.id, "link": u.link, "url": f"https://{request.build_absolute_uri()}/{u.id}"} for u in URL.objects.all()]
    return JsonResponse(urls, safe=False)

@csrf_exempt
def update_url(request, uid):
    if not check_token(request):
        return HttpResponseForbidden("Unauthorized")
    url = get_object_or_404(URL, id=uid)
    if request.method == "PUT":
        data = json.loads(request.body)
        url.link = data.get("short_url", url.link)
        url.save()
        return JsonResponse({"id": url.id, "link": url.link, "url": f"https://{request.build_absolute_uri()}/{url.id}"})

@csrf_exempt
def delete_url(request, uid):
    if not check_token(request):
        return HttpResponseForbidden("Unauthorized")
    url = get_object_or_404(URL, id=uid)
    if request.method == "DELETE":
        url.delete()
        return JsonResponse({"result": "success"})