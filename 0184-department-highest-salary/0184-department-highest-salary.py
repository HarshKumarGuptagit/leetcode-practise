import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['sal_rnk']=employee.sort_values('salary',ascending=False).groupby('departmentId')['salary'].rank(method="dense",ascending=False)
    return employee[employee.sal_rnk==1].merge(department,left_on='departmentId',right_on="id",how="left",suffixes=["_emp","_dep"])[["name_dep","name_emp","salary"]].rename(columns={
      "name_dep":"Department" ,
      "name_emp":"Employee",
      "salary":"Salary"  
    })