import pandas as pd
import numpy as np

# =========================
# Employees
# =========================

employees = pd.DataFrame({
    'emp_id': [101,102,103,104,105,106,107,108],
    'emp_name': ['Sunil','Rahul','Anu','Kiran','Meena','Arjun','Pooja','David'],
    'dept_id': [1,2,1,3,2,4,1,None],
    'salary': [70000,80000,75000,65000,90000,72000,68000,60000],
    'manager_id': [201,202,201,203,202,204,201,None],
    'join_date': [
        '2023-01-15',
        '2022-07-10',
        '2023-05-01',
        '2021-03-20',
        '2020-11-11',
        '2024-01-01',
        '2022-09-09',
        '2023-12-12'
    ]
})

employees['join_date'] = pd.to_datetime(employees['join_date'])

# =========================
# Departments
# =========================

departments = pd.DataFrame({
    'dept_id': [1,2,3,5],
    'dept_name': ['Engineering','HR','Finance','Marketing'],
    'location': ['Bangalore','Hyderabad','Chennai','Mumbai']
})

# =========================
# Projects
# =========================

projects = pd.DataFrame({
    'project_id': [1001,1002,1003,1004,1005],
    'emp_id': [101,102,101,105,109],
    'project_name': ['AI','Migration','Analytics','Security','Cloud'],
    'hours_logged': [120,80,100,140,60]
})

# =========================
# Monthly Sales
# =========================

sales = pd.DataFrame({
    'sale_id': [1,2,3,4,5,6,7,8,9,10],
    'emp_id': [101,101,102,103,104,105,106,107,101,103],
    'month': [
        'Jan','Feb','Jan','Jan','Feb',
        'Mar','Jan','Feb','Mar','Mar'
    ],
    'sales_amount': [
        5000,7000,4000,6500,3000,
        9000,4500,8000,7500,6200
    ]
})

# Q1 — Employee + Department Join

# Show:
# emp_name
# dept_name
# location
# salary
# Requirements:
# keep all employees
# employees without departments should also appear

df_emp_dept = pd.merge(employees, departments, on='dept_id', how='left')
print(df_emp_dept[['emp_name','dept_name', 'location', 'salary']])
print('*'*80)
print('\n')

# Q2 — Missing Department Validation

# Find employees whose department does not exist.
# Expected:
# dept_id = 4
# NULL dept_id rows

print(df_emp_dept.query('dept_name.isna()'))
print('*'*80)
print('\n')

# Q3 — Total Salary by Department

# Calculate:
# total salary
# average salary

df_all_departments = pd.merge(employees, departments, on='dept_id', how='left')
(
    df_emp_dept
    .groupby('dept_name')
    .agg(
        total_salary=('salary','sum'),
        avg_salary=('salary','mean')
    )
    .sort_values('total_salary', ascending=False)
)
print('*'*80)
print('\n')

# Q4 — Project Assignment Validation
# Find:
# projects assigned to employees NOT present in employee table.

df_proj_assigned = pd.merge(employees, projects, on='emp_id', how='right')
print(df_proj_assigned)
print(df_proj_assigned.query('emp_name.isna()'))
print('*'*80)
print('\n')

# Q5 — Employees with Multiple Projects
# Find employees working on more than 1 project.
df_proj_assigned['count'] = df_proj_assigned.groupby('emp_id')['emp_id'].transform('count')
print(df_proj_assigned[df_proj_assigned['count'] > 1].drop_duplicates('emp_id')[['emp_id','count']])
print('*'*80)
print('\n')

emp_project_counts = df_proj_assigned.groupby('emp_id').size().reset_index(name='project_count')
print(emp_project_counts[emp_project_counts['project_count'] > 1])
print('*'*80)
print('\n')

# Q6 — Window Function Style Problem

# For each department:
# calculate employee salary rank.

df_all_departments['rank'] = df_all_departments.groupby('dept_id')['salary'].rank(method='dense', ascending=False)
print(df_all_departments.sort_values(['dept_id', 'rank']))
print('*'*80)
print('\n')

# Department Average Salary Comparison

# Add a new column:
# dept_avg_salary
# Then find employees earning ABOVE department average.

df_all_departments['dept_avg_salary'] = df_all_departments.groupby('dept_id')['salary'].transform('mean')
print(df_all_departments.query('salary > dept_avg_salary'))
print('*'*80)
print('\n')

df_merged = pd.merge(sales, df_all_departments, on='emp_id', how='inner')
df_merged['month'] = pd.to_datetime(df_merged['join_date']).dt.month
df_pivot = pd.pivot_table(
    data = df_merged,
    index = 'emp_id',
    columns= 'month',
    values = 'sales_amount',
    aggfunc='sum',
    fill_value=0
)
print(df_pivot)
print('*'*80)
print('\n')

# Q10 — Method Chaining Workflow

# Using employees dataframe:
# Build a chained workflow:
# remove null dept_id
# filter salary > 70000
# join departments
# calculate avg salary per department
# sort descending

df_employee_f = (employees.dropna(subset=['dept_id']).
                 query('salary > 70000')
                 .merge(departments, on='dept_id', how='inner')
                 .groupby('dept_id')['salary']
                 .mean()
                 .reset_index(name='avg_sal')
                 .sort_values('avg_sal', ascending=False))
print(df_employee_f)