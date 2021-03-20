from django.shortcuts import render
from .models import Advisor, BoardMember

# Create your views here.


def board_page(request):
    advisors = Advisor.objects.all()
    board_members = BoardMember.objects.all()
    board_dict = {
        "advisors" : advisors,
        "board_members" : board_members
    }
    return render(request, "board.html", board_dict)

