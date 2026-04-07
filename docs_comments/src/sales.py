# TODO refactor this module using buisness logic names

def _parse_record(line: str):
    """Parse data from one sale record

    Parameters:
        line : record on one sale that come from file

    Return:
        Data on one sale in from dict or None if validation fails.
    
    """




    fields = line.strip().split(",")
    if len(fields) != 4:
        return None

    product, category, unit_price, quantity = fields

    try:
        unit_price = float(unit_price)
    except ValueError:
        return None

    try:
        quantity = int(quantity)
    except ValueError:
        return None

    return {
        "product": product,
        "category": category,
        "unit_price": unit_price,
        "quantity": quantity
    }


def read_sales_data(path):
    """Parse data from one sale record

    Parameters:
        line : record on one sale that come from file

    Return:
        Data on one sale in from dict or None if validation fails.
    
    """
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            record = _parse_record(line)
            if record is not None:
                records.append(record)
    return records


def calculate_total(records, discount=0):
    total = 0
    for record in records:
        total = total + record["unit_price"] * record["quantity"]
    if discount:
        total = total - total * discount / 100
    return total


def find_above_threshold(records, threshold):
    result = []
    for record in records:
        amount = record["unit_price"] * record["quantity"]
        if amount >= threshold:
            result.append(record)
    return result


def group_by_category(records):
    category_totals = {}
    for record in records:
        category = record["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += record["unit_price"] * record["quantity"]
    return category_totals


def build_report(records):
    lines = []
    lines.append("Report")
    lines.append("------")
    for category, amount in group_by_category(records).items():
        lines.append(f"{category}: {amount}")
    lines.append("------")
    lines.append(f"Total: {calculate_total(records)}")
    return "\n".join(lines)


def write_report(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)