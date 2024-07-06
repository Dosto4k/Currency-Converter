from django.shortcuts import render
from .services import get_convert_sum
from .forms import ConvForm


def convert_view(request):
    if request.GET:
        form = ConvForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['from_'] == form.cleaned_data['to']:
                result_sum = form.cleaned_data['sum_']
            else:
                result_sum = get_convert_sum(
                    form.cleaned_data['from_'],
                    form.cleaned_data['to'],
                    form.cleaned_data['sum_']
                )
        else:
            result_sum = False
        context = {
            'form': form,
            'result_sum': result_sum,
            'to': request.GET['to'],
            'from': request.GET['from_'],
            'sum': request.GET['sum_']
        }
        return render(request, template_name='converterapp/Convert.html', context=context)
    else:
        form = ConvForm()
        return render(request, template_name='converterapp/Convert.html', context={'form': form})
