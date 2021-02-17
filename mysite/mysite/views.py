from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dailyMeetings(request):
    return render(request, 'dailyMeetings.html')

def projectDocuments(request):
    return render(request, 'projectDocuments.html')