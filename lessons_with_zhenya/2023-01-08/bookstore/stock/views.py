# View 1 will generate a random item every time it's called
# View 2 will return a response with a list of all existing items

from django.http import HttpResponse
import random

even__two_digit_numbers = [x for x in range(10, 100, 2)]


def random_item(request):
    return_value = random.choice(even__two_digit_numbers)
    return HttpResponse(return_value)


def all_items(request):
    return HttpResponse(even__two_digit_numbers)
