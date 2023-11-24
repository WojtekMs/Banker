from banker.data.transaction import Transaction

def main():
    print("Hello world from Banker!")
    t = Transaction(_date="July", _value=50, _description="Descr")
    print(t)