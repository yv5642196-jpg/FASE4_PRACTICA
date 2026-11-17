import datetime

class GestorLogs:
    """Clase encargada de registrar eventos y excepciones en un archivo de texto plano."""
    
    ARCHIVO_LOG = "registro_eventos.log"

    @staticmethod
    def registrar_evento(nivel, mensaje):
        """Registra un mensaje en el archivo de log con su fecha, hora y nivel (INFO, ERROR)."""
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea_log = f"[{fecha_hora}] [{nivel}] - {mensaje}\n"
        
        # Bloque try/except/finally básico para la gestión del archivo
        try:
            with open(GestorLogs.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
                archivo.write(linea_log)
        except Exception as e:
            print(f"Error crítico al intentar escribir en el log: {e}")