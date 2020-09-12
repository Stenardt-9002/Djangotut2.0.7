from rest_framework import serializers
from .models import Data_article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_article
        fields = ['id','title','author']
    pass
