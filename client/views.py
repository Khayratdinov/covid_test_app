from django.shortcuts import render
from client.models import Client
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.


def client_detail(request, slug):
    client = Client.objects.get(slug=slug)
    return render(request, 'client_detail.html', {'client': client})


def client_list(request):   
    clients = Client.objects.all()

    return render(request, 'client_list.html', {'clients': clients})





def client_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    client = get_object_or_404(Client, pk=pk)

    template_path = 'pdf_template.html'
    context = {'client': client}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # find the template and render it.
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'


    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)


    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

