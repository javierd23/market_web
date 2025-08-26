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
        features = [
            {'icon': 'M12 2L6 12h5v8h2v-8h5L12 2z', 'title': 'Velocidad garantizada',
             'desc': 'Disfruta de la máxima velocidad sin interrupciones para todas tus actividades en línea.'},
            {'icon': 'M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z', 'title': 'Instalación rápida',
             'desc': 'Nuestro equipo de profesionales te conectará en tiempo récord y sin complicaciones.'},
            {
                'icon': 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15H9v-2h2v2zm0-4H9v-2h2v2zm0-4H9V7h2v2zm4 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V7h2v2z',
                'title': 'Planes flexibles',
                'desc': 'Elige el plan que mejor se adapte a tus necesidades y presupuesto, sin contratos forzosos.'},
            {'icon': 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 16h-2v-2h2v2zm0-4h-2V7h2v7z',
             'title': 'Soporte técnico 24/7',
             'desc': 'Nuestro equipo de soporte está siempre disponible para ayudarte, cualquier día y a cualquier hora.'}
        ]
        context = {'features': features}

        return render(request, self.template_name, context)


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
