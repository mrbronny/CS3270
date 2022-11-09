from abc import ABC, abstractmethod
from dataclasses import dataclass

customers = {}
items = {}
orders = {}

@dataclass
class Customer():

  def __init__(self, cust_id, name, street, city, state, postal_code, phone, email):
    self.cust_id = cust_id
    self.name = name
    self.street = street
    self.city = city
    self.state = state
    self.postal_code = postal_code
    self.phone = phone
    self.email = email

  @staticmethod
  def read_customers(fname):
    with open(fname, "r") as file:
      file = file.readlines()
      for line in file:
        line = line.strip()
        line = line.split(",")
        customers[line[0]] = Customer(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]) 

  def __str__(self):
    return f"Customer ID #{self.cust_id}:\n{self.name}, ph. {self.phone}, email: {self.email}\n{self.street}\n{self.city}, {self.state} {self.postal_code}"

#---------------------------------------------------

class Item():

  def __init__(self, item_id, description, price):
    self.item_id = item_id
    self.description = description
    self.price = price

  @staticmethod
  def read_items(fname):
    with open(fname, "r") as file:
      file = file.readlines()
      for line in file:
        line = line.strip()
        line = line.split(",")
        items[line[0]] = Item(line[0],line[1],float(line[2]))

#---------------------------------------------------

class LineItem():

  def __init__(self, item_id, qty):
    self.item_id = item_id
    self.qty = qty

  def sub_total(self):
    return items[self.item_id].price * self.qty

#---------------------------------------------------

class Payment(ABC):

  def __init__(self, amount):
    self.amount = amount

  @abstractmethod
  def __str__(self):
    pass

class Credit(Payment):

  def __init__(self, amount, card_number, exp_date):
    Payment.__init__(self, amount)
    self.card_number = card_number
    self.exp_date = exp_date

  def __str__(self):
    return f"Amount: ${self.amount:.2f}, Paid by Credit Card {self.card_number}, exp. {self.exp_date}"

class PayPal(Payment):

  def __init__(self, amount, paypal_id):
    Payment.__init__(self, amount)
    self.paypal_id = paypal_id

  def __str__(self):
    return f"Amount: ${self.amount:.2f}, Paid by Paypal ID: {self.paypal_id}"

class WireTransfer(Payment):

  def __init__(self, amount, bank_id, account_id):
    Payment.__init__(self, amount)
    self.bank_id = bank_id
    self.account_id = account_id

  def __str__(self):
    return f"Amount: ${self.amount:.2f}, Paid by Wire transfer from Bank ID {self.bank_id}, Account# {self.account_id}"

#---------------------------------------------------

class Order():

  def __init__(self, order_id, order_date, cust_id, line_items, payment):
    self.order_id = order_id
    self.order_date = order_date
    self.cust_id = cust_id
    self.line_items = line_items
    self.payment = payment

  def total(self):
    return self.payment.amount

  @staticmethod
  def read_orders(fname):
    with open(fname, "r") as file:
      file = file.readlines()
      i = 0
      while i < len(file):
        order = file[i].strip().split(",")
        info = order[:3]
        sales = order[3:]
        line_items = []
        for pair in sales:
          pair = pair.split("-")
          line_items.append(LineItem(pair[0],int(pair[1])))
        line_items.sort(key=lambda x: x.item_id, reverse=False)
        result = 0
        for l in line_items:
          result += l.sub_total()
        i += 1
        pay = file[i].strip().split(",")
        if pay[0] == "1":
          method = Credit(result,pay[1],pay[2])
        if pay[0] == "2":
          method = PayPal(result,pay[1])
        if pay[0] == "3":
          method = WireTransfer(result,pay[1],pay[2])
        orders[info[1]] = Order(info[1],info[2],info[0],line_items,method)
        i += 1

  def __str__(self):
    stryng = f"=" * 30
    stryng += f"\nOrder #{self.order_id}, Date: {self.order_date}\n{self.payment}\n\n{customers[self.cust_id]}\n\nOrder Detail:\n"
    for i in self.line_items:
      stryng += f"\tItem {i.item_id}: '{items[i.item_id].description}', {i.qty} @ {items[i.item_id].price:.2f}\n"
    return stryng + f"\n"

#---------------------------------------------------

def main():
  Customer.read_customers("customers.txt") 
  Item.read_items("items.txt") 
  Order.read_orders("orders.txt")
  with open("order_report.txt","w") as file:
    for order in orders:
      file.write(f"{orders[order]}")

if __name__ == "__main__":
  main()