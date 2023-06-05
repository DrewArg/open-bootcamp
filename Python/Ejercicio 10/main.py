file =  open("ejer10.txt","w")
file.write("ejercicio 10\n")
file.write("drewArg\n")
file.close()

file = open("ejer10.txt","a")
file.write("otra linea nueva")
file.close()
