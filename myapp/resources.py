from import_export import resources
from .models import Kaynak

class KaynakResource(resources.ModelResource):
    class Meta:
        model = Kaynak
        fields = ('kaynak_no', 'kaynak_yontemi', 'kaynakci_adi', 'wps_no', 'ndt_yontem', 'ndt_sonucu')
