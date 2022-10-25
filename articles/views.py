from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Articles
from articles.serializers import ArticlesSerializers

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    articles = Articles.objects.all()
    # article = articles[0]
    # serializer = ArticlesSerializers(articles)
    serializer = ArticlesSerializers(articles, many=True)
    return Response(serializer.data)