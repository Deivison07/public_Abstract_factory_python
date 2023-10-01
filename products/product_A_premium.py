from products.interface_product_A import InterfaceProductA


class ProductAPremium(InterfaceProductA):

    def start(self):
        print('Produto(A) Premium iniciado')
    
    def description(self):
        print('Descrição do produto(A) Premium')
