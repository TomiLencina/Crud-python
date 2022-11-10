from bd.conexion import Dao
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================MENU PRINCIPAL==================")
            print("1. Listar cursos")
            print("2. Registrar curso")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Salir")
            print("==================")
            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese de nuevo...")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)
    
def ejecutarOpcion(opcion):
    dao = Dao()
    
    if opcion == 1:
        try:
            cursos=dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error...")

    elif opcion == 2 :
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrio un error...")

    elif opcion ==3:
        try:
            cursos=dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("Codigo del curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error...")

    elif opcion ==4:
        try:
            cursos=dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Codigo de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error...")
    else:
        print("opcion no valida...")    

menuPrincipal()


