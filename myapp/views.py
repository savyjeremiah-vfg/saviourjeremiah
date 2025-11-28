from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Case, When, Value, BooleanField
from .models import Image, Testimony, Testimonys
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Testimony
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")



def connectgroup(request):
    return render(request, "connectgroup.html")

def eventsingle(request):
    return render(request, "eventsingle.html")

def events(request):
    return render(request, "events.html")

def style(request):
    return render(request, "style.html")

def volunteer(request):
    return render(request, "volunteer.html")

def contact(request):
    return render(request, "contact.html")


def nav(request):
    return render(request, "nav.html")

def styles(request):
    return render(request, "styles.html")



def image(request):
    images = Image.objects.all()
    return render(request, "image.html", {"images": images})


# Form submission view
def MEDIA(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        image = request.FILES.get("image")

        if not name or not message:
            messages.error(request, "Name and message are required.")
            return redirect('MEDIA')

        Testimony.objects.create(
            name=name,
            message=message,
            image=image
        )
        messages.success(request, "Your testimony has been submitted successfully!")
        return redirect('tem')  # Redirect to display page

    return render(request, "Media.html")



# def tem(request):
#     testimonies = Testimonys.objects.all().order_by('-created_at')
#     return render(request, "Tem.html", {"testimonies": testimonies})


# Delete testimony (only for authenticated users)
@login_required
def delete_testimony(request, id):
    testimony = get_object_or_404(Testimony, id=id)
    testimony.delete()
    messages.success(request, "Testimony deleted successfully!")
    return redirect('tem')


def testimony_success(request):
    """
    Shows a success message after submitting a testimony.
    """
    return render(request, "success_redirect.html")



def testimony_page(request):
    """
    Displays testimonies, prioritizing those older than 48 hours.
    """
    now = timezone.now()
    testimonies = Testimonys.objects.annotate(
        older_than_1=Case(
            When(created_at__lte=now - timezone.timedelta(hours=1), then=Value(True)),
            default=Value(False),
            output_field=BooleanField()
        )
    ).order_by('-older_than_1', '-created_at')

    return render(request, "Tem.html", {"testimonies": testimonies})




