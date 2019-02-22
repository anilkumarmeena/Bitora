from rest_framework import serializers
from .models import Entry


class queSerializer(serializers.ModelSerializer):

    blog = serializers.SerializerMethodField()
    class Meta:
        model = Entry
        fields = ("blog", "headline")


    def get_blog(self, obj):
        return_data = None
        if type(obj.blog) == list:
            embedded_list = []
            for item in obj.blog:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.blog.__dict__
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data


        def create(self, validated_data):
            return Entry.create(**validated_data)