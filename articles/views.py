from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from articles.models import Articles
from articles.serializers import ArticlesSerializers

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        # article = articles[0]
        # serializer = ArticlesSerializers(articles)
        #장고의 쿼리 형테를 딕션너리 형태로 변경하는중
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response()