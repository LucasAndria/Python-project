from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Enseignant
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def listeAll(request):
    enseignants = Enseignant.objects.all()
    return render(request, "liste.html",
                  {'enseignants': enseignants})