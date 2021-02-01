import io
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# 添加对象
snippet = Snippet(code='print("hello, world")\n')
snippet.save()

# 序列化对象
serializer = SnippetSerializer(snippet)
# serializer.data
# 将数据序渲染为json
content = JSONRenderer().render(serializer.data)

# 反序列化
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()

# 获取对象集合，添加标记many=True
serializer = SnippetSerializer(Snippet.objects.all(), many=True)