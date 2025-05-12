from django.shortcuts import render, get_object_or_404
from core.models import Fixture
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpRequest
from core.models import predictions


# Create your views here.
@login_required
def index(request):
    fixtures=Fixture.objects.all()
    predictions =[f.predictions.filter(user=request.user).first() for f in fixtures]
    context = {
        'fixtures_and_preditctions' : zip(fixtures,predictions),
    }
    return render(request, 'index.html', context)

@login_required
@require_POST
def submit_prediction(request,fixture_pk):
    fixture = get_object_or_404(Fixture, pk=fixture_pk)
    home_goals= int(request.POST.get('home_goals'))
    away_goals= int(request.POST.get('away_goals'))

    prediction = predictions.object.filter(fixture=fixture, user=request.user).filter()
    if prediction:
        prediction.home_goals = home_goals
        prediction.away_goals = away_goals
        prediction.save()
    else:
        prediction= predictions.objects.create(
            user=request.user,
            fixture=fixture,
            home_goals=home_goals,
            away_goals=away_goals
        )
    