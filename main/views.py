from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306203854',
        'name': 'Fariz Muhammad Rayhansyah Ramadhan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)