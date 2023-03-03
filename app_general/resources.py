

from .models import noisemap
from import_export import resources

class NoisemapResource(resources.ModelResource):
    class Meta:
        model = noisemap
        

