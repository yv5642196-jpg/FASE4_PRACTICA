from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError
from logs import GestorLogs

class EntidadBase(ABC):
    """Clase abstracta que representa entidades generales del sistema."""
    
    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_detalles(self):
        pass

class Cliente(EntidadBase):
    """Clase Cliente con validaciones robustas y encapsulación de datos."""
    
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        # Encapsulación de datos (atributos privados)
        self.__nombre = None
        self.__correo = None
        self.__telefono = None
        
        # Uso de setters para aplicar las validaciones inmediatamente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        try:
            if not valor or len(str(valor).strip()) < 3:
                raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")
            self.__nombre = str(valor).strip()
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Validación de nombre fallida para ID {self.identificador}: {e.mensaje}")
            raise

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        try:
            if not valor or "@" not in str(valor):
                raise DatosInvalidosError("Formato de correo electrónico inválido (falta '@').")
            self.__correo = str(valor).strip()
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Validación de correo fallida para ID {self.identificador}: {e.mensaje}")
            raise

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, valor):
        try:
            if not valor or not str(valor).isdigit():
                raise DatosInvalidosError("El teléfono debe contener únicamente caracteres numéricos.")
            self.__telefono = str(valor).strip()
        except DatosInvalidosError as e:
            GestorLogs.registrar_evento("ERROR", f"Validación de teléfono fallida para ID {self.identificador}: {e.mensaje}")
            raise

    def mostrar_detalles(self):
        return f"Cliente: {self.nombre} | ID: {self.identificador} | Correo: {self.correo} | Tel: {self.telefono}"