from cli.cli import CLI 
import locale


try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252') 
    except locale.Error:
        print("Advertencia: No se pudo configurar el locale para español. Los días de la semana podrían salir en inglés.")

if __name__ == "__main__":
    mi_interfaz = CLI()
    mi_interfaz.iniciar()