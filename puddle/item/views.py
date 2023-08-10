from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import logging
from .models import Item
from .forms import EditItemForm, NewItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def new(req):
    if req.method == 'POST':
        form = NewItemForm(req.POST, req.FILES)
        if form.is_valid():
            # commit = false for creating an object but not saving in the DB
            item = form.save(commit=False)
            item.created_by = req.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(req, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def edit(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    if req.method == 'POST':
        form = EditItemForm(req.POST, req.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(req, 'item/editform.html', {
        'pk': pk,
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    item.delete()
    return redirect('dashboard:index')
