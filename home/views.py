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
        return render(request, self.template_name)
