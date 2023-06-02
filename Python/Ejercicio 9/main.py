import datetime

now = datetime.datetime.now()
hora_de_irse = now.replace(hour=19, minute=0)

flag_go = True if hora_de_irse <= now else False


if flag_go:
    print('Es hora de irse a casa!')
else:
    horas_faltantes = hora_de_irse - now
    print('Falta', horas_faltantes, 'para irse a casa')
