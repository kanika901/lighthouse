from django.db import models
from lighthouse.models.lapack_le import lapack_RoutineInfo


PRECISION_CHOICES = (
        (u's', u's(single)'), 
        (u'd', u'd(double)'), 
        (u'c', u'c(complex)'), 
        (u'z', u'z(complex double)'),
)

STANDARD_CHOICES = (
        (u'standard', u'standard'),
        (u'generalized', u'generalized'), 
)

MATRIX_CHOICES = (
        (u'general', u'general'), 
        (u'symmetric', u'symmetric'), 
        (u'Hermitian', u'Hermitian'), 
        (u'SPD', u'SPD'),
        (u'HPD', u'HPD'),
        (u'triangular', u'triangular'),
        (u'SPsD', u'SPsD'),
        (u'HPsD', u'HPsD'),
        (u'upper Hessenberg', u'upper Hessenberg'),
        (u'upper quasi-triangular', u'upper quasi-triangular'),
        )

STORAGE_CHOICES = (
        (u'full', u'full'),
        (u'band', u'band'),
        (u'packed', u'packed'),
        (u'tridiagonal', u'tridiagonal'),
        (u'RFP', u'RFP'),
        (u'full/packed/band/tridiagonal', u'full/packed/band/tridiagonal'),
)

NOYES_CHOICES = (
        (u'no', u'no'),
        (u'yes', u'yes'),    
)

NOYESNONE_CHOICES = (
        (u'no', u'no'),
        (u'yes', u'yes'),
        (u'none', u'none'), 
)


NOYESBOTH_CHOICES = (
        (u'no', u'no'),
        (u'yes', u'yes'),
        (u'no/yes', u'no/yes'), 
)







###---------------- for guided search ----------------###
###--- Eigenproblem ---###
class lapack_eigen(models.Model):
        thePrecision = models.CharField('Precision', max_length=10, choices=PRECISION_CHOICES)
        routineName = models.CharField('Routine Name', max_length=30)
        standardGeneralized = models.CharField('Standard/Generalized', max_length=20, choices=STANDARD_CHOICES)
        matrixType = models.CharField('Matrix Type', max_length=30, choices=MATRIX_CHOICES)
        storageType = models.CharField('Storage', max_length=60, choices=STORAGE_CHOICES)
        selectedEV = models.CharField('Selected Eigenvalues', max_length=10, choices=NOYESNONE_CHOICES)
        eigenvector = models.CharField('Eigenvectors', max_length=10, choices=NOYESBOTH_CHOICES)
        schur = models.CharField('Schur form/vectors', max_length=30, choices=NOYESNONE_CHOICES)
        cndNumber = models.CharField('cndNumber/balance', max_length=10, choices=NOYESNONE_CHOICES)
        notes = models.CharField('Notes', max_length=225)
        info = models.ForeignKey(lapack_RoutineInfo)

        class Admin:
                list_display = ('id', 'thePrecision', 'routineName', 'standardGeneralized', 'matrixType', 'storageType', 'info')

        def __unicode__(self):
                return self.matrixType
                return self.storageType
        
        class Meta:
                app_label = 'lighthouse'
                
                
                
###--- Sylvester ---###
class lapack_sylvester(models.Model):
        thePrecision = models.CharField('Precision', max_length=10, choices=PRECISION_CHOICES)
        routineName = models.CharField('Routine Name', max_length=30)
        standardGeneralized = models.CharField('Standard/Generalized', max_length=20, choices=STANDARD_CHOICES)
        matrixType = models.CharField('Matrix Type', max_length=30, choices=MATRIX_CHOICES)
        storageType = models.CharField('Storage', max_length=60, choices=STORAGE_CHOICES)
        info = models.ForeignKey(lapack_RoutineInfo)

        class Admin:
                list_display = ('id', 'thePrecision', 'routineName', 'standardGeneralized', 'matrixType', 'storageType', 'info')

        def __unicode__(self):
                return self.matrixType
                return self.storageType
        
        class Meta:
                app_label = 'lighthouse'