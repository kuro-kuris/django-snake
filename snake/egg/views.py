from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Pet, User, Saving_Account

class IndexView(generic.ListView):
    model = User
    template_name = 'egg/index.html'

# get all the sub-objects
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'egg/user.html', {'user': user})

class PetView(generic.DetailView):
    model = Pet
    template_name = 'egg/pet.html'
