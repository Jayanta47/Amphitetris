from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


def postview(request):
    content = {
        'id': 40,
        'name': 'J&Kenterprise',
        'tenderno': 45,
        'tendertitle': 'need clothes',
        'publish_date': '25/9/20',
        'closing_date': '30/9/20',
        'description': 'Need superior quality linen',
        'category': 'clothes',
    }

    return render(request, 'mainpost.html', {'post_data': [content]})


def postdetail(request, pk):
    post_details = {
        'id': pk,
        'cmp_name': "J&Kenterprise",
        'address': "mirpur",
        'tendertitle': 'need clothes',
        'publish_date': '25/9/20',
        'closing_date': '30/9/20',
        'description': 'Need superior quality linen',
        'category': 'clothes',
    }
    return render(request, 'post_detail.html', {'details': post_details})