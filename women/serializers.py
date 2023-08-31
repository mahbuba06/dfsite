from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from women.models import Women
import io


class WomenModel:
    def init(self, title, content, cat_id):
        self.title = title
        self.content = content
        self.cat_id = cat_id


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = [
            "title",
            "content",
            "cat",
            "photo",
            "user",
        ]


def encode():
    model = WomenModel("Ainazik Paizullaeva", "Ноутбук алды", True)
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    decode = io.BytesIO(b'{"title":"Ainazik Paizullaeva","content":"\xd0\x9d\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba \xd0\xb0\xd0\xbb\xd0\xb4\xd1\x8b","is_published":true}')
    data = JSONParser().parse(decode)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)


# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = [
#             'id',
#             'title',
#             'content',
#         ]
