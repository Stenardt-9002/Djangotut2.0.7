from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={"placeholder": "Your Title"})
    )

    # override existing tmplate

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "S1" in title:
            raise forms.ValidationError("This is not a valid title  just add S1 in title")
        return title
        pass

    pass


class RawProductform(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your des",
                "class": "new-class"
            }
        )
    )
    price = forms.DecimalField(initial=199.99)


pass


class EditProduct(forms.ModelForm):
    id = forms.IntegerField()

    class Meta:
        model = Product
        fields = [
            'id'
        ]

    def clean_id(self, *args, **kwargs):
        id = self.cleaned_data.get("id")

        obj_get = Product.objects.all()
        obj_list = [query.id for query in obj_get]
        if not id in obj_list:
            raise forms.ValidationError("id not accepted")
        return id