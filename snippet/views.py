from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import redirect
from .models import *
from .serializers import *
# Create your views here.



# class SnippetAPI(APIView):
#     permission_classes=[IsAuthenticated,]
#     serializer_class=SnippetSerializer
#     def get(self, request):
#         try:
#             rst_snippet_data = Snippet.objects.all()
#             if request.GET.get('id'):
#                 rst_snippet_data = rst_snippet_data.filter(id=request.GET.get('id')).first()
#                 serializer = SnippetSerializer(rst_snippet_data)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             serializer = SnippetSerializer(rst_snippet_data, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'status':0, 'reason':str(e), 'message':'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def post(self, request):
#         try:
#             serializer = SnippetSerializer(data=request.data,context={'request': request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'status':0, 'reason':str(e), 'message':'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def put(self, request):
#         try:
#             if request.GET.get('id'):
#                 rst_snippet_data = Snippet.objects.filter(id=request.GET.get('id'))
#                 serializer = SnippetSerializer(rst_snippet_data, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'status':0, 'reason':str(e), 'message':'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def delete(self, request):
#         try:
#             if request.GET.get('id'):
#                 rst_factory_data = Snippet.objects.filter(id=request.GET.get('id')).delete()
#             return redirect('/snippet_api/')
#         except Exception as e:
#             return Response({'status':0, 'reason':str(e), 'message':'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SnippetLinkAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Snippet.objects.all()
    serializer_class = SnipeetLinkSerializer

    @action(detail=False)
    def count(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        content = {'count': count}
        return Response(content)


class TagAPI(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    def retrieve(self, request, pk):
        rst_snippet_data = Snippet.objects.filter(tag_id=pk)
        serializer = SnippetSerializer(rst_snippet_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
