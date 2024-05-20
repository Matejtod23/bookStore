from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def details(request, id):
    book = Book.objects.get(id=id)
    return render(request, "details.html", {"book" : book})

def add(request):
    if request.method == "POST":
        form_data = BookForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            book = form_data.save(commit=False)
            book.image = form_data.cleaned_data['image']
            book.save()
            return redirect("index")
    return render(request, "book_add.html", context={"form":BookForm})