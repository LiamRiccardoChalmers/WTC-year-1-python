print("[Module] Balance loaded")

def do_balance(amount):
    print(f"After checking your payments you owe Liam R{(amount*10-amount)}.00")

if __name__ == "__main__":
    do_balance()