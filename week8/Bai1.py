class Manufacturer:
    def __init__(self, identity: int, location: str):
        """
        Khoi tao thong tin cua nha san xuat.
        """
        self.identity = identity
        self.location = location

    def inTT(self):
        """
        In thong tin cua nha san xuat.
        """
        print("Identity:", self.identity)
        print("Location:", self.location)


class Device(Manufacturer):
    def __init__(self, name: str, price: float, identity: int, location: str):
        """
        Khoi tao thong tin thiet bi, bao gom ten, gia, ma so va vi tri nha san xuat.
        """
        self.name = name
        self.price = price
        super().__init__(identity, location)

    def inTT(self):
        """
        In thong tin chi tiet cua thiet bi va thong tin cua nha san xuat.
        """
        print("Name:", self.name)
        print("Price:", self.price)
        super().inTT()

device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.inTT()
print()

device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.inTT()
