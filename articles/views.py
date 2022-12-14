from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles.models import Articles
from articles.serializers import ArticlesSerializers
from drf_yasg.utils import swagger_auto_schema

# @api_view(['GET','POST'])
# def articleAPI(request):
#     if request.method == 'GET':
#         articles = Articles.objects.all()
#         # article = articles[0]
#         # serializer = ArticlesSerializers(articles)
#         #장고의 쿼리 형테를 딕션너리 형태로 변경하는중
#         serializer = ArticlesSerializers(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # print(request.data)
#         serializer = ArticlesSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response()

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Articles.objects.all()
        # article = articles[0]
        # serializer = ArticlesSerializers(articles)
        #장고의 쿼리 형테를 딕션너리 형태로 변경하는중
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=ArticlesSerializers)
    def post(self, request, format=None):
        # print(request.data)
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response()

# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, article_id):
#     if request.method == 'GET':
#         # article = Articles.objects.get(id=article_id)
#         article = get_object_or_404(Articles, id=article_id)
#         serializer = ArticlesSerializers(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         article = get_object_or_404(Articles, id=article_id)
#         serializer = ArticlesSerializers(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         article = get_object_or_404(Articles, id=article_id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        # article = Articles.objects.get(id=article_id)
        article = get_object_or_404(Articles, id=article_id)
        serializer = ArticlesSerializers(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        serializer = ArticlesSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
