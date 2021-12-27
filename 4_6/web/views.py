from django.http import HttpResponse

def sad_msg(request, name):
    msg = f'Nobody likes you, {name}!'
    return HttpResponse(msg)

def happy_msg(request, name, times):
    msg = ''.join([f'You are great, {name} :) \n' for i in range(times)])
    return HttpResponse(msg)