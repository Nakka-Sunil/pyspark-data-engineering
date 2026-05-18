import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1,2,3,4,5],
    'name': ['Sunil','Rahul','Anu','Kiran','Meena'],
    'dept_id': [101,102,101,105,None],
    'salary': [50000,60000,55000,45000,70000]
})

departments = pd.DataFrame({
    'dept_id': [101,102,103],
    'dept_name': ['IT','HR','Finance']
})

orders = pd.DataFrame({
    'order_id': [1,2,3,4,5],
    'customer_id': [101,102,101,104,105],
    'amount': [500,700,300,900,1000]
})

customers = pd.DataFrame({
    'id': [101,102,103,104],
    'customer_name': ['A','B','C','D']
})

# Q1: inner join
df_employees = pd.merge(employees, departments, on = 'dept_id', how = 'inner')
print(df_employees[['emp_id','name','dept_name']])
print('\n')

# Q2: left join 
df_dept_not_exist = pd.merge(employees, departments, on= 'dept_id', how = 'left')
print(df_dept_not_exist[df_dept_not_exist['dept_name'].isnull()])
print('\n')

# Q3: Right Join 
df_emp_not_exist = pd.merge(employees, departments, on = 'dept_id', how = 'right')
print(df_emp_not_exist[df_emp_not_exist['emp_id'].isnull()])
print('\n')

# Q4: left_on, right_on
df_diff_join = pd.merge(orders, customers, left_on='customer_id', right_on='id', how= 'inner')
print(df_diff_join[['order_id','customer_name','amount']])
print('\n')

#Q5: merge with full join

df_full_join = pd.merge(orders, customers, left_on='customer_id',right_on='id', how='outer', indicator=True)
print(df_full_join)
print('\n')