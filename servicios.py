# servicios.py
from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError
from logs import GestorLogs

class Servicio(ABC):
    """Clase abstracta para los servicios ofrecidos por Software FJ."""
    def __init__(self, id_servicio, nombre, costo_base):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0.0, descuento=0.0):
        """Método sobrecargado (simulado con valores por defecto) para calcular costos."""
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

class ServicioSala(Servicio):
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        try:
            if horas <= 0:
                raise DatosInvalidosError("Las horas de reserva de sala deben ser mayores a cero.")
            costo_total = (self.costo_base * horas) 
            costo_final = costo_total + (costo_total * impuesto) - descuento
            return max(0, costo_final)
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Cálculo fallido en ServicioSala {self.id_servicio}: {e.mensaje}")
            raise

    def describir_servicio(self):
        return f"Reserva de Sala: {self.nombre} - Costo por hora: ${self.costo_base}"

class ServicioEquipo(Servicio):
    def calcular_costo(self, dias, impuesto=0.0, descuento=0.0):
        try:
            if dias <= 0:
                raise DatosInvalidosError("Los días de alquiler de equipo deben ser mayores a cero.")
            costo_total = (self.costo_base * dias)
            costo_final = costo_total + (costo_total * impuesto) - descuento
            return max(0, costo_final)
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Cálculo fallido en ServicioEquipo {self.id_servicio}: {e.mensaje}")
            raise

    def describir_servicio(self):
        return f"Alquiler de Equipo: {self.nombre} - Costo por día: ${self.costo_base}"

class ServicioAsesoria(Servicio):
    def calcular_costo(self, sesiones, impuesto=0.0, descuento=0.0):
        try:
            if sesiones <= 0:
                raise DatosInvalidosError("El número de sesiones de asesoría debe ser mayor a cero.")
            costo_total = (self.costo_base * sesiones)
            costo_final = costo_total + (costo_total * impuesto) - descuento
            return max(0, costo_final)
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Cálculo fallido en ServicioAsesoria {self.id_servicio}: {e.mensaje}")
            raise

    def describir_servicio(self):
        return f"Asesoría Especializada: {self.nombre} - Costo por sesión: ${self.costo_base}"