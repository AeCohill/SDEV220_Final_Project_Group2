class Invoice:
    def __init__(self, invoice_number, client_name, service_name, quantity, price):
        self.invoice_number = invoice_number
        self.client_name = client_name
        self.service_name = service_name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity + self.price 
    
# This can be the class we use for the Invoices ^^^



#GUI basic setup 
'''
SDEV220.py
4/24/2024
Basic GUI Setup
'''
import tkinter as tk
from tkinter import ttk 

# Root window 
root = tk.Tk() 
root.title(" ~ Lumber Company Invoices ~ ") 
root.columnconfigure(0, weight=1) 

# Label for the window 
ttk.Label( root, text="~ Lumber Company Invoices ~ ", font=("TkDefaultFont", 16) ).grid() 

# LabelFrame for the invoice form 
drf = ttk.LabelFrame(root, text="* Invoice Form *") 
drf.grid(padx=10, sticky=(tk.E + tk.W)) 
drf.columnconfigure(0, weight=1) 

# Client information - first row 
r_info = ttk.LabelFrame(drf, text="! Client Information !") 
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3): 
    r_info.columnconfigure(i, weight=1) 

variables = {} 
variables["Name"] = tk.StringVar() 
ttk.Label(r_info, text="Name").grid(row=0, column=0) 
ttk.Entry(r_info, textvariable=variables["Name"]).grid(row=1, column=0, sticky=(tk.W + tk.E)) 

variables["Invoice Number"] = tk.StringVar() 
ttk.Label(r_info, text="Invoice Number").grid(row=0, column=1) 
ttk.Entry(r_info, textvariable=variables["Invoice Number"]).grid(row=1, column=1, sticky=(tk.W + tk.E)) 

services = ["Lumber thing", "Another thing", "And one more thing"] 
variables["Services: "] = tk.StringVar() 
ttk.Label(r_info, text="Services: ").grid(row=0, column=2) 
ttk.Combobox( r_info, textvariable=variables["Services: "], values=services ).grid(row=1, column=2, sticky=(tk.W + tk.E)) 


root.mainloop()
