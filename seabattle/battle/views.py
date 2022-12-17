from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Lobby
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from ipware import get_client_ip

def index(request):
	if request.method == 'POST':
		if 'newlobby' in request.POST:
			lobby = Lobby()
			lobby.lock = False;
			lobby.save()
			idlobby = lobby.id
			#return render(request, "startpage/startpage.html", {'id': lobby.id})
			#return HttpResponseRedirect(reverse('battle:detail', lobby.id))
			return redirect('battle:detail', lobby_id = lobby.id)
	return render(request, "startpage/startpage.html")

def detail(request, lobby_id):
	if request.method == 'POST':
		ip, is_routable = get_client_ip(request)
		if ip is None:
			print("No ip")
		else:
			print(ip)
		user = request.user.id
		print(user)
	try:
		lobby = Lobby.objects.get(id = lobby_id)
		return render(request, "game/game.html")
	except:
		raise Http404("Лобби не найдено")
	
