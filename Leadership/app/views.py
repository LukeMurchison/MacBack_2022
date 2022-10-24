from django.http import HttpResponse
from django.shortcuts import render
from dataclasses import dataclass

# Create your views here.
@dataclass
class Team:
    name: str
    decs: str
    members: str

def procurement(request, input):
    context = {
        'procurement' : Team("procurement", "Procurement team gets necessary items for Base Camp and provides food every day.", "Luke, Mike, Rivers, Anna, Zaul, Dylan"),
        'management' : Team("management", "Management team keeps Base Camp clean, organized, and keeps inventory. ", "Brooks, Chevy, Errin, Kevin, Lukas, Andrew"),
        'documentation' : Team("documentation", "Documentation team keeps up with all the events and milestones at Base Camp and manges the social media.", "Colt, Isaiah, Cooper, Cannon, Angela, Antonio, Gabriel"),
        'community' : Team("community", "Community team organizes events for Base Camp and keeps track of the birthdays and celebrations.", "Joshua, Malcolm, Amber, J.W, Eric"),
        'key': input,

    }
    return render(request, "app/procurement.html", context)

def list(request):
    return render(request, "app/list.html")