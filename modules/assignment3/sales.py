SALES_TAX = 6

def get_tax_amount(cost):
    tax_amount = cost * (SALES_TAX / 100)
    return tax_amount

def get_total_cost(cost):
    tax_amount = get_tax_amount(cost)
    total_amount = tax_amount + cost
    return total_amount

