from django.shortcuts import render
from django.views import generic

from apps.main.models import Page, ProductSet


def index(request):
    page = Page.objects.get(slug='home')
    product_sets = ProductSet.objects.filter(is_active=True)
    return render(request, 'index.html', {'page': page, 'product_sets': product_sets})


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    quaryset = Page.objects.all()

    def set_breadcrumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'breadcrumbs': self.set_breadcrumbs()})
        return context
