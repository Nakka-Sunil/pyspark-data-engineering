import pandas as pd
import numpy as np

df_emp = pd.DataFrame({
    'employee_id': [1,2,2,3,4,5,6,6],
    'department': ['IT','HR','HR',None,'Finance','IT','HR','HR'],
    'salary': [70000,80000,80000,np.nan,90000,75000,np.nan,np.nan],
    'city': ['Bangalore',None,None,'Mumbai','Delhi','Bangalore','Chennai','Chennai']
})

# print(df_emp)
# Q1: total missing values per column

print(df_emp.isnull().sum())

# Q2: missing department → "Unknown"

df_emp = df_emp.fillna(
    'unknown'
)
# print(df_emp)

# missing salary → average salary

salary_filled =pd.to_numeric(df_emp['salary'], errors = 'coerce')
# print(salary_filled)

df_emp['salary'] = salary_filled.fillna(
    salary_filled.mean()
)

print(df_emp)

# Q3: Find duplicate rows based on:
# employee_id + department
sub_set = ['employee_id', 'department']

duplicates = df_emp.duplicated(subset = sub_set)
print(df_emp[duplicates])


# Q4: Remove duplicates but:
# keep latest occurrence

df_emp.drop_duplicates(
    subset= 'employee_id',
    keep = 'last',
    inplace= True
)

print(df_emp)

# Q5: Remove rows where:
# salary is null
df_emp.dropna(
    subset= 'salary'
)

print(df_emp)


print('\n')
print('\n')
print('************************** SECTION 02 ****************************')
print('\n')
print('\n')
df_sales = pd.DataFrame({
    'region': ['South','South','North','North','East','East','West','West'],
    'salesperson': ['A','B','C','D','E','F','G','H'],
    'sales': [500,700,400,900,300,600,1000,1200],
    'orders': [5,7,4,8,3,5,10,11]
})

print(df_sales)
print('\n')
print('\n')

# Q1: total sales per region
total_sales_per_region = df_sales.groupby('region')['sales'].sum()
print(total_sales_per_region)
print('\n')

# Q2: Find:
#     min sales
#     max sales
#     avg sales

df_sales_summery = df_sales.groupby('region').agg(
    min_sales = ('sales','min'),
    max_sales = ('sales', 'max'),
    avg_sales = ('sales', 'mean')
)
print(df_sales_summery)
print('\n')

# Q3: Create new column:
# region_avg_sales

df_sales['region_avg_sales'] = df_sales.groupby('region')['sales'].transform('mean')
print(df_sales)
print('\n')

#Q4: Create new column:
# sales_diff_from_avg

df_sales['sales_diff_from_avg'] = (
                        df_sales['sales']
                        -
                        (df_sales.groupby('region')['sales'].transform('mean'))
)

print(df_sales)
print('\n')

# Q5: Find: sales contribution % by each sales person in each region

df_sales['sales_contribution'] = (
                                (df_sales['sales']
                                /
                                (df_sales.groupby('region')['sales'].transform('sum'))) * 100
)

print(df_sales)
print('\n')
print('************************** SECTION 03 ****************************')
print('\n')
print('\n')

df_orders = pd.DataFrame({
    'customer_id': [101,102,103,101,102,103,101,104],
    'category': ['Electronics','Electronics','Furniture','Furniture',
                 'Furniture','Electronics','Electronics','Furniture'],
    'amount': [1200,800,1500,700,2200,3000,1800,400],
    'quantity': [2,1,4,2,5,6,3,1]
})

print(df_orders)

# Q1: Create column:
# order_size

# amount < 1000 → Low
# 1000–2000 → Medium

# 2000 → High

def order_size(x):
    if x >= 2000:
        return 'High'
    elif x > 1000:
        return 'Medium'
    else:
        return 'Low'
    

df_orders['order_size'] = df_orders['amount'].apply(order_size)
print(df_orders)

# Q2: Create column:
# total_price_per_item

def price_per_item(row):
    return row['amount'] / row['quantity']
df_orders['total_price_per_qty'] = df_orders.apply(price_per_item, axis = 1)

print(df_orders)
print('\n')
#Q3:  Find:
# total sales per category AND customer
# groupby(['col1', 'col2'])

df_orders['sales_per_cat_cust'] = df_orders.groupby(['customer_id', 'category'])['customer_id'].transform('count')

print(df_orders)
print('\n')

# Q4: Find:
# total amount
# avg quantity         # per category
 
df_orders['total_amount'] = df_orders.groupby('category')['amount'].transform('sum')
df_orders['avg_qty'] = df_orders.groupby('category')['quantity'].transform('mean')

print(df_orders)
print('\n')
print('\n')
#Q5: Find highest order amount per category using:
# transform('max')
# and create:
# is_highest_order
# column:
# Yes
# No

df_orders['order_max'] = df_orders.groupby('category')['amount'].transform('max')
print(df_orders)
print('\n')
df_orders['is_highest_order'] = df_orders['order_max'] == df_orders['amount']
df_orders['is_highest_order'] = df_orders['is_highest_order'].map({True: 'Yes', False: 'NO'})

print(df_orders)