fich=open("/etc/passwd","r")
maquinas=fich.readlines()
for maquina in maquinas:
#for maquina in maquinas[:2]:
#lineas[0] sera "pepepepeppepepep"
#lineas[:1] sera ["pepepepeppepepep"]
	
	login = maquina.split(':')[0]
	shell = maquina.split (':')[-1][:-1]
	print ('login: ', login, '	shell: ', shell)
print ('el numero de usuarios es', len(maquinas))
fich.close()

#login = linea.split(':')[0]
#shell = linea.split (':')[-1][:-1]
#print (login, shell)

#login = linea[:linea.find(':')]
#shell = linea[linea.rfind(':')+1:-1] 
#print (login, shell)
