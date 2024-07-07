from django.shortcuts import render
from .services import get_convert_sum, not_correct_choices
from .forms import ConvForm
from django.http import HttpResponseServerError


def convert_view(request):
    if request.GET:
        form = ConvForm(request.GET)
        if not_correct_choices(form):
            return server_error_500(request, message='Не удалось загрузить коды валют')
        if form.is_valid():
            if form.cleaned_data['from_'] == form.cleaned_data['to']:
                result_sum = form.cleaned_data['sum_']
            else:
                try:
                    result_sum = get_convert_sum(
                        form.cleaned_data['from_'],
                        form.cleaned_data['to'],
                        form.cleaned_data['sum_']
                    )
                except KeyError:
                    return server_error_500(request)
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
        if not_correct_choices(form):
            return server_error_500(request, message='Не удалось загрузить коды валют')
        return render(request, template_name='converterapp/Convert.html', context={'form': form})


def server_error_500(request, message: str = False):
    if message:
        return HttpResponseServerError(f'<h1>{message}</h1>')
    return HttpResponseServerError('<h1>Ошибка со стороны сервера приносим извинения за неудобства</h1>')
