class User:
    def _init_(self, username, email):
        self.username = username
        self.email = email
        self.credit_cards = []
        self.devices = []
        self.points = 0

    def add_credit_card(self, card_info):
        self.credit_cards.append(card_info)

    def add_device(self, device):
        self.devices.append(device)

    def purchase_app(self, app):
        pass

    def accumulate_points(self, amount):
        self.points += amount

    def redeem_points(self, points):
        pass

class CreditCard:
    def _init_(self, brand, card_number, expiration, cvv):
        self.brand = brand
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv

class Device:
    def _init_(self, device_id):
        self.device_id = device_id

user1 = User("user123", "user123@example.com")
card1 = CreditCard("Visa", "1234 5678 9012 3456", "12/24", "123")
user1.add_credit_card(card1)
device1 = Device("device1")
user1.add_device(device1)

user1.purchase_app("App1")
user1.accumulate_points(100)

user1.redeem_points(50)