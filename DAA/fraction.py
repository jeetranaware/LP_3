def fractional_knapsack(capacity, values, weights):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0 
    
    for value, weight in items:
        if capacity <= 0: 
            break
        
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break  

    return total_value

values = [25, 24 , 15]  
weights = [18, 15, 10]    
capacity = 20           

max_value = fractional_knapsack(capacity, values, weights)
print("Maximum value in Knapsack =", max_value)
