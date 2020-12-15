from hola import opc_chavezvive
from hola import opc_login
from hola import opc_signup
salida = 2
opc = 0
opc_txt = 'elija una de las opciones'
Menu = '''
BIENVENIDO AL FACECLAP LA RED SOCIAL EN DONDE VES QUE COSAS TRAE EL CLAP
                         ELIGE TU TU OPCION
1- CHAVES VIVE
2- INICIAR SESION
3- REGISTRARSE

'''
print(Menu)


def opc_inicio():
    opc = int(input('elija una de las opciones'))
    if opc == 1:
        opc_chavezvive()
    elif opc == 2:
        opc_login()
    elif opc == 3:
        opc_signup()
    else:
        print('JAJA BECERRA MUY GRACIOSA NO PONGAS OTRAS OPCIONES')
        print(Menu)
        opc = int(input(opc_txt))
