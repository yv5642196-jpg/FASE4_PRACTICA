
class SoftwareFJError(Exception):
    """Clase base para las excepciones personalizadas del sistema Software FJ."""
    pass

class DatosInvalidosError(SoftwareFJError):
    """Excepción lanzada cuando faltan parámetros o los datos del cliente son incorrectos."""
    def __init__(self, mensaje="Se han ingresado datos inválidos o faltan parámetros obligatorios."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ServicioNoDisponibleError(SoftwareFJError):
    """Excepción lanzada cuando se intenta reservar un servicio sin disponibilidad."""
    def __init__(self, mensaje="El servicio solicitado no se encuentra disponible actualmente."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class OperacionNoPermitidaError(SoftwareFJError):
    """Excepción lanzada para cálculos inconsistentes o cancelaciones inválidas."""
    def __init__(self, mensaje="La operación solicitada no está permitida en este estado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)