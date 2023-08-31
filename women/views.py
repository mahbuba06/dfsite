from rest_framework import generics, viewsets
from women.models import Women, Category
from women.serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from women.permissions import IsAdminUserOrReadOnly, IsOwnerReadOnly
from women.pagionation import PaginationWomen


class WomenListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    pagination_class = PaginationWomen
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerReadOnly, )


# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk", None)
#         if not pk:
#             return Women.objects.all()[:7]
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=["get"], detail=False)
#     def category(self, request):
#         cats = Category.objects.all().values()
#         return Response({"cats": cats})


# class WomenListAPIView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenCreateAPIView(generics.CreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
