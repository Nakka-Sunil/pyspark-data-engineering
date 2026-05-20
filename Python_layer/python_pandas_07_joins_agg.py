import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'emp_id': [1,2,3,4,5,6,7,8],
    'name': ['A','B','C','D','E','F','G','H'],
    'dept_id': [101,101,102,102,103,103,101,np.nan],
    'salary': [50000,70000,60000,np.nan,90000,40000,75000,65000],
    'experience': [2,5,3,4,10,1,6,2]
})

departments = pd.DataFrame({
    'dept_id': [101,102,103],
    'dept_name': ['IT','HR','Finance']
})


# Q1 Merge both tables
df_merged = pd.merge(employees,departments)
print(df_merged)
print('**'*40)
print('\n')

# Q2 Replace missing salaries with department average salary
df_merged_mean = df_merged.groupby('dept_id')['salary'].mean() 
df_merged['salary'] = df_merged['salary'].fillna(
                    df_merged['dept_id'].map(df_merged_mean)    
)

print(df_merged)
print('**'*40)
print('\n')

df_merged['salary'] = df_merged.groupby('dept_id')['salary'].transform(
                        lambda x: x.fillna(x.mean())
)
print(df_merged)
print('**'*40)
print('\n')


# Q3 Find top-paid employee in each department
df_top_emp = df_merged.groupby('dept_id')['salary'].rank(method='dense', ascending=False)
print(df_merged.where(df_top_emp == 1))
print('**'*40)
print('\n')

# Q4 Create salary bands:
#  Low < 60000
#  Medium 60000–80000
#  High > 80000
def salary_band(sal):
    if sal < 60000:
        return 'Low'
    elif sal > 80000:
        return "High"
    else:
        return 'Medium'
    
df_merged['salary_band'] = df_merged['salary'].apply(lambda x: salary_band(x))
print(df_merged)
print('**'*40)
print('\n')

# Q5 Find employees earning above department average
avg_sal = df_merged.groupby('dept_id')['salary'].transform('mean')

print(df_merged.where(df_merged['salary'] > avg_sal))
print('**'*40)
print('\n')

# Q6 Rank employees within each department by salary
# Q7 Find department-wise:
# Q avg salary
# Q max salary
# Q employee count
# Q8 Find departments where avg salary > 65000
# Q9 Handle missing department IDs properly
# Q10 Output final cleaned DataFrame sorted by salary descending