from django.http import JsonResponse, HttpResponse
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import Post


@csrf_exempt
def posts(request):
    if request.method == 'GET':
        blog_list = Post.objects.all()
        serializer = PostSerializer(blog_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, id):
    try:
        blog = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(blog)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)
