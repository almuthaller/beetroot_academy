# View 1 will generate a random item every time it's called
# View 2 will return a response with a list of all existing items

from django.http import HttpResponse


def generate_new_item(request):
    pass
    return HttpResponse()
