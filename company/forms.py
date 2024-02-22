from django import forms
from company.models import Emp, Team

class EmpForm(forms.Form):
    name=forms.CharField(max_length=50)
    salary=forms.IntegerField()
    title=forms.CharField(max_length=50)
    team=forms.ChoiceField(choices=[(team.pk,team.pk)for team in Team.objects.all()],required=False)



class EmpForm2(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'manager']
