# this file for validation and helpers
from datetime import datetime
from typing import Generator

def get_valid_float(prompt)->float:
    """returns float value of the amount if the value could be 
    converted to float

    Args:
        prompt (string): just a normal prompt asking user to enter
        amount

    Returns:
        float: float value of the amount if possible else value error
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid value....")


def get_valid_date(prompt: str) -> datetime:
    """takes a string date time value and returns it as a
    datetime object

    Args:
        prompt (str): prompt for the user -> ex-enter the date

    Returns:
        datetime: datetime object of the format YYYY-mm-dd
    """
    while True:
        try:
            value: str = input(prompt)
            dt = datetime.strptime(value, "%Y-%m-%d")
            return dt
        except ValueError:
            print("INVALID DATE FORMAT.")

def get_valid_type(prompt)->str:
    while True:
        val = input(prompt).lower().strip()
        if val == "income" or val=="expense":
            return val
            break
        else:
            print("Enter either 'expense' or 'income'")

def build_transaction(amount, type_, category, date, note)->dict:
    return {
        "amount": amount,
        "type": type_,
        "category": category,
        "date": date.strftime("%Y-%m-%d"),
        "note": note
    }

def large_expenses(transactions, threshold)->Generator[dict, None, None]:
    for transaction in transactions:
        if transaction.get("type")=="expense" and transaction.get("amount")>threshold:
                yield transaction

def display_transactions(transactions) -> None:
    if not transactions:
        print("No transactions found.")
        return
    filtered_amount: list = list(map(lambda t: f"${t['amount']:.2f}", transactions))
    for index, (transaction,amount) in enumerate(zip(transactions, filtered_amount), 1):
        print(
            f"{index} "
            f"{transaction['type']} "
            f"{transaction['category']} "
            f"{amount} "
            f"{transaction['date']} "
            f"{transaction.get('note', '-')}"
        )

    