from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario


class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = (IsAuthenticated,)                   

    def list(self, request):
        print('Get  a todos los usuarios')
        queryset =  self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
        
class UsuarioRetrieveUpdateDelteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "id"
    lookup_url_kwarg = 'pk'
    #permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        print('Get a usuario')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):    
        print('Put a usuario')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
        return super().put(request, *args, **kwargs)
   

    def delete(self, request, *args, **kwargs):
        print('Delete a usuario')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
        return super().delete(request, *args, **kwargs)