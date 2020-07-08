from twilio.rest import Client


def send_messages(event=None, context=None):
    twilio_sid = 'tu sid'
    auth_token = 'tu auth token'

    whatsappCliente = Client(twilio_sid, auth_token)
    contactos = {'ganado 1, me haces falta':'+51999999999', 'ganado 2, te quiero': '+51999999999', 'Ganado 3, te amo': '+51999999999'}

    for ganado, numero in contactos.items():
        mensage = whatsappCliente.messages.create(
            body='Buenos dias {} !'.format(ganado),
            from_='whatsapp:+14155238886',
            to='whatsapp:' + numero,
        )
        print(mensage.sid)
    return 'envio exitoso'
