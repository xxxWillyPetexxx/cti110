miles_per_gallon = float(input()) #input for car miles per gallon
cost_per_gallon = float(input()) #input for cost of gas per gallon

cost_per_mile = cost_per_gallon / miles_per_gallon #miles per gallon = car mpg divided by cost of gas per gallon
trip_cost1 = cost_per_mile * 20 # trip cost1 = total cost per mile multiplied by 20 miles
trip_cost2 = cost_per_mile * 75 # trip cost2 = total cost per mile multiplied by 75 miles
trip_cost3 = cost_per_mile * 500 # trip cost3 = total cost per mile multiplied by 200 miles

print(f'{trip_cost1:.2f} {trip_cost2:.2f} {trip_cost3:.2f}')
