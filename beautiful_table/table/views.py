from django.shortcuts import render

# Create your views here.

def get_beautiful_table(request):
    return render(request, 'table/table.html')