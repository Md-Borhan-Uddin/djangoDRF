from functools import partial
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog
from blog.seriealizers import PostSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(request, id=None):
    
    if request.method == 'GET':
        
        if id :
            post = Blog.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            post = Blog.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"ok"})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        post = Blog.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"ok"})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        post = Blog.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"ok"})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        post = Blog.objects.get(id=id)
        post.delete()
        return Response({"delete":"ok"})

# class base view

class PostAPIView(APIView):

    def get(self,request, id=None, format=None):
        if id :
            try:
                post = Blog.objects.get(id=id)
            
                serializer = PostSerializer(post)
                return Response(serializer.data)
            except:
                return Response({"msg":"there have no data that searching "})
        else:
            post = Blog.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mes":"data save successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id, format=None):
        post = Blog.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mes":"data update successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self,request,id, format=None):
        post = Blog.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mes":"data update successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        try:
            post = Blog.objects.get(id=id)
            post.delete()
            return Response({"msg":"delete successfully"})
        except:
            return Response({"msg":"some things want wrang"})


#GenericAPI view

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class PostList(ListModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SinglePost(RetrieveModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostCreate(CreateModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdate(UpdateModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class PostDelete(DestroyModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#short from of generic view


class ListAndCreate(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer




class UpdateDeleteRetrive(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer
