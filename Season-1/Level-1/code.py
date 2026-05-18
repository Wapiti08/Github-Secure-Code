'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_AMOUNT = 1000000
MAX_QUANTITY = 100
MIN_QUANTITY=0
MAX_TOTAL = 1e6 # maximum total amount accepted for an order

def validorder(order: Order):
    # need to distinguish expenses and payments to check the middle process
    expenses = Decimal('0')
    payments = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            # check whether the amount is right type
            if -MAX_AMOUNT<=item.amount <= MAX_AMOUNT:
                payments += Decimal(str(item.amount))

        elif item.type == 'product':
            if isinstance(item.quantity, int) and MIN_QUANTITY<item.quantity <=MAX_QUANTITY and 0 < item.amount <= MAX_AMOUNT:
                expenses += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    
    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id