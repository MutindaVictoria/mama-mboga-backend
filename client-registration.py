class Client:
  
    def __init__(self, name,phone_number,email,password,home_address):
        self.name = name
        self.phone_number=phone_number
        self.email=email
        self.password=password
        self.home_address=home_address
    def sign_up():   
        name = input("Enter your name:")
        phone_number = input("Enter your phone_number:")
        email = input("Enter your email:")
        password = input("Enter your password:")
        home_adress = input("Enter your home_address")
        client=Client(name,phone_number,email,password,home_address)
        return client
    def log_in(clients):
        email = input("Enter your email:")
        password = input("Enter your password:")
        for client in clients:
            if client.email==email and client.password==password:
                print("logging was successful")
                return True
            else:
                print("logging was unsuccessful")
                return False