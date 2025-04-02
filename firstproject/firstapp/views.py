from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def index(request):
    # Create a simple html page as a string
    template = "<html>" \
               "This is our first view" \
               "</html>"

    # Return template as content argument in HTTP response.
    return HttpResponse(content = template)

def get_date(request):
    today = date.today()
    template = "<html>" \
               f"Today's date is {today}" \
               "</html>"
    
    return HttpResponse(content=template)
