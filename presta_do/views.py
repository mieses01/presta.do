from django.shortcuts import render
from .models import Cliente,sexo
from .forms import ClienteForm

def customer(request):
        clientes = Cliente.objects.all()
        return render(request, 'presta_do/customer.html', {'clientes':clientes})
def cliente_new(request):
        sexos = sexo.objects.all()
        if request.method == "POST":
            form = ClienteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = ClienteForm()
        return render(request, 'presta_do/customer.html', {'form': form,'sexos': sexos})