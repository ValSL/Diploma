from django.shortcuts import render, redirect
from .models import Counterparty
from .forms import CounterpartiesForm
from django.contrib.auth.decorators import login_required


@login_required
def counterparty_list(request):
    cp = Counterparty.objects.filter(created_user=request.user.profile)
    return render(request, 'counterparty/cp_list.html', {'cps': cp, 'section': 'cp'})


def counterparty_create(request):
    if request.method == 'POST':
        form = CounterpartiesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user.profile
            form.save()
            return redirect('counterparties:counterparties_list')
        return render(request, 'counterparty/cp_create.html', {'form': form})
    else:
        form = CounterpartiesForm()
        return render(request, 'counterparty/cp_create.html', {'form': form})
