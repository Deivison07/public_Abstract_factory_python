from products.interface_product_A import InterfaceProductA


class ProductASimple(InterfaceProductA):

    def start(self):
        print('Produto(A) SIMPLES iniciado')
    
    def description(self):
        print('Descrição do produto(A) SIMPLES')
