import random


class Product:
    def __init__(self, name, price, primary_key):
        self.name = name
        self.price = price
        self.primary_key = primary_key

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.price})"


raw_products = list(
    {
        ("Razer DeathAdder V3 Pro", 124.90),
        ("Logitech G Pro X Wireless", 129.00),
        ("Microsoft Surface Keyboard", 109.99),
        ("A4Tech Bloody B120", 19.99),
        ("Samsung Galaxy S23", 999.00),
        ("Apple iPhone 14", 1099.00),
        ("Xiaomi Redmi Note 12", 249.00),
        ("Microsoft Surface KeyCaps", 109.98),
        ("Razer BlackShark V2 X", 79.99),
        ("Razer Barracuda X", 89.99),
        ("Razer Kraken V3 Pro", 169.99),
        ("Razer Barracuda Pro", 199.99),
        ("Razer Barracuda", 149.99),
        ("Razer Wolverine V2 Chroma", 159.99),
        ("Razer DeathStalker V2 Pro", 199.90),
        ("Razer DeathStalker V2 Pro Tenkeyless", 179.90),
        ("Razer DeathStalker V2", 159.90),
        ("Razer Huntsman Mini Mercury", 119.90),
        ("Razer Ornata V3", 69.99),
        ("Razer Ornata V3 X", 59.99),
        ("Razer Stream Controller", 249.99),
        ("Razer Ring Light", 59.00),
        ("Razer Cobra", 89.90),
        ("Razer Viper V2 Pro", 149.95),
        ("Razer Pro Type", 139.99),
        ("Razer Pro Click", 99.99),
        ("Razer Pro Glide", 18.99),
        ("Razer Orochi V2", 49.99),
        ("Redragon K585 DITI", 64.99),
        ("Redragon K673 PRO", 54.99),
        ("Keychron K3 RGB Blue Switch", 84.99),
        ("Keychron K2 Gateron Red Switch", 89.99),
        ("Keychron K1SE Red Switch", 99.00),
        ("Logitech MX Keys S Black", 109.00),
        ("Logitech MX Keys MINI Pale", 98.99),
        ("Logitech G915 TKL", 179.99),
        ("Logitech G502 X Lightspeed", 149.99),
        ("Logitech MX Master 3S", 119.99),
        ("Logitech MX Vertical", 129.99),
        ("Logitech G Pro X Superlight", 159.99),
        ("Logitech G915 Lightspeed", 249.99),
        ("Logitech G733 Lightspeed", 139.99),
        ("Logitech G Pro X", 128.99),
        ("Logitech G502 HERO", 78.99),
        ("Logitech G604 LIGHTSPEED", 99.95),
        ("Logitech G305 LIGHTSPEED", 58.99),
        ("Logitech G703 LIGHTSPEED", 88.99),
        ("Logitech G Pro", 69.95),
        ("Logitech G502 Lightspeed", 148.99),
        ("EWEADN X87 Bluetooth Type-C", 54.90),
        ("Wooting UwU", 169.99),
        ("TechFurn Katana", 139.49),
    }
)

# Перемешаем
random.shuffle(raw_products)

# Выбираем первые 50 уникальных и создаём экземпляры
products = [
    Product(name, price, idx + 1) for idx, (name, price) in enumerate(raw_products[:50])
]
