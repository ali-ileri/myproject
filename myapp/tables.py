import django_tables2 as tables
from .models import Kaynak

class KaynaklarTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{{ record.pk }}/edit">Düzenle</a>')
    delete = tables.TemplateColumn('<a href="{{ record.pk }}/delete">Sil</a>')

    class Meta:
        model = Kaynak
        template_name = 'django_tables2/bootstrap.html'
        fields = ('kaynak_no', 'kaynak_yontemi', 'kaynakci_adi', 'wps_no', 'ndt_yontem', 'ndt_sonucu', 'edit', 'delete')
