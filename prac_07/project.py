class Project:
    def __init__(self, name='', date='', priority='', cost=0.0, percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __str__(self):
        return f'{self.name}\t{self.date}\t{self.priority}\t{self.cost}\t{self.percentage}'
