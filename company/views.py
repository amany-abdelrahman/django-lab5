from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from company.forms import EmpForm, EmpForm2, TeamForm
from company.models import Emp, Team

# Create your views here.
def EmpView(request):
    if request.method=="GET":
        myform=EmpForm()
        return render(request,'company/create_emp.html',{'form':myform})
    if request.method=="POST":
        myform=EmpForm(request.POST)
        if myform.is_valid():
            team_id = request.POST["team"] 
            team = Team.objects.get(pk=team_id)
            Emp.objects.create(name=request.POST["name"],
                               salary=request.POST["salary"],
                               title=request.POST["title"],
                               team=team)
            return render(request,'company/create_emp.html',{'form':myform})
    return HttpResponse("Heloooooooo")


def EmpView2(request):
    if request.method=="GET":
        myform=EmpForm2()
        return render(request,'company/create_emp.html',{'form':myform})
    if request.method=="POST":
        myform=EmpForm2(request.POST)
        if myform.is_valid(): 
            myform.save()           
            return render(request,'company/create_emp.html',{'form':myform})
    return HttpResponse("Helooo")



from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Team, Emp

# class TeamView(View):
#     def get(self, request):
#         return render(request, 'company/create_team.html')
#     def post(self, request):
#         name = request.POST.get('name')
#         manager_name = request.POST.get('manager')

#         if name and manager_name:
#             manager = Emp.objects.filter(name=manager_name).first()

#             if manager:
#                 Team.objects.create(name=name, manager=manager)
#                 return HttpResponse('Hellooooooooooo')
#             else:
#                 return HttpResponse('Manager not found', status=400)
#         else:
#             return HttpResponse('Invalid request', status=400)


def TeamView(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Hellooooooooo")
    else:
        form = TeamForm()
    return render(request, 'company/create_team.html', {'form': form})