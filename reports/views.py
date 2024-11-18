from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from weasyprint import HTML

def report_preview(request):
    report_content = "This is the report data."
    return render(request, 'report.html', {'report_content': report_content})


def report_download(request):
    report_content = "This is the report data."
    html_string = render_to_string('report.html', {'report_content': report_content})
    pdf_file = BytesIO()
    HTML(string=html_string).write_pdf(pdf_file)
    pdf_file.seek(0)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response

# Create your views here.
