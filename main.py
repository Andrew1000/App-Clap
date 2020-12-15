# COMO TAL SWITCH NO EXISTE EN PYTHON PERO PUEDO ENSEÑARTE
# ALGUNAS COSAS PARA QUE MAS O MENOS TE UBIQUES
# EL PROYECTO CONSTA EN HACER QUE EL USUARIO SE REGISTRE Y QUE SE LOGUE Y QUE SE LE MUESTRE ALGUNAS OPC
from hola import opc_chavezvive
from hola import opc_login
from hola import opc_signup
from hola import opc_carnet
from hola import opc_patria
salida = 2
opc = 0
opc_txt = 'elija una de las opciones'
Menu = '''
BIENVENIDO AL FACECLAP LA RED SOCIAL EN DONDE VES QUE COSAS TRAE EL CLAP
                         ELIGE TU TU OPCION
1- CHAVES VIVE
2- INICIAR SESION
3- REGISTRARSE
4- Recibir un bono de 1000$
5- Recibir una canaimita de 64GB de ram

'''


def opc_inicio():
    print(Menu)
    opc = int(input(opc_txt))
    if opc == 1:
        opc_chavezvive()
    elif opc == 2:
        opc_login()
    elif opc == 3:
        opc_signup()
    elif opc == 4:
        opc_carnet()
    elif opc == 5:
        opc_patria()      
    else:
        print('JAJA BECERRA MUY GRACIOSA NO PONGAS OTRAS OPCIONES')
        print(Menu)
        opc = int(input(opc_txt))

    
    opc_inicio()


