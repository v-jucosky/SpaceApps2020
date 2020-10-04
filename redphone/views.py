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

class ChatbotView(View):
    def get(self, request):
        return render(request, 'redphone/chatbot.html')