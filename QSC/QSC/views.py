from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def home_redirect(request):
    return render(request, 'home_redirect.html')
