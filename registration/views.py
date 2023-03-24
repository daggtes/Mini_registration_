

from rest_framework.response import Response
from registration.models import EducationLevel, Member
from rest_framework.decorators import api_view
from registration.api.serializers import EducationLevelSerializers, MemberSerializers
# Create your views here.
@api_view(['GET'])
def MemberLevelViewSetGet(request):
    tasks = Member.objects.all()
    serializer = MemberSerializers(tasks, many = True)
    return Response(serializer.data) 

@api_view(['POST'])
def MemberLevelViewSetPost(request):
    serializer = MemberSerializers(data=request.data)
    return Response(serializer.data)

@api_view(['POST'])
def MemberLevelViewSetCreate(request):
    serializer = MemberSerializers(data=request.data)

    if serializer. is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def MemberLevelViewSetUpdate(request):
    task = Member.objects.all()
    serializer = MemberSerializers(instance= task, data=request.data)

    if serializer. is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def MemberLevelViewSetDelete(request):
    task = Member.objects.all()
    task.delete

    return Response("item Successfuly delete")