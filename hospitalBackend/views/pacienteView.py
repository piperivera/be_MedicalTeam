from rest_framework import status
from rest_framework.response import Response
from hospitalBackend.models.paciente import Paciente
from hospitalBackend.serializers.pacienteSerializer import PacienteSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])

def createpaciente(request):
    if request.method == 'GET':
        modelo = Paciente.objects.all()
        seraializer = PacienteSerializer(modelo,many=True)
        return Response(seraializer.data)
    elif request.method == 'POST':
        seraializer = PacienteSerializer(data=request.data)
        if seraializer.is_valid():
            seraializer.save()
            return Response(seraializer.data, status=status.HTTP_201_CREATED)
        return Response(seraializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','DELETE'])

def detailpaciente(request,pk):
    if request.method == 'PUT':
        modelo = Paciente.objects.get(pk=pk)
        seraializer = PacienteSerializer(modelo,data=request.data)
        if seraializer.is_valid():
            seraializer.save()
            return Response(seraializer.data, status=status.HTTP_201_CREATED)
        return Response(seraializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        modelo = Paciente.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

