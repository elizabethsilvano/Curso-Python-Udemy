from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'SEUEMAIL@GMAIL.COM'
minha_senha = 'SUASENHA'

with open('/home/elizabeths/Documentos/Cursos Itflex/Curso_Python/Seção 5/enviaemail/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome=' Elizabeth', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'SEU NOME'
msg['to'] = 'EMAILDOCLIENTE@GMAIL.COM' 
msg['subject'] = 'ASSUNTO DO E-MAIL'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
