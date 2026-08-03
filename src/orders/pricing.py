VAT_RATE = 0.19


def line_total(line):
    net = line["quantity"] * line["unit_price"]
    return round(net * (1 + VAT_RATE), 2)
