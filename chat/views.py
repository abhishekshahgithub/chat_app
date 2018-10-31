from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Chatter
from .forms import ChatterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("CHATTTTTTTTTTTTTTTTTTTTTTT WORLD.")

def chat_display(request):
	c = Chatter.objects.all()
	context = {
		"object_list": c ,
	}
	return render(request,"chatpage.html",context)

@login_required
def create_chat(request):
	c = Chatter.objects.all()

	form = ChatterForm(request.POST or None )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect('/chat/create/')

	context ={
		"form": form,
		"object_list": c ,
	}
	return render(request,"chat_create.html", context )
