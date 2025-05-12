from core.models import Fixture, Team
from django.utils import timezone

# Register your models here.
def run():
    teams = [
        "Arsenal",
        "Chelsea",
        "Liverpool",
        "Manchester City",
        "Manchester United",
        "Tottenham Hotspur",
        "Real Madrid",
        "Barcelona",
        "Juventus",
        "Inter Milan",
        "Bayern Munich",
        "Ajax",
        "PSG",
        "Porto"
    ]

    for team in teams:
        Team.objects.get_or_create(name=team)

    teams = Team.objects.all()

    for team1, team2 in zip(teams[::2],  teams[1::2]):
        Fixture.objects.get_or_create(home_team=team1, away_team=team2)  


