import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(hora) >= 19:
	print ("Ya es hora de ir a casa") 
else:
	print (f"Faltan {18- int(hora)} horas y {59-int(minutos)} minutos para ir a casa"
