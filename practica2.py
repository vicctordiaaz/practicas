print('Bienvenido a EMPAREJANDO.COM')
print('===============================')
print('Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal')
nombre = input('Tu nombre es: ')
fecha = input('Tu edad es: ')
taburete = input('�Te gusta Taburete? ')
print ('Hola', nombre, '. Si no me equivoco tienes ',fecha , 'a�os.')
if taburete in ('si', 'Si', 'SI'):

  print ("OK Boomer, lo tuyo va a ser un caso dificil")
if taburete in ('no', 'No', 'NO'):
      print("Bueno, al menos es un comienzo. Veremos que se puede hacer contigo")
     

variable = 0

for variable in range(0,200):
    print('Que no cumple',variable)
    variable=variable+1
    if variable == int(fecha):
        break
    
print('�Que si cumpla ',variable,' a�os!')




  
  
  
  
      
     

  

   