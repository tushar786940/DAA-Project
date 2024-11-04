class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight

def fractional_knapsack(capacity,items):
    #To sort the item on profit and weight ratio.
    items.sort(key = lambda x: x.profit/x.weight, reverse = True)

    total_profit = 0
    for item in items:
        if capacity > 0 and item.weight <= capacity:

            #To take the whole item.
            capacity = capacity - item.weight
            total_profit = total_profit + item.profit
        else:

            #To only take the fraction of whole item.
            total_profit = total_profit + capacity*(item.profit/item.weight)
            capacity = 0
            break #Here, the knapsack is full.
    
    return total_profit

if __name__=="__main__":
    items = [Item(40,10),Item(100,25),Item(120,50)] #To call the the class.
    capacity = 50
    max_value = fractional_knapsack(capacity,items)
    print(f"Maximum profit in the knapsack: {max_value}")