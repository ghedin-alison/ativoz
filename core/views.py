from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Team, Testemonial
from .forms import ContatoForm


# A nossa view, é uma formview, ou seja, uma pagina web que possui um formulario
# nome do template continua sendo index, a classe do formulario ContatoForm e no sucesso a pagina retorna a index
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    # recuperacao de dados para envio ao template
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['team'] = Team.objects.order_by('?').all()
        context['testemonial'] = Testemonial.objects.all()
        return context

    # Se email enviado com sucesso, manda uma mensagem e retorna ao formulario/pagina principal
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # Se email nao for enviado, manda uma mensagem de erro e retorna ao formulario/pagina principal
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class SaibaView(TemplateView):
    template_name = 'saiba.html'
