from django.http import Http404
from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status, mixins, generics
from rest_framework.response import Response


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SnippetDetail(APIView):
    '''
    updates or deletes snippet
    '''

    def get(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pl, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
