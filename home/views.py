from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Homepage(View):
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutPage(View):
    template_name = 'home/about.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactPage(View):
    template_name = 'home/contact.html'

    def get(self, request):
        return render(request, self.template_name)

class PlanPage(View):
    template_name = 'home/plan.html'


    def get(self, request):
        plans = [
            {'name': 'Básico', 'velocidad': '10 Mbps', 'soporte': '24/7', 'subida': '5 Mbs', 'latencia_baja': False},
            {'name': 'Esencial', 'velocidad': '50 Mbps', 'soporte': '24/7', 'subida': '25 Mbs', 'latencia_baja': False},
            {'name': 'Intermedio', 'velocidad': '80 Mbps', 'soporte': '24/7', 'subida': '40 Mbs',
             'latencia_baja': True},
            {'name': 'Avanzado', 'velocidad': '100 Mbps', 'soporte': '24/7', 'subida': '50 Mbs', 'latencia_baja': True},
            {'name': 'Premium', 'velocidad': '150 Mbps', 'soporte': '24/7', 'subida': '75 Mbs', 'latencia_baja': True},
            {'name': 'Ultra', 'velocidad': '200 Mbps', 'soporte': 'VIP 24/7', 'subida': '100 Mbs',
             'latencia_baja': True},
        ]

        context = {'plans': plans}
        return render(request, self.template_name, context)
