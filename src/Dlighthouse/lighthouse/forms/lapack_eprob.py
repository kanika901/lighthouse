from django import forms
from django.db.models import get_model
from lighthouse.models.lapack_eprob import *


def makeFieldRadio(name):
    if name in eprob_fields:
    	field_label, field_choices = eprob_fields[name]
    	return forms.ChoiceField(label=field_label, choices=field_choices, widget=forms.RadioSelect())
    else:
        return forms.ChoiceField(widget=forms.RadioSelect)

def makeFieldCheckbox(name):
    if name in eprob_fields:        
    	field_label, field_choices = eprob_fields[name]
    	return forms.MultipleChoiceField(label=field_label, choices=field_choices, widget=forms.CheckboxSelectMultiple(), required = False)
    else:
        return forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

### ---------------- Form Classes  ---------------- ###


class SimpleForm(forms.Form):
    def __init__(self, name = 'problem' , *args, **kwargs):
        super(SimpleForm, self).__init__(*args, **kwargs)
        self.fields[name] = makeFieldRadio(name)

class FilteredForm(forms.Form):
    def __init__(self, name, filtered, *args, **kwargs):
        super(FilteredForm, self).__init__(*args, **kwargs)
        self.fields[name] = forms.ChoiceField(label=eprob_fields[name][0],
                choices=getFilteredChoices(filtered,name), widget=forms.RadioSelect())


class AdvancedFilteredForm(forms.Form):
    def __init__(self, name,filtered, *args, **kwargs):
        super(AdvancedFilteredForm, self).__init__(*args, **kwargs)
        formslist = getFilteredChoicesAdvanced(filtered, name)
        for formname,field_label,field_choices in formslist:
            self.fields[formname] = forms.MultipleChoiceField(label=field_label, choices=field_choices, widget=forms.CheckboxSelectMultiple(), required = False)

class AdvancedForm(forms.Form):
	def __init__(self, formname, *args, **kwargs):
		super(AdvancedForm, self).__init__(*args, **kwargs)
		for label in eprob_advanced_forms[formname]:
			self.fields[label] = makeFieldCheckbox(label)
