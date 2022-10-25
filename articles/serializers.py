from rest_framework import serializers
from articles.models import Articles

class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        #모든 필드를 받아주는것 __all__
        fields = '__all__'
