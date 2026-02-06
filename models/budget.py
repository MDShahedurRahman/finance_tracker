class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    def to_dict(self):
        return {
            "category": self.category,
            "limit": self.limit
        }

    @staticmethod
    def from_dict(data):
        return Budget(data["category"], data["limit"])
