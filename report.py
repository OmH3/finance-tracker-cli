import datetime
from utils import large_expenses

def total_balance(transactions: list[dict], index=0)->float:
    """returns the total balance after evaluating from all the transactions.
       uses a recursive approach to add amount if type is income and deduct if
       type is expense.
    Args:
        transactions (list[dict]): list of dictionaries of transaction data
        index (int, optional): each index of transactions list

    Returns:
        total balance after recursively calling the function
    """
    if not transactions:
        return 0
    if index==len(transactions):
        return 0
    
    if transactions[index].get("type","").lower()=="expense":
        return total_balance(transactions, index+1) - transactions[index].get("amount",0)
    elif transactions[index].get("type","").lower() == "income":
        return total_balance(transactions, index + 1) + transactions[index].get("amount", 0)
    else:
        raise ValueError(f"Unknown transaction type")
    
def summary_report(transactions:list[dict])->None:
    """returns the total balance after evaluating from all the transactions.
       uses a recursive approach to add amount if type is income and deduct if
       type is expense.
    Args:
        transactions (list[dict]): list of dictionaries of transaction data
        index (int, optional): each index of transactions list

    Returns:
        total balance after recursively calling the function
    """
    if not transactions:
        print("No transactions found.")
        return
    
    expenses = list(filter(lambda x: x.get("type")=="expense", transactions))
    income = list(filter(lambda x: x.get("type")=="income", transactions))

    income_total:float=0
    # total income - loop + accumulation
    for i in income:
        income_total+=i.get("amount",0)

    # total expenses — loop + accumulation
    total_expense:float=0
    for e in expenses:
        total_expense+=e.get("amount",0)

    # net balance — calls recursive function
    net_balance:float=total_balance(transactions)

    # category-wise totals — dictionary accumulator
    category_totals: dict={}

    for transaction in transactions:
        category = transaction.get("category","uncategorized")
        amount = transaction.get("amount",0)
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount

    # highest single expense — comprehension
    highest_expense = max([t["amount"] for t in transactions if t.get("type")=="expense"],default=0)

    # display
    print("\n" + "=" * 40)
    print("         SUMMARY REPORT")
    print("=" * 40)
    print(f"  Total Income:    £{income_total:.2f}")
    print(f"  Total Expenses:  £{total_expense:.2f}")
    print(f"  Net Balance:     £{net_balance:.2f}")
    print(f"  Highest Expense: £{highest_expense:.2f}")
    print("\n  Category Totals:")
    print("  " + "-" * 30)
    for category, total in category_totals.items():
        print(f"  {category:<20} £{total:.2f}")
    print("=" * 40)


def filter_by_category(transactions:list[dict], category:str)->list[dict]:
    """filters transactions based on given category

    Args:
        transactions (list[dict]): list of dictionaries
        category (str): category to match

    Returns:
        list[dict]: sub transactions with category equal to the category parameter
    """
    if not transactions:
        print("provide a valid transaction")
        return []
    
    filter_by_category_transaction = [t for t in transactions if t.get("category").lower()==category.lower()]
    # filter_by_category_transaction = list(filter(lambda x: x.get("category")==category, transactions))

    if not filter_by_category_transaction:
        print(f"No transactions found for category '{category}'")

    return filter_by_category_transaction

def filter_by_date_range(transactions:list[dict], start:str, end:str)->list[dict]:
    """filters transactions between start and end date inclusive

    Args:
        transactions (list[dict]): list of transaction dictionaries
        start (str): start date in YYYY-MM-DD format
        end (str): end date in YYYY-MM-DD format

    Returns:
        list[dict]: transactions within the date range
    """
    if not transactions:
        print("No transactions found.")
        return []
    
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()

    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return []
    
    if start_date > end_date:
        print("Start date cannot be after end date.")
        return []
    
    filtered = [t for t in transactions if start_date<=datetime.strptime(t.get("date",""), "%Y-%m-%d").date()<=end_date]

    if not filtered:
        print(f"No transactions found between {start} and {end}.")
    
    return filtered

def filter_above_amount(transactions:list[dict], threshold:float)->list[dict]:
    """filters expenses above a given threshold using large_expenses generator

    Args:
        transactions (list[dict]): list of transaction dictionaries
        threshold (float): minimum amount to filter by

    Returns:
        list[dict]: expense transactions above the threshold
    """
    if not transactions:
        print("No transactions found.")
        return []
    
    filtered = list(large_expenses(transactions, threshold))
    if not filtered:
        print(f"No expenses found above £{threshold:.2f}.")
    
    return filtered

def display_date_amount_summary(transactions:list[dict])->None:
    """displays a compact summary pairing dates with amounts using zip()

    Args:
        transactions (list[dict]): list of transaction dictionaries
    """
    if not transactions:
        print("No transactions found.")
        return
    
    # dono ko list bnake zip wise traverse krdenge
    dates = [t.get("date","N/A") for t in transactions]
    amounts=[f"${t.get("amount",0):.2f}" for t in transactions]

    for date, amount in zip(dates, amounts):
        print(f"  {date:<15} {amount}")