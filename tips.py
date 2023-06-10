# importar un archivo dede un dir distinto
import sys
sys.path.append("ruta/al/directorio/externo")
# import nombre_del_archivo

# otra forma
nombre_del_archivo = __import__("ruta.al.directorio.externo.nombre_del_archivo")
