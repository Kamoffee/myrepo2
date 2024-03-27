st_lev = int(input("Please enter initial stock level: "))
month_to_plan = int(input("Please enter the number of month to plan: "))

planned_sales_quantity = []
for i in range(month_to_plan):
    planned_sales = int(input(f"Please enter the planned sales quantity {i + 1}: "))
    planned_sales_quantity.append(planned_sales)

new_st_lev = st_lev
prod_qty = []
for i in range(month_to_plan):
    if planned_sales_quantity[i] <= new_st_lev:
        prod_qty.append(0)
    else:
        prod_qty.append(planned_sales_quantity[i] - new_st_lev)
    # ensure that new stock level is not negative
    new_st_lev = max(0, new_st_lev - planned_sales_quantity[i])

print()
print("The resulting production quantities are:")

for i, dmd in enumerate(prod_qty, start=1):
    print(f"Production quantity month {i} - {dmd} ")





