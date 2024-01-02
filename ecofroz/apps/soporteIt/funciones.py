import logging
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.template import context, loader

logger = logging.getLogger(__name__)

def envioMail(subject, email, template, queryset, queryset2):
    html_message = loader.render_to_string(
        'soporteIt/%s' %template,
            {
                'aprob':queryset,
                'aprob2':queryset2,
            }
        )
    email_subject = subject
    to_list = email
    mail = EmailMultiAlternatives(
            email_subject, '', '', [to_list], bcc=['desarrolloecofroz@gmail.com'])
    mail.attach_alternative(html_message, "text/html")
    try:
        mail.send()
    except:
        logger.error("Unable to send mail.")