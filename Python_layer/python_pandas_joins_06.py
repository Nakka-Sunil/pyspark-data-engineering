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

df_sal_by_dept = pd.merge(employees, departments, on ='dept_id', how='inner')
print(
    df_sal_by_dept.groupby('dept_name', as_index=False)['salary'].sum()
)