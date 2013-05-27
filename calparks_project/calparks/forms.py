from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, TabHolder,Tab,Div
from calparks.models import ParkInfo, UserRecommendations

class ParkInfoForm(ModelForm):
    class Meta:
        model = ParkInfo
        fields = ( 'name', 'county', 'park_type', 'park_size', 'url', 'average_user_rec') 
    def __init__(self, *args,**kwargs):
        # Call the original __init__ method before assigning field overloads        
        super(ParkInfoForm,self).__init__(*args,**kwargs)
        self.fields['name'].required = True
        self.fields['name'].label = ""
        self.fields['name'].widget.attrs['placeholder'] = u'Park Name'
        self.fields['county'].required = True
        self.fields['county'].label = ""
        self.fields['county'].widget.attrs['placeholder'] = u'Count'
        self.fields['park_type'].required = True
        self.fields['park_type'].label = ""
        self.fields['park_type'].widget.attrs['placeholder'] = u'Park Type'
        self.fields['park_size'].required = True
        self.fields['park_size'].label = ""
        self.fields['park_size'].widget.attrs['placeholder'] = u'Park Size in Acres'
        self.fields['url'].required = True
        self.fields['url'].label = ""
        self.fields['url'].widget.attrs['placeholder'] = u'Park Website link'
        self.fields['average_user_rec'].label = ""
        self.fields['average_user_rec'].widget.attrs['placeholder'] = u'Averagr User recommendaiton'
        self.helper = FormHelper()
        self.helper.help_text_inline = True
        self.helper.layout = Layout (
                        Div(
                            Div('name',css_class='span2'),
                            Div('county',css_class='span2 offset4'),
                            css_class='row-fluid'),
                        Div(
                            Div('park_type',css_class='span2 '),
                            Div('park_size',css_class='span2 offset4'),
                            css_class='row-fluid'),
                        Div(
                            Div('url',css_class='span2'),
                            Div('average_user_rec', css_class='span2 offset4'),
                            css_class='row-fluid'),
            FormActions(
                  Submit('save_changes', 'Save changes', css_class="btn-primary"),
               )
        )

class UserRecommendationsForm(ModelForm):
    class Meta:
        model = UserRecommendations
        fields = ( 'user', 'park', 'comments', 'user_rating')
        widgets = {
            'comments' : forms.Textarea(attrs={'class' : 'desc', 'cols' : 60, 'rows' : 20}),
        }

    def __init__(self, *args,**kwargs):
        # Call the original __init__ method before assigning field overloads        
        super(UserRecommendationsForm,self).__init__(*args,**kwargs)
        self.fields['comments'].required = True
        self.fields['user_rating'].required = True
