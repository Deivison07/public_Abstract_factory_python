from category.abstractFactoryCategory import AbstractFactoryCategory
from products.interface_product_A import InterfaceProductA
from products.interface_product_B import InterfaceProductB
from products.product_A_premium import ProductAPremium
from products.product_B_premium import ProductBPremium

class CategoryProductPremium(AbstractFactoryCategory):

    def getProductA(self) -> InterfaceProductA:
        return ProductAPremium() 
    
    def getProductB(self) -> InterfaceProductB: 
        return ProductBPremium()

