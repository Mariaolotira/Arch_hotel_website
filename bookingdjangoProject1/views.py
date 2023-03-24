from django.shortcuts import render, redirect
from .models import Booking


def bookings(request):
    data = Booking.objects.all()
    context = {'data': data}
    return render(request, "bookings.html", context)


def home(request):
    return render(request, 'index.html')


def project(request):
    return render(request, 'index-1.html')


def services(request):
    return render(request, 'index-2.html')


def blog(request):
    return render(request, 'index-3.html')


def contact(request):
    return render(request, 'index-4.html')


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        clients_quantity = request.POST.get('clients quantity')
        residence = request.POST.get('residence')
        phone = request.POST.get('phone')
        stay_duration = request.POST.get('stay duration')

        query = Booking(name=name, email=email, clients_quantity=clients_quantity, residence=residence, phone=phone,
                        stay_duration=stay_duration)
        query.save()
        return redirect("/")

    return render(request, "bookings.html")


def deleteData(request, id):
    d = Booking.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "bookings.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        clients_quantity = request.POST.get('clients_quantity')
        residence = request.POST.get('residence')
        phone = request.POST.get('phone')
        stay_duration = request.POST.get('stay_duration')

        update_info = Booking.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.clients_quantity = clients_quantity
        update_info.residence = residence
        update_info.phone = phone
        update_info.stay_duration = stay_duration

        update_info.save()
        return redirect("/")

    d = Booking.objects.get(id=id)
    context = {"d": d}
    return render(request, "bookings.html", context)
