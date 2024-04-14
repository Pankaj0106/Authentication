from django.views.generic import TemplateView

class home(TemplateView):
    template_name = 'index.html'

class thanks(TemplateView):
    template_name = 'thanks.html'