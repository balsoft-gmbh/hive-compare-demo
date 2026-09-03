from decimal import ROUND_HALF_UP, Decimal

VAT_RATE = Decimal("0.19")


def line_total(line):
    net = Decimal(line["quantity"]) * Decimal(str(line["unit_price"]))
    return float((net * (1 + VAT_RATE)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
