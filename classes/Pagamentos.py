class Pagamento:
    def __init__(self,pedido):
        self.pedido = pedido
        self.__status = 'aberto' 
    def get_status(self):
        return self.__status

    def processa_pagamento(self):
        print('Processando pagamento')
        self.__status = 'pago'
    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        if self.__status == 'pago':
            return True

    