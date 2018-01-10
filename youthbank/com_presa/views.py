from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from .models import PostModel

def get_post(request, slug):
    post = get_object_or_404(PostModel,slug=slug)
    return render(request, 'ComunicatPresa.html', {'post':post})
