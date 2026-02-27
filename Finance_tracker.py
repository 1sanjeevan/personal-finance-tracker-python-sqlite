# importing sqlite3 to use database here
import sqlite3

# connect to the database
conn = sqlite3.connect("finance.db")

# creating cursor
cursor = conn.cursor()

# creating table to store income & expense
cursor.execute("""
CREATE TABLE IF NOT EXISTS money(
type TEXT,
amount INTEGER
)
""")

# menu here
print("1. Add Income")
print("2. Add Expense")
print("3. Show Balance")

# for the user choice
choice = input("Enter choice: ")


# option 1  to add income
if choice == "1":

    # take income amount
    amt = int(input("Enter income: "))

    # insert into database
    cursor.execute("INSERT INTO money VALUES('income',?)", (amt,))

    # save
    conn.commit()

    print(" Income Added")


# option 2 to add expense
elif choice == "2":

    # take expense amount
    amt = int(input("Enter expense: "))

    # insert into database
    cursor.execute("INSERT INTO money VALUES('expense',?)", (amt,))

    conn.commit()

    print(" Expense Added")


# option 3 to show balance
elif choice == "3":

    # get total income
    cursor.execute("SELECT SUM(amount) FROM money WHERE type='income'")
    income = cursor.fetchone()[0]

    # get total expense
    cursor.execute("SELECT SUM(amount) FROM money WHERE type='expense'")
    expense = cursor.fetchone()[0]

    # if no income so make it 0
    if income is None:
        income = 0

    # if no expense so make it 0
    if expense is None:
        expense = 0

    # show balance
    print("Balance =", income - expense)

# close connection
conn.close()