from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
challenge_task = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for at least 20 minutes everyday.",
    "march": "Learn Django for at least 20 minutes everyday.",
    "april": "Eat no meat for the entire month.",
    "may": "Walk for at least 20 minutes everyday.",
    "june": "Learn Django for at least 20 minutes everyday.",
    "july": "Eat no meat for the entire month.",
    "august": "Walk for at least 20 minutes everyday.",
    "september": "Learn Django for at least 20 minutes everyday.",
    "october": "Eat no meat for the entire month.",
    "november": "Walk for at least 20 minutes everyday.",
    "december": None,
}


def index(request):
    months = list(challenge_task.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_task(request, month):
    try:
        task = challenge_task[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": task
        })
    except:
        raise Http404()


def monthly_challenge_task_by_number(request, month):
    months = list(challenge_task.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month Number")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
