from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'redphone/index.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'redphone/about.html')

class CrewView(View):
    def get(self, request):
        return render(request, 'redphone/crew.html')

class ChallengesView(View):
    def get(self, request):
        return render(request, 'redphone/challenges.html')