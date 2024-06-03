# Import pandas
import pandas as pd

# Read Salaries.csv as a dataframe called sal
df = pd.read_csv('Salaries.csv')

# Check the head of the DataFrame
print("Head of the DataFrame:")
print(df.head())

# Use the .info() method to find out how many entries there are
print("\nInfo about the DataFrame:")
df.info()

# What is the average BasePay?
average_base_pay = df['BasePay'].mean()
print("\nAverage BasePay:", average_base_pay)

# What is the highest amount of OvertimePay in the dataset?
highest_overtime_pay = df['OvertimePay'].max()
print("\nHighest OvertimePay:", highest_overtime_pay)

# What is the job title of JOSEPH DRISCOLL?
joseph_driscoll_job_title = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print("\nJob title of JOSEPH DRISCOLL:", joseph_driscoll_job_title.values)

# How much does JOSEPH DRISCOLL make (including benefits)?
joseph_driscoll_total_pay_benefits = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print("\nTotal Pay Benefits of JOSEPH DRISCOLL:", joseph_driscoll_total_pay_benefits.values)

# What is the name of highest paid person (including benefits)?
highest_paid_idx = df['TotalPayBenefits'].idxmax()
highest_paid_person = df.loc[highest_paid_idx]
print("\nHighest paid person (including benefits):\n", highest_paid_person)

# What is the name of lowest paid person (including benefits)?
lowest_paid_idx = df['TotalPayBenefits'].idxmin()
lowest_paid_person = df.loc[lowest_paid_idx]
print("\nLowest paid person (including benefits):\n", lowest_paid_person)

# What was the average (mean) BasePay of all employees per year? (2011-2014)
average_base_pay_per_year = df.groupby('Year')['BasePay'].mean()
print("\nAverage BasePay per year (2011-2014):\n", average_base_pay_per_year)

# How many unique job titles are there?
unique_job_titles = df['JobTitle'].nunique()
print("\nNumber of unique job titles:", unique_job_titles)

# What are the top 5 most common jobs?
top_5_common_jobs = df['JobTitle'].value_counts().head(5)
print("\nTop 5 most common jobs:\n", top_5_common_jobs)

# How many Job Titles were represented by only one person in 2013?
job_titles_2013 = df[df['Year'] == 2013]['JobTitle'].value_counts()
one_person_jobs_2013 = job_titles_2013[job_titles_2013 == 1].count()
print("\nJob Titles represented by only one person in 2013:", one_person_jobs_2013)

# How many people have the word Chief in their job title?
chief_count = df['JobTitle'].str.contains('Chief', case=False).sum()
print("\nNumber of people with 'Chief' in their job title:", chief_count)

# Bonus: Is there a correlation between length of the Job Title string and Salary?
df['title_len'] = df['JobTitle'].apply(len)
correlation = df['TotalPayBenefits'].corr(df['title_len'])
print("\nCorrelation between job title length and total pay benefits:", correlation)

# Great Job!
