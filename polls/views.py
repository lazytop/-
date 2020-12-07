from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Person
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people":people})

def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()

        return HttpResponseRedirect("/polls")
def edit(request, id):
    try:
        person=Person.objects.get(id=id)
        if request.method == "POST":
            person.name=request.POST.get("name")
            person.age=request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/polls")
        else:
            return render(request,"edit.html", {"person":person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
def delete(request,id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/polls")
    except Person.DoesNotExist:
        return (HttpResponseNotFound("<h2>Person not found</h2>"))


