class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def is_empty(self):
        return self.head is None

    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def peek(self):
        if self.data:
            return self.data[-1]
        return None

    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        return self.data


class BankAccount:
    def __init__(self, account_number, username, balance=0):
        self.account_number = account_number
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"{self.username} - Balance: {self.balance}"


accounts = MyLinkedList()
transaction_history = Stack()
bill_queue = Queue()
account_requests = Queue()
next_id = 1


def generate_id():
    global next_id
    acc_id = f"ACC{next_id:04d}"
    next_id += 1
    return acc_id


def find_account(username):
    for acc in accounts.to_list():
        if acc.username.lower() == username.lower():
            return acc
    return None


def add_account(username, balance=0):
    if find_account(username):
        print("Account already exists")
        return
    acc = BankAccount(generate_id(), username, balance)
    accounts.add(acc)
    print("Account added successfully")


def display_accounts():
    if accounts.is_empty():
        print("No accounts")
        return
    print("Accounts List:")
    for i, acc in enumerate(accounts.to_list(), 1):
        print(f"{i}. {acc}")


def deposit(username, amount):
    acc = find_account(username)
    if not acc:
        print("Account not found")
        return
    acc.balance += amount
    transaction_history.push(f"Deposit {amount} to {username}")
    print("New balance:", acc.balance)


def withdraw(username, amount):
    acc = find_account(username)
    if not acc:
        print("Account not found")
        return
    if acc.balance < amount:
        print("Insufficient funds")
        return
    acc.balance -= amount
    transaction_history.push(f"Withdraw {amount} from {username}")
    print("New balance:", acc.balance)


def show_last_transaction():
    if not transaction_history.is_empty():
        print("Last transaction:", transaction_history.peek())
    else:
        print("No transactions")


def undo_transaction():
    if not transaction_history.is_empty():
        print("Undo ", transaction_history.pop())
    else:
        print("Nothing to undo")



def add_bill():
    bill = input("Enter bill: ")
    bill_queue.enqueue(bill)
    print("Added:", bill)


def process_bill():
    if not bill_queue.is_empty():
        print("Processing:", bill_queue.dequeue())
    else:
        print("No bills")


def show_bills():
    print("Queue:", bill_queue.display())


def request_account():
    username = input("Enter username: ")
    account_requests.enqueue(username)
    print("Request submitted")


def process_request():
    if not account_requests.is_empty():
        username = account_requests.dequeue()
        add_account(username)
    else:
        print("No requests")


def show_requests():
    print("Requests:", account_requests.display())



def show_array():
    arr = [
        BankAccount("ACC0001", "Ali", 150000),
        BankAccount("ACC0002", "Sara", 220000)
    ]
    print("Array accounts:")
    for acc in arr:
        print(acc)



def bank_menu():
    while True:
        print("\n1.Request 2.Deposit 3.Withdraw 4.Show 5.Back")
        c = input("Choice: ")

        if c == "1":
            request_account()
        elif c == "2":
            deposit(input("Username: "), int(input("Amount: ")))
        elif c == "3":
            withdraw(input("Username: "), int(input("Amount: ")))
        elif c == "4":
            display_accounts()
        elif c == "5":
            break


def atm_menu():
    while True:
        print("\n1.Balance 2.Withdraw 3.Back")
        c = input("Choice: ")

        if c == "1":
            acc = find_account(input("Username: "))
            print(acc.balance if acc else "Not found")
        elif c == "2":
            withdraw(input("Username: "), int(input("Amount: ")))
        elif c == "3":
            break


def admin_menu():
    while True:
        print("\n1.View req 2.Process req 3.Add bill 4.Process bill 5.View bills 6.History 7.Undo 8.Back")
        c = input("Choice: ")

        if c == "1":
            show_requests()
        elif c == "2":
            process_request()
        elif c == "3":
            add_bill()
        elif c == "4":
            process_bill()
        elif c == "5":
            show_bills()
        elif c == "6":
            print(transaction_history.data)
        elif c == "7":
            undo_transaction()
        elif c == "8":
            break


def main():
    show_array()

    accounts.add(BankAccount("ACC0001", "Ali", 150000))
    accounts.add(BankAccount("ACC0002", "Sara", 220000))

    global next_id
    next_id = 3

    while True:
        print("\n1.Bank 2.ATM 3.Admin 4.Exit")
        c = input("Choice: ")

        if c == "1":
            bank_menu()
        elif c == "2":
            atm_menu()
        elif c == "3":
            admin_menu()
        elif c == "4":
            break


if __name__ == "__main__":
    main()