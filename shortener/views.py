from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Url
from django.http import JsonResponse, Http404
from rest_framework import generics
from rest_framework import status
import string
import random
import json
from .serializers import UrlSerializer
class UrlShortener(View):
    def get(self, request):
        return render(request, 'index.html', {})




class createUrl(generics.CreateAPIView):
    def post(self, request):
        short_url = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        serializer = Url(real_url = request.data['url'], generated_link = short_url, url_views = 0)
        serializer.save()
        return JsonResponse({'status': status.HTTP_201_CREATED, 'data' : 'http://' + str(request.META['HTTP_HOST']) + '/l/' + str(serializer) })

def viewUrl(request, generated_link):
        print(generated_link)
        url_object =  Url.objects.get(generated_link=str(generated_link))
        print(url_object)
        url_object.url_views = url_object.url_views + 1
        url_object.save()
        return redirect(str(url_object.real_url))
    

