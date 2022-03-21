#from django.shortcuts import render

# Create your views here.
#from django.http import JsonResponse

from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AgendamentoDoacaoSerializer
from .models import AgendamentoDoacao

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
          'Endpoints': '/notes/',
          'method': 'GET',
          'body': None,
          'description': 'Return an array of notes'  
        },

        {
          'Endpoints': '/notes/id',
          'method': 'GET',
          'body': None,
          'description': 'Return an single note objects'
        },

        {
          'Endpoints': '/notes/id/create',
          'method': 'POST',
          'body': {'body': ""},
          'description': 'Create new note wih data sent in post required'  
        },

        {
          'Endpoints': '/notes/id/update',
          'method': 'PUT',
          'body': {'body': ""},
          'description': 'Creates an existing note with date sent'  
        },

        {
          'Endpoints': '/notes/id/delete',
          'method': 'DELETE',
          'body': None,
          'description': 'Deletes and existing note'  
        },
    ]
    return Response(routes)
  

@api_view(['GET'])
def getAgendamentos(request):
  agendamentos = AgendamentoDoacao.objects.all()
  serializer = AgendamentoDoacaoSerializer(agendamentos, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def getAgendamento(request, pk):
  agendamento = AgendamentoDoacao.objects.get(id=pk)
  serializer = AgendamentoDoacaoSerializer(agendamento, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def createAgendamento(request):
  novo_agendamento = request.data

  agendamento = AgendamentoDoacao.objects.create(
    dat_agendamento = novo_agendamento['dat_agendamento'],
    des_destinatario = novo_agendamento['des_destinatario'],
    mensagem = novo_agendamento['mensagem']
  )

  serializer = AgendamentoDoacaoSerializer(agendamento, many=False)
  
  return Response(serializer.data)


@api_view(['PUT'])
def updateAgendamento(request, pk):
  novo_agendamento = request.data

  agendamento = AgendamentoDoacao.objects.get(id=pk)

  serializer = AgendamentoDoacaoSerializer(agendamento, data=request.data)

  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)


@api_view(['DELETE'])
def deleteAgendamento(request, pk):
  agendamento = AgendamentoDoacao.objects.get(id=pk)
  agendamento.delete()

  return Response('Agendamento excluído')