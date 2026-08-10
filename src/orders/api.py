from .pricing import line_total


def create_order(customer, lines):
    return {"customer": customer, "lines": list(lines), "status": "new"}


def order_total(order):
    return sum(line_total(line) for line in order["lines"])


def set_status(order, status):
    order["status"] = status
    return order
