from cmath import pi
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.medicoSerializer import MedicoSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.medico import Medico

class MedicoListCreateView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    """ permission_classes = (IsAuthenticated,) """

    def list(self, request):
        print('Get a todos los medicos')
        queryset =  self.get_queryset()
        serializer = MedicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print('Post a medico')
        print(request.data)
        usurioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer (data = usurioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfdata = request.data
        enfdata.update({"Usuario":usuario.id})
        serrializaerEnf = MedicoSerializer(data=enfdata)
        serrializaerEnf.is_valid(raise_exception=True)
        serrializaerEnf.save()
        return Response()(status=status.HTTP_201_CREATED)
        
class MedicoRetrieveUpdateDelteView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    #permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        print('Get a medico')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):    
        print('Put a medico')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
        return super().put(request, *args, **kwargs)
   

    def delete(self, request, *args, **kwargs):
        print('Delete a medico')
        """ if valid_data['user_id'] = kwargs ['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
        return super().delete(request, *args, **kwargs)