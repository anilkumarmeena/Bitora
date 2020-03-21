from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def main(request):
	if request.user.username:
		user = request.user
	elif user.username:
		user=user
		request.user = user
	return render(request, 'login/index.html', {'user': user, 'auth': request.user.is_authenticated()})


def index(request):
	return render(request, 'login/index.html')
