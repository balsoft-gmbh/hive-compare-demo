import csv
import io


def orders_to_csv(orders):
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["customer", "status", "lines"])
    for order in orders:
        writer.writerow([order["customer"], order["status"], len(order["lines"])])
    return out.getvalue()
