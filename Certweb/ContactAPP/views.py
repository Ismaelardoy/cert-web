from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, get_connection
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Elegir backend según entorno
            if settings.DEBUG:
                # Desarrollo: consola
                connection = get_connection('django.core.mail.backends.console.EmailBackend')
            else:
                # Producción: SMTP real
                connection = get_connection(
                    'django.core.mail.backends.smtp.EmailBackend',
                    host=settings.EMAIL_HOST,
                    port=settings.EMAIL_PORT,
                    username=settings.EMAIL_HOST_USER,
                    password=settings.EMAIL_HOST_PASSWORD,
                    use_tls=settings.EMAIL_USE_TLS
                )

            send_mail(
                subject=f"Solicitud Certificado Energético - {data['nombre']}",
                message=f"""
Nombre: {data['nombre']}
Email: {data['email']}
Teléfono: {data['telefono']}
Dirección: {data['direccion']}
Mensaje: {data['mensaje']}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                connection=connection
            )

            return render(request, "ContactAPP/thanks.html")
    else:
        form = ContactForm()
    return render(request, "ContactAPP/contact.html", {"form": form})