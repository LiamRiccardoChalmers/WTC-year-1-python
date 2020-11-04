print("[Module] Journal loaded.")

def receive_income(amount):
    print(f"[Journal] Received R{amount}.00")


def pay_expense(amount):
    print(f"[Journal] Paid R{amount}.00")

if __name__ == "__main__":
    receive_income(amount)
    pay_expense(amount)