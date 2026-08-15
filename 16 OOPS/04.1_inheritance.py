# Gate smashers

class OTTsub:
    def __init__(self, sub_id, plan, total_payment):
        self.sub_id = sub_id
        self.plan = plan
        self.total_payment = total_payment
    
    def sub_status(self):
        print(f"the subscriber {self.sub_id}, has a plan {self.plan} monthly plan and the payment is of {self.total_payment}")

    def unsub_status(self):
        print(f"the subscriber {self.sub_id}, has a plan {self.plan} monthly plan and the payment is of {self.total_payment}")

s1 = OTTsub(121212, 1, 800)
print(s1.total_payment)
print(s1.plan)
print(s1.sub_id)
s1.sub_status()
# class premium(OTTsub):
#     def __init__ (self, sub_id, plan, total_payment, screens):
#         super().__init__( sub_id, plan, total_payment)
#         max_screens = screens

#         def max_screens(self, screens):
#             print(f"the max screens are {max_screens} and have premium plan")

# s2 = premium(111112, 5, 1000, 5)
# s2.max_screens(4)

