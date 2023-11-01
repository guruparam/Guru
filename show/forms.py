from django.forms import ModelForm
from show.models import Brand, Phonemodel

class brandform(ModelForm):
    class Meta:
        model = Brand
        fields = ['name','image']

class modelform(ModelForm):
    class Meta:
        model = Phonemodel
        fields = ['brand','name','released_year','available_quantities','price',
                  'is_available','image']      