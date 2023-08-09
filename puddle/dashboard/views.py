from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def index(req):
    items = Item.objects.filter(created_by=req.user)

    return render(req, 'dashboard/index.html', {
        'items': items,
    })