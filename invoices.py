import math
import random


class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    pass

class Service:
    def __init__(self, description, trees, rate, hours):
        self.description = description
        self.trees = trees
        self.rate = rate
        self.hours = hours
        self.cost = self.calc_cost()

    def calc_cost(self):
        return self.rate * self.hours + (self.trees * 300)

    pass

class Invoice:
    def __init__(self, invoice_id, customer, service, cost):
        self.invoices = {}
        self.invoice_id = invoice_id
        self.customer = customer
        self.service = service
        self.cost = cost

    def gen_invoice_id(self):
        self.invoice_id = random.randint(1, 50000)

    def create_invoice(self):
        invoice_id = self.gen_invoice_id()
        print(f"Invoice ID: {invoice_id}")

        name = input("Customer name: ")
        address = input("Customer address: ")
        phone = input("Customer phone number: ")
        customer = Customer(name, address, phone)
        details = input("Service details/description: ")
        trees = int(input("Number of trees: "))
        rate = int(input("Rate per hour: "))
        hours = int(input("Number of hours: "))
        service = Service(details, trees, rate, hours)
        invoice = Invoice(self.invoice_id, customer, service)
        self.invoices[self.invoice_id] = invoice
        print(f"Success! Invoice created: {invoice}")

    def get_invoice(self, invoice_id):
        invoice_request = int(input("Enter invoice ID: "))
        if invoice_request in self.invoices:
            invoice = self.invoices[invoice_request]
            print(f"Invoice ID: {invoice.invoice_id}")
            print(f"Customer name: {invoice.customer.name}")
            print(f"Customer address: {invoice.customer.address}")
            print(f"Customer phone number: {invoice.customer.phone}")
            print(f"Service details/description: {invoice.service.description}")
            print(f"Number of trees: {invoice.service.trees}")
            print(f"Rate per hour: {invoice.service.rate}")
            print(f"Number of hours: {invoice.service.hours}")
            print(f"Total cost: {invoice.service.cost}")


    def print_all_invoices(self):
        """
        Prints all invoices currently stored.
        """
        if not self.invoices:
            print("No invoices found.")
            return

        for invoice in self.invoices:
            invoice.print_invoice()
            print("-" * 50)

# Example usage
invoice_manager = Invoice()

while True:
  print("\nTree Removal Service Invoice Manager")
  print("1. Create An Invoice")
  print("2. Get An Invoice")
  print("3. Print All Invoices")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    invoice_manager.create_invoice()
  elif choice == '2':
    invoice_number = input("Enter Invoice Number: ")
    retrieved_invoice = invoice_manager.get_invoice(invoice_number)
    if retrieved_invoice:
      print("Invoice Details:")
      retrieved_invoice.print_invoice()
    else:
      print("Invoice not found.")
  elif choice == '3':
    invoice_manager.print_all_invoices()
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please try again.")

print("Closing the program.")
