from django.shortcuts import render
from  django.http import  JsonResponse

import paho.mqtt.client as paho
import json

# Create your views here.

from rest_framework.decorators import api_view
from .models import send_command
from .serializers import send_commandSerializers
from rest_framework.response import Response
from rest_framework import status


#@api_view(["GET","POST"])
#def show_list(request):
#    if(request.method=="GET"):
#        data = student.objects.all()
#        serializers = studentserializers(data,many=True)
#        return Response(serializers.data)
#   elif(request.method=="POST"):
#        serializers = studentserializers(data=request.data)
#        if(serializers.is_valid()):
#            serializers.save()
#            return Response(serializers.data,status=status.HTTP_201_CREATED)
#        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def send_commandRequestList(request):
    res={
        "main-path":"/v1.0",
        "send-command-list":"v1.0/send-command-list"
    }
    return Response(res)

@api_view(['GET'])
def send_commandList(request):
    commandList=send_command.objects.all()
    serializer=send_commandSerializers(commandList,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def send_commandDetail(request,pk):
    commandList=send_command.objects.get(id=pk)
    serializer=send_commandSerializers(commandList,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def send_commandCreate(request):
    serializer=send_commandSerializers(data=request.data)
    if serializer.is_valid():
        #serializer.save
        return Response(serializer.data)
        #return Response(serializer.data['topic'])

        topic = json.dumps(serializer.data['topic'])
        print(topic)
        msg = json.dumps(serializer.data['message'])
        broker="192.168.0.158"
        port=1883
        def on_publish(client,userdata,result):             #create function for callback
            print("data published \n")
            pass
        client1= paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret= client1.publish(topic,msg) 


@api_view(['POST'])
def send_commandUpdate(request,pk):
    command=send_command.objects.get(id=pk)
    serializer = send_commandSerializers(instance=command,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def send_commandDelete(request,pk):
    command=send_command.objects.get(id=pk)
    command.delete()
    return Response("Item deleted")