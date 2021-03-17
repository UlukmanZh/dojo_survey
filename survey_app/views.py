from django.shortcuts import render, redirect

def index (request):
    locations = [
        'San Jose',
        'Chicago',
        'Austin',
        'New York'
    ]
    languages = [
        'Python',
        'Java',
        'C#',
        'Javascript'
    ]
    context = {
        'locations': locations,
        'languages': languages
    }
    return render(request, "index.html", context)

def result (request):
    name_form = request.POST['name']
    location_form = request.POST['locations']
    language_form = request.POST['languages']
    comments_form = request.POST['comments']
    context = {
        'name_temp': name_form,
        'location_temp': location_form,
        'language_temp': language_form,
        'comments_temp': comments_form
    }

    return render(request, "action.html", context)

def back(request):
    return redirect('/')



