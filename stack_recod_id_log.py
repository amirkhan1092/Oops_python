# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#
# 1.record(order_id): adds the order_id to the log
# 2.get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.


# You should be as efficient with time and space as possible.

class E_commerce:
    def __init__(self):
        self.order = list()

    def record(self,item_id):
        self.order.append(item_id)
    def get_last(self,i):
        if len(self.order)>i:
            return self.order[i]
        else:
            return None
    def __str__(self):
        return str(self.order)

customer = E_commerce()

customer.record('12sdd334232')
customer.record('330334232')
customer.record('00202d334232')
customer.record('12sdd33433322')

print(customer.get_last(3))
print(customer)





