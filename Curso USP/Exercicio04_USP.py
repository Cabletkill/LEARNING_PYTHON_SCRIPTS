segundos_str=int(input('Entre com os segundos para converter:'))

horas=segundos_str//3600
segrestante=segundos_str%3600
minutos=segrestante//60
final=segrestante%60
dias=horas  // 24
restohoras=(segundos_str//3600)-(dias*24)

print(dias,'Dias',restohoras,'Horas',minutos,'Minutos e',final,'Segundos')