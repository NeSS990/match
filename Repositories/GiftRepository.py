class GiftRepository:
    def __init__(self):
        self.gifts = []

    def save_gift(self, gift):
        self.gifts.append(gift)

    def find_gift_by_id(self, gift_id):
        for gift in self.gifts:
            if gift.gift_id == gift_id:
                return gift
        return None
