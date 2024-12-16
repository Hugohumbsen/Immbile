from django.shortcuts import render



def list_location(request):
    immobiles = immobile.objects.filter(is_locale=false)
    context = {
        'immobiles' : immobiles
    }
    return render(request, 'list-location.html', context)