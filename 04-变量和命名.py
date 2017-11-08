cars = 100
space_in_car = 4.0

drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
avg_passengers_per_car = passengers / cars_driven

print("这有",cars,"辆车")
print("这只有",drivers,"个司机")
print("所以还剩下",cars_not_driven,"辆车没人开")
print("开走了",drivers,"辆车")
