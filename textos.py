#### CONCEPTOS UTILES DE LA LIBRERIA MYSQL.CONNECTOR####

#               ##################### CURSOR ###################

# """ Es un objeto relacionado con las bases de datos que funciona como nexo para hacer lecturas
#     modifica datos, actualiza, y elimina datos en la BD.
#        EJ: cursor = conexion.cursor() """"
#            

#               #####################  execute() #####################
#   cursor.execute() nos ayudara a hacer las consultas mysql requeridas...
#   EJ: cursor = conexion.cursor()
#       cursor.execute(SELECT database();)"""


#               #####################   fetch   #####################
"""" El metodo .fetch tiene muchas variables, y es el metodo que se utiliza para traer/asignar a variables las consultas 
        hechas a la BD. Sus variaciones dependen de si de la BD estas extrayendo un campo (fetchone) 
        o multiples campos (fetchall)
    
    EJ : cursor = conexion.cursos()
#       cursor.execute(SELECT database();)
#       registro = cursor.fetchone """


#              ##################### .commint() #####################
"""   Este metodo sirve para confirmar la accion que estamos ejecutando 
    
    EJ: cursor = conexion.cursor()
        cursor.execute("INSERT INTO tipousuario (nombre) VALUES ("vigilante")) 
        conexion.commit() 
        """