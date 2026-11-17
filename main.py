
from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from excepciones import ServicioNoDisponibleError, DatosInvalidosError, OperacionNoPermitidaError
from logs import GestorLogs

class Reserva:
    """Integra cliente, servicio, duración y estado, procesando la confirmación."""
    def __init__(self, id_reserva, cliente, servicio, duracion):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        GestorLogs.registrar_evento("INFO", f"Iniciando creación de reserva {self.id_reserva}.")

    def confirmar_reserva(self):
        try:
            if not self.servicio.disponible:
                raise ServicioNoDisponibleError(f"El servicio {self.servicio.nombre} no está disponible.")
            
            costo = self.servicio.calcular_costo(self.duracion, impuesto=0.19, descuento=10)
            self.servicio.disponible = False
            self.estado = "Confirmada"
            GestorLogs.registrar_evento("INFO", f"Reserva {self.id_reserva} confirmada. Costo: ${costo}")
            return costo
        except ServicioNoDisponibleError as e:
            self.estado = "Fallida"
            GestorLogs.registrar_evento("ERROR", f"Fallo al confirmar reserva {self.id_reserva}: {e.mensaje}")
            # Encadenamiento de excepciones
            raise OperacionNoPermitidaError("No se pudo confirmar la reserva por falta de disponibilidad.") from e
        except Exception as e:
            self.estado = "Error"
            GestorLogs.registrar_evento("ERROR", f"Error inesperado en reserva {self.id_reserva}: {e}")
            raise
        finally:
            GestorLogs.registrar_evento("INFO", f"Proceso de confirmación finalizado para reserva {self.id_reserva}.")

def ejecutar_simulacion():
    print("Iniciando simulación de Software FJ...")
    GestorLogs.registrar_evento("INFO", "=== INICIO DE SIMULACIÓN ===")
    
    # 1-3: Creación de servicios
    sala = ServicioSala("S01", "Sala de Conferencias A", 50.0)
    equipo = ServicioEquipo("E01", "Proyector 4K", 30.0)
    asesoria = ServicioAsesoria("A01", "Consultoría TI", 100.0)
    
    # 4: Cliente válido
    try:
        cliente_valido = Cliente("C01", "Yamileth Varela", "yv5642196@gmail.com", "3001234567")
        print(cliente_valido.mostrar_detalles())
    except Exception as e:
        print(f"Error creando cliente: {e}")

    # 5: Cliente inválido (nombre corto) - try/except básico
    try:
        cliente_invalido = Cliente("C02", "Al", "al@correo.com", "1234567")
    except DatosInvalidosError as e:
        print(f"Operación 5 (Fallo esperado capturado): {e}")

    # 6: Cliente inválido (correo sin @)
    try:
        cliente_correo = Cliente("C03", "Juan Perez", "juanperez.com", "3009876543")
    except DatosInvalidosError as e:
        print(f"Operación 6 (Fallo esperado capturado): {e}")

    # 7: Reserva exitosa con try/except/else
    try:
        reserva1 = Reserva("R01", cliente_valido, sala, 4)
        costo = reserva1.confirmar_reserva()
    except OperacionNoPermitidaError as e:
        print(f"Error confirmando reserva: {e}")
    else:
        print(f"Operación 7: Reserva {reserva1.id_reserva} exitosa. Costo total: ${costo}")

    # 8: Reserva de servicio ya ocupado (demuestra encadenamiento)
    try:
        reserva2 = Reserva("R02", cliente_valido, sala, 2)
        reserva2.confirmar_reserva()
    except OperacionNoPermitidaError as e:
        print(f"Operación 8 (Fallo esperado capturado): {e} Causa original: {e.__cause__}")

    # 9: Cálculo de costo con duración inválida
    try:
        reserva3 = Reserva("R03", cliente_valido, equipo, -5)
        reserva3.confirmar_reserva()
    except Exception as e:
        print(f"Operación 9 (Fallo esperado capturado): {e}")

    # 10: Reserva válida validando bloque finally
    try:
        reserva4 = Reserva("R04", cliente_valido, asesoria, 2)
        reserva4.confirmar_reserva()
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Operación 10: Finalizada la verificación de la asesoría (Bloque finally ejecutado).")

if __name__ == "__main__":
    ejecutar_simulacion()