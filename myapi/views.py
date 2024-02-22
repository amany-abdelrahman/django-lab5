from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from company.models import Emp, Team
from myapi.serializers import EmpSerializer, TeamSerializer

# Create your views here.

# @api_view()
# def EmpFunBaseView(request):
#     employee=Emp.objects.all()
#     # all=[]
#     # for emp in employee:
#     #     all.append({'id':emp.name, 'salary':emp.salary})
#     serializer=EmpSerializer(employee,many=True)
#     return Response(serializer.data)

# @api_view(["GET","POST"])
# def EmpFunBaseView(request,id):
#     if request.method == 'GET':
#         employee=Emp.objects.filter()
#         serializer=EmpSerializer(employee,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data=request.data
#         serializer=EmpSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class EmpFunBaseView(APIView):
    def get(self, request):
        employee = Emp.objects.all()
        serializer = EmpSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = EmpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            employee = Emp.objects.all()
            all_data = EmpSerializer(Emp.objects.all(), many=True)
            return Response({"all": all_data.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = Emp.objects.get(id=pk)
        serializer = EmpSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = Emp.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class EmpFunBaseView(viewsets.ModelViewSet):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = EmpSerializer
#     queryset = Emp.objects.all()
    

class TeamClassViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()