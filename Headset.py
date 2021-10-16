class Headset(object):
  """
    blueprint for headset
  """

  def __init__(self, model, color, company, type, connectionType,price):
    self.model = model
    self.color = color
    self.company = company
    self.type = type
    self.connectionType = connectionType
    self.price = price

  def hear(self):
    print("hear")

  def showPrice(self):
    self.price=int(self.price)
    self.price=self.price-0.2 *self.price
    print(self.price)

  

h1 = Headset("Alpha", "red", "HyperX","wired","Usb", "85")

h1.showPrice()