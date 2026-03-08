from utils import get_valid_float, get_valid_type, get_valid_date, build_transaction, display_transactions
from storage import load_from_file, save_to_file
from report import summary_report, filter_by_date_range, filter_above_amount

def display_menu() -> None:
    print("\n" + "=" * 40)
    print("    PERSONAL FINANCE CLI TRACKER")
    print("=" * 40)
    print("  1. Add Transaction")
    print("  2. View All Transactions")
    print("  3. View Summary")
    print("  4. Filter by Category")
    print("  5. Filter by Date Range")
    print("  6. Filter Above Amount")
    print("  7. Save to File")
    print("  8. Load from File")
    print("  9. Exit")
    print("=" * 40)

def add_transaction(transactions: list[dict])->None:
    amount=get_valid_float("Enter amount: ")
    type_ = get_valid_type("Enter type (income/expense): ")
    category = input("Enter category (food, rent, salary etc): ").lower().strip()
    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    note = input("Enter note (optional, press Enter to skip): ").strip()
    transaction = build_transaction(amount, type_, category, date, note)
    transactions.append(transaction)

def main():
    print("Hello from finance-cli-tracker!")
    transactions: list[dict]=load_from_file()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-9): "))

            if choice == 1:
                add_transaction(transactions)

            elif choice == 2:
                print("\n--- All Transactions ---")
                display_transactions(transactions)

            elif choice == 3:
                summary_report(transactions)

            elif choice == 4:
                start = input("Enter start date (YYYY-MM-DD): ").strip()
                end = input("Enter end date (YYYY-MM-DD): ").strip()
                filtered = filter_by_date_range(transactions, start, end)
                display_transactions(filtered)
            
            elif choice == 5:
                start = input("Enter start date (YYYY-MM-DD): ").strip()
                end = input("Enter end date (YYYY-MM-DD): ").strip()
                filtered = filter_by_date_range(transactions, start, end)
                display_transactions(filtered)

            elif choice == 6:
                threshold = get_valid_float("Enter minimum amount: ")
                filtered = filter_above_amount(transactions, threshold)
                display_transactions(filtered)

            elif choice == 7:
                save_to_file(transactions)

            elif choice == 8:
                transactions = load_from_file()
            
            elif choice == 9:
                save = input("Save before exiting? (y/n): ").lower().strip()
                if save == "y":
                    save_to_file(transactions)
                print("Goodbye! 👋")
                break
            
            else:
                print("Please enter a number between 1 and 9.")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
