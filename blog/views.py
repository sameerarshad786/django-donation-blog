from django.shortcuts import render


def home(request):
    return render(request, "blog/home.html")

def donate(request):
    return render(request, "blog/donation.html")

def success(request, args):
    amount = args
    context = {
        "amount": amount,
        "title": "Donation Page",
    }
    return render(request, "blog/success.html", context)
