from django.shortcuts import render
from .ecc import message

# Create your views here.
def index(request):
    return render(request, 'index.html')


def encrypt(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        encrypted, decrypted = message(msg)
        return render(request, 'index.html', {'enc': encrypted, 'dec': decrypted})