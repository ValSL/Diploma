from django.shortcuts import render, redirect
from .models import Counterparty
from .forms import CounterpartiesForm


def counterparty_list(request):
    cp = Counterparty.objects.all()
    return render(request, 'counterparty/cp_list.html', {'cps': cp, 'section': 'cp'})


def counterparty_create(request):
    if request.method == 'POST':
        form = CounterpartiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counterparties:counterparties_list')
        return render(request, 'counterparty/cp_create.html', {'form': form})
    else:
        form = CounterpartiesForm()
        return render(request, 'counterparty/cp_create.html', {'form': form})
