result = []

def divider(a, b):
    if a < b:
        raise ValueError(f"Значення 'a' ({a}) менше ніж 'b' ({b})")
    if b > 100:
        raise IndexError(f"Значення 'b' ({b}) більше ніж 100")
    return a / b

data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Помилка при обробці пари ({key}, {data[key]}): {e}")

print(result)

