from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    # # desabilita csrf para essas rotas
    # permission_classes = ()
    # authentication_classes = ()

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
