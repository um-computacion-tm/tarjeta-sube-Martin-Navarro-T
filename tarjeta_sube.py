import unittest

class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

# Valores constantes
PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"

PRECIO_TICKET = 70
DESACTIVADO = "desactivado"
ACTIVADO = "activado"

DESCUENTOS = {
    PRIMARIO: 50, #porcentaje 0.5
    SECUNDARIO: 40, #porcentaje 0.4
    UNIVERSITARIO: 30, #porcentaje 0.3
    JUBILADO: 25, #porcentaje 0.25
}
class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return PRECIO_TICKET - (PRECIO_TICKET * (PRIMARIO/100))
        if self.grupo_beneficiario == SECUNDARIO:
            return PRECIO_TICKET - (PRECIO_TICKET * (SECUNDARIO/100))
        if self.grupo_beneficiario == UNIVERSITARIO:
            return PRECIO_TICKET - (PRECIO_TICKET * (UNIVERSITARIO/100))
        if self.grupo_beneficiario == JUBILADO:
            return PRECIO_TICKET - (PRECIO_TICKET * (JUBILADO/100))
        else:
            return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        if self.grupo_beneficiario == None:
            if self.saldo < self.obtener_precio_ticket():
                raise NoHaySaldoException()
            else:
                self.saldo -= self.obtener_precio_ticket() 
        
        else: 
            if self.saldo < self.obtener_precio_ticket():
                raise NoHaySaldoException()
            else:
                self.saldo -= self.obtener_precio_ticket()
    
    def cambiar_estado(self,nuevoEstado):
        if nuevoEstado == ACTIVADO or nuevoEstado == DESACTIVADO:
            self.estado = nuevoEstado
        else:
            raise EstadoNoExistenteException()

if __name__ == '__main__':
    unittest.main()