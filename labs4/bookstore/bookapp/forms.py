from django import forms
from .models import Book, PublicationHouse

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


    class Meta:
        model = Book
        fields = '__all__'