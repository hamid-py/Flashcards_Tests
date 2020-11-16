class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, time):
        return cls(*time.split(':'))


a = Time.from_string('14:10')
print(a.__dict__)