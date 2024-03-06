# First Project (Self_Cashier)

Welcome to my first and final Pacman project Self Cashier / Super Cashier! This is a simple self-checkout system implemented in Python. The system allows users to manage items in their shopping cart, perform various operations such as adding, removing, and updating items, calculate the total cost including discounts, and complete the purchase. 

## Flow Chart
#### Welcome | Start - *Input User
-------While loop - Menu----------
- Opsi 1  (Add Item)
- Opsi 2 (Remove or Clear Item) -- While loop remove_choice - break (Menu)
- Opsi 3 (Update Item: Name, Qty & price) -- While loop update_choice - break (Menu)
- Opsi 4 (Check Cart) 
- Opsi 5 (Payment) -- Confirmation (Y/N) - If Y - Print Receipt - break Menu loop.
- Opsi 6 (Exit) -- break

## Features

- Add items to the shopping cart.
- Remove items from the shopping cart.
- Update item details (name, quantity, price) in the shopping cart.
- Calculate total cost with discounts applied.
- Complete the purchase and generate a receipt.
- Check items in the cart.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/Self_Cashier.git
2. Navigate to Project Dictionary:
   ```bash
   cd Self_Cashier
3. Install Required Dependencies:
   ```bash
   pip install tabulate

## Usage
Run the main.py file:
```bash
python main.py
