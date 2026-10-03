from django.shortcuts import render
from django.http import HttpResponse
#def home(request):
  #  return HttpResponse("<h1>Hello User !</h1>")
#def home(request):
 #return render(request, "index.html")
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StaffSerializer
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_404_NOT_FOUND
from .models import * 
@api_view(["GET"])
def home(request):
    staffs=Staff.objects.all()
    serData = StaffSerializer(staffs,many=True)
    return Response(serData.data,HTTP_200_OK)

# @api_view(["GET"])
# def staff(request,pk):
#     staff = Staff.objects.get(id=pk)
#     serData=StaffSerializer(staff)
#     return Response(serData.data,HTTP_200_OK)
@api_view(["GET"])
def staff(request,pk):
  try:
    staff = Staff.objects.get(id=pk)
  except Staff.DoesNotExist :
    return Response(data={"msg:err"},status=HTTP_404_NOT_FOUND)
  serData=StaffSerializer(staff)
  return Response(serData.data,HTTP_200_OK)

@api_view(["GET","DELETE"])
def removestaff(request,pk):
  try:
    staff = Staff.objects.get(id=pk)
  except Staff.DoesNotExist :
    return Response(data={"msg:err"},status=HTTP_404_NOT_FOUND)
  staff.delete()
  return Response(status=HTTP_200_OK)

@api_view(["GET","POST"])
def addstaff(request):
    serData = StaffSerializer(data=request.data)
    if serData.is_valid():
      serData.save()
      return Response(data={"msg":"Created"},status=HTTP_201_CREATED)
    return Response(serData.data)

