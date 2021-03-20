from django.shortcuts import render
from .models import Entry, Author

# Create your views here.

def mainPage(request):
    entrys = Entry.objects.all()
    authors = Author.objects.all()
    return render(request, 'blog.html', {"entrys": entrys, "author": authors})