class Product:
    """Класс описывает продукты питания"""

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    """Класс описывает подобие базы данных"""

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        """Метод возвращает список продуктов"""
        file = open(self.__file_name, "r")
        product_list = file.read()
        file.close()
        return product_list

    def add(self, *products: Product):
        """Метод добавляет продукт в файл/базу.
         Предварительно проверяет на наличие по имени."""
        products_in_file = self.get_products()
        file = open(self.__file_name, "a")
        for element in products:
            if element.name not in products_in_file:
                file.write(f"{str(element)}\n")
            else:
                print(f"Продукт {element.name} уже есть в магазине")
        file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
