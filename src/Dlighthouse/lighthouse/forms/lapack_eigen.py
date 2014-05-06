from django import forms
from django.db.models import get_model
from lighthouse.models.lapack_eigen import *
from lighthouse.models.choiceDict import *



######-------- For Guided Search --------######
##---- problem form ---- ##
class problemForm(forms.Form):
    eigen_prob = forms.ChoiceField(label='Which of the following problems would you like to compute?',
					      widget=forms.RadioSelect(),
					      choices=EIGENPROBLEM_CHOICES
					      )    


##---- standard/generalized form ---##
class standardGeneralizedForm(forms.Form):
    eigen_standardGeneralized = forms.ChoiceField(label='Is the problem standard or generalized?',
					      widget=forms.RadioSelect(),
					      choices=STANDARD_CHOICES,
					)
    
    
##---- complex form ----##
class complexNumberForm(forms.Form):
    eigen_complexNumber = forms.ChoiceField(label='Does your matrix have any complex numbers?',
					      widget=forms.RadioSelect(),
					      choices=NOYES_CHOICES
					      )


##---- matrix type form ----##
class matrixTypeForm(forms.Form):
    eigen_matrixType = forms.ChoiceField(label='What is the type of your matrix?', choices=[], widget=forms.RadioSelect())
    def __init__(self, request, *args, **kwargs):
	super(matrixTypeForm, self).__init__(*args, **kwargs)
	self.fields['eigen_matrixType'].choices = request.session['Routines'].values_list('matrixType', 'matrixType').distinct()
	##--- display full names for semidefinite, SPD and HPD ---##
	for i, item in enumerate(self.fields['eigen_matrixType'].choices):
		if 'SPD' in item:
			self.fields['eigen_matrixType'].choices[i] = (u'SPD', u'real symmetric positive definite (SPD)')
		elif 'HPD' in item:
			self.fields['eigen_matrixType'].choices[i] = (u'HPD', u'complex Hermitian positive definite (HPD)')
	##--- order choices by string length ---##
	self.fields['eigen_matrixType'].choices.sort(key=lambda k:len(k[1]))
	if len(self.fields['eigen_matrixType'].choices) == 1:
		self.fields['eigen_matrixType'].initial = self.fields['eigen_matrixType'].choices[0][1]




##---- storage type form ----##
class storageTypeForm(forms.Form):
    eigen_storageType = forms.ChoiceField(label='How is your matrix stored?', choices=[], widget=forms.RadioSelect())
    def __init__(self, request, *args, **kwargs):
	super(storageTypeForm, self).__init__(*args, **kwargs)
	self.fields['eigen_storageType'].choices = request.session['Routines'].values_list('storageType', 'storageType').distinct()
	if (u'full/packed/band/tridiagonal', u'full/packed/band/tridiagonal') in self.fields['eigen_storageType'].choices:
	    self.fields['eigen_storageType'].choices.remove((u'full/packed/band/tridiagonal', u'full/packed/band/tridiagonal'))
	if len(self.fields['eigen_storageType'].choices) == 1:
		self.fields['eigen_storageType'].initial = self.fields['eigen_storageType'].choices[0][1]



##--- selected eigenvalue form ---##
class selectedEVForm(forms.Form):
    eigen_selectedEV = forms.ChoiceField(label='Do you only need eigenvalues within a specific range?',
					 widget=forms.RadioSelect(),
					 choices=NOYES_CHOICES)


    
##--- eigenvectors form ---##
class eigenvectorForm(forms.Form):
    eigen_eigenvector = forms.ChoiceField(label='Do you need eigenvectors?',
					      widget=forms.RadioSelect(),
					      choices=NOYES_CHOICES
					      )
    
    
     
     
##--- condition numbers for eigenvectors form ---##
class cndN_eigenvectorForm(forms.Form):
    eigen_cndN_eigenvector = forms.ChoiceField(label='Would you like to compute the reciprocal condition numbers for the eigenvectors?',
					      widget=forms.RadioSelect(),
					      choices=NOYES_CHOICES
					      )
    
    
         
##--- eigenvectors or Schur form ---##
class schurForm(forms.Form):
    eigen_schur = forms.ChoiceField(label='In addition to eigenvalues, do you need other properties such as Schur form, Schur vectors, and sorted eigenvalues?',
					      widget=forms.RadioSelect(),
					      choices=NOYES_CHOICES
					      )
    
    
##--- condition number form ---##
class cndNumberForm(forms.Form):
    eigen_cndNumber = forms.ChoiceField(label='Do you need a balancing transformation or a reciprocal condition number?',
					      widget=forms.RadioSelect(),
					      choices=NOYES_CHOICES
					      )
    
    
    
##--- precision form ---##
class thePrecisionForm(forms.Form):
    eigen_thePrecision = forms.ChoiceField(label='Would you like to use single or double precision?',
					      widget=forms.RadioSelect(),
					      choices=SINGLEDOUBLE_CHOICES
					      )