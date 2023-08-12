from django.shortcuts import render,redirect
from django.contrib.auth import logout
from item.models import Category, Item
from .forms import SignupForm


def index(req):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:9]
    categories = Category.objects.all()
    return render(req, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(req):
    return render(req, 'core/contact.html')


def signup(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()
    return render(req, 'core/signup.html', {
        'form': form
    })

def logout_view(req):
    logout(req)
    return redirect('core:index')