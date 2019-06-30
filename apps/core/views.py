from django.views.generic import TemplateView

app_name = 'core'


class CoreHomeView(TemplateView):
    """Class to be home template render."""

    template_name = 'core_home.html'
