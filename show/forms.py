from django.forms import ModelForm
from show.models import Brand, Phonemodel, Transaction

class brandform(ModelForm):
    class Meta:
        model = Brand
        fields = ['name','image']

class modelform(ModelForm):
    class Meta:
        model = Phonemodel
        fields = ['brand','name','released_year','available_quantities','price',
                  'is_available','image']    

class Transactionform(ModelForm):
    def __init__(self, *args, **kwargs):
        # Pop the phonemodel instance from kwargs
        phonemodel = kwargs.pop('phonemodel', None)
        
        # Call the parent class's __init__ method
        super(Transactionform, self).__init__(*args, **kwargs)

        # If a phonemodel instance was provided, set the initial values
        if phonemodel:           
            self.fields['amount'].initial = phonemodel.price
            self.fields['model'].initial = phonemodel.name
        

    class Meta:
        model = Transaction
        fields = ['user','model','transaction_type','amount']