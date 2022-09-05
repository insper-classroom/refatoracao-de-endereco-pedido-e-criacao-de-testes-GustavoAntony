from classes.Pedido import Pedido


class Pagamento:
    def __init__(self,pedido:Pedido):
        self.pedido = pedido
        self.pagamento = pedido.pagamento 
    def get_status(self):
        return self.pagamento

    def processa_pagamento(self):
        self.pagamento = 'pago'
    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        if self.pagamento == 'pago':
            return True

    