print("bienvenido a cajero automatico techbank riwi digital") 
tries = 0
maxtries = 3
password = "1234"
mount= 1000

while tries < maxtries:
    clave = input("ingrese su clave: ")
    if clave == password: 
        print("clave correcta, bienvenido")
        
        print("n---MENU PRINCIPAL---")  
        print("1. consultar saldo")
        print("2. retirar dinero")
        print("3. salir")

        action = int (input ("que desea hacer ?"))
       

    if action == 1:
        print("su saldo es de :", mount) 

    elif action == 2:
        withdraw = int (input("cuanto dinero desea retirar?"))

        if withdraw > mount:
            print(" saldo insufuciente")
        else:
            mount = mount - withdraw 
            print ("valor a retirar: ", withdraw)
            print ("su nuevo saldo es :", mount)

    elif action == 3: 
        print ( " gracias por usar nuestro cajero automatico, vuelva pronto")
        break
