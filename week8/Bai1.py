class Device:
    def __init__(self, name: str, price: float, identity: int, location: str):
        """
        Initialize the device information.
        """
        self.name = name
        self.price = price
        self.identity = identity
        self.location = location

    def describe(self):
        """
        Print the details of the device.
        """
        print("Name:", self.name, "- Price:", self.price)
        print("Identity:", self.identity, "- Location:", self.location)

device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()

device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()
