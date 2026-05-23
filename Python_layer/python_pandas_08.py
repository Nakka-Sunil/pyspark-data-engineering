# Tasks

# Fill missing salaries with department average salary
# Create salary category:
# High > 75000
# Medium 50000–75000
# Low < 50000
# Rank employees within each department by salary
# Find employees earning above department average
# Calculate cumulative department salary
# Find department-wise:
# avg salary
# max salary
# employee count

# Answer

import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'emp_id': [1,2,3,4,5,6,7],
    'name': ['A','B','C','D','E','F','G'],
    'dept': ['IT','HR','IT','Finance','HR','IT','Finance'],
    'salary': [50000,60000,np.nan,90000,75000,80000,65000],
    'experience': [2,5,3,8,6,4,7]
})

employees['salary'] = employees['salary'].fillna(
    employees.groupby('dept')['salary'].transform('mean')
)

def salary_category(x):
    if x > 75000:
        return 'High'
    elif x >= 50000:
        return 'Medium'
    else:
        return 'Low'

employees['salary_category'] = employees['salary'].apply(salary_category)

employees['rank'] = (
    employees
    .groupby('dept')['salary']
    .rank(method='dense', ascending=False)
)

dept_avg = employees.groupby('dept')['salary'].transform('mean')

above_avg = employees[
    employees['salary'] > dept_avg
]

employees = employees.sort_values(['dept','salary'])

employees['cumulative_salary'] = (
    employees
    .groupby('dept')['salary']
    .cumsum()
)

dept_summary = (
    employees
    .groupby('dept')
    .agg(
        avg_salary=('salary','mean'),
        max_salary=('salary','max'),
        employee_count=('emp_id','count')
    )
    .reset_index()
)

print(employees)
print(above_avg)
print(dept_summary)

print('\n')
print('*'*50)

# Tasks
# Convert sale_date to datetime
# Fill missing amounts using product average
# Create month and year columns
# Find city-wise revenue
# Find product-wise revenue
# Find top-selling product in each city
# Rank products by revenue within each city
# Calculate rolling average of amount (window size = 2)
# Find cumulative city revenue ordered by date
# Sort by:
# city ascending
# amount descending

# Answer

import pandas as pd
import numpy as np

sales = pd.DataFrame({
    'sale_id': [101,102,103,104,105,106,107,108],
    'city': ['Bangalore','Hyderabad','Bangalore','Mumbai',
             'Hyderabad','Mumbai','Bangalore','Mumbai'],
    'product': ['Laptop','Phone','Tablet','Laptop',
                'Tablet','Phone','Laptop','Tablet'],
    'amount': [80000,30000,np.nan,95000,25000,20000,85000,40000],
    'sale_date': [
        '2025-01-10',
        '2025-01-15',
        '2025-02-01',
        '2025-02-10',
        '2025-03-05',
        '2025-03-12',
        '2025-04-01',
        '2025-04-10'
    ]
})

sales['sale_date'] = pd.to_datetime(sales['sale_date'])

sales['amount'] = sales['amount'].fillna(
    sales.groupby('product')['amount'].transform('mean')
)

sales['month'] = sales['sale_date'].dt.month
sales['year'] = sales['sale_date'].dt.year

sales['city_revenue'] = (
    sales.groupby('city')['amount']
    .transform('sum')
)

sales['product_revenue'] = (
    sales.groupby('product')['amount']
    .transform('sum')
)

city_product = (
    sales
    .groupby(['city','product'])['amount']
    .sum()
    .reset_index()
)

city_product['rank'] = (
    city_product
    .groupby('city')['amount']
    .rank(method='dense', ascending=False)
)

top_products = city_product[
    city_product['rank'] == 1
]

sales = sales.sort_values('sale_date')

sales['rolling_avg'] = (
    sales['amount']
    .rolling(2)
    .mean()
)

sales['cumulative_city_revenue'] = (
    sales
    .groupby('city')['amount']
    .cumsum()
)

sales = sales.sort_values(
    ['city','amount'],
    ascending=[True,False]
)

print(sales)
print(city_product)
print(top_products)

print('\n')
print('*'*50)