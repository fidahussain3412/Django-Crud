from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Items
from .ItemsSerializer import ItemsSerializer


# Create your views here.
#@api_view('GET')
#def CreateItem(request):
 #   return Response({'name':'fida hussain'})

#@api_view('GET')
#def GetItem(request,pk):
 #  return Response()

@api_view(['GET'])
def GetAll(request):
    data=Items.objects.all()
    serializeddata=ItemsSerializer(data,many=True)
    return Response (serializeddata.data)

@api_view(['GET'])
def GetById(request,id):
    data=Items.objects.get(id=id)
    sdata=ItemsSerializer(data,many=False)
    return Response(sdata.data)

@api_view(['POST'])
def StoreData(request):
    serializeddata=ItemsSerializer(data=request.data)
    if serializeddata.is_valid():
        serializeddata.save()
        return Response (serializeddata.data)
    return Response(serializeddata.errors)

@api_view(['GET','PATCH'])
def UpdateData(request,id):
    try:
        data=Items.objects.get(id=id)
    except Exception as e:
        print("Patch request : "+str(e))
        return Response({"excption":"data not found"})
    try:
        data = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return Response({"error": "Data not found"}, status=404)

    if request.method == "GET":  # ✅ Handle GET request
        serializer = ItemsSerializer(data)
        return Response(serializer.data, status=200)


    s_data=ItemsSerializer(data,data=request.data,partial=True)
    if s_data.is_valid():
        s_data.save()
        return Response(s_data.data) 
    else:
        print("data is not valid")
        a={"inavlid data":"invalid"}
        return Response(a)


@api_view(['PUT'])
def UpdateDataFull(request,id):
    try:
        data=Items.objects.get(id=id)
    except Exception as e:
        print("Patch request : "+str(e))
        return Response({"excption":"data of the given id not found"})
    s_data=ItemsSerializer(data,data=request.data)
    if s_data.is_valid():
        s_data.save()
        return Response(s_data.data)
    else:
        print("data is not valid")


@api_view(["GET"])
def main_method(request):
    return Response({
        "1": "path('GetAll/', GetAll, name='GetAll')",
        "2": "path('GetById/<str:id>/', GetById, name='GetById')",
        "3": "path('StoreData/', StoreData, name='StoreData')",
        "4": "path('UpdateData/<str:id>/', UpdateData, name='UpdateData')",
        "5": "path('UpdateDataFull/<str:id>/', UpdateDataFull, name='StoreDataFull')",
        "6": "path('DeleteData/<str:id>/', DeleteData, name='DeleteData')",

    })

@api_view(['DELETE'])
def DeleteData(request, id):
    try:
        data = Items.objects.get(id=id)
        data.delete()
        return Response({"message": "Item deleted successfully"}, status=200)
    except Items.DoesNotExist:
        return Response({"error": "Data not found"}, status=404)
    