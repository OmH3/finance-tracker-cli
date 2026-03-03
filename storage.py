import json

def save_to_file(transactions: list[dict], filename="transactions.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(transactions, f, indent=4)
        print(f"Transactions saved to '{filename}'")
    except IOError as e:
        print(e)
    except TypeError as e:
        print(e)

def load_from_file(filename='transactions.json')->list[dict]:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"Transactions loaded from '{filename}'")
        return data
    except FileNotFoundError as e:
        print(e)
        return []
    except json.JSONDecodeError as e:
        print(e)
        return []