from category.abstractFactoryCategory import AbstractFactoryCategory
from products.interface_product_A import InterfaceProductA
from products.interface_product_B import InterfaceProductB
from products.product_A_Simple import ProductASimple
from products.product_B_Simple import ProductBSimple


class CategoryProductsSimple(AbstractFactoryCategory):

    def getProductA(self) -> InterfaceProductA:
        return ProductASimple()
    
    def getProductB(self) -> InterfaceProductB:
        return ProductBSimple()