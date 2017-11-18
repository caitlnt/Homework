
# coding: utf-8

# In[57]:

#CTa-HW04-PyCitySchools


# In[58]:

#import libraries to use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[59]:

#read in files
school_data = pd.read_csv('Resources/schools_complete.csv')

student_data = pd.read_csv('Resources/students_complete.csv')


# In[60]:

#shows first 5 lines in school data
school_data.head()


# In[61]:

#shows first 5 lines in student data
student_data.head()


# In[62]:

#District Summary Calculations
school_total = len(school_data)
student_total = len(student_data)
budget_total = school_data['budget'].sum()
avgmath_score = student_data['math_score'].mean()
avgread_score = student_data['reading_score'].mean()

pass_math_count = student_data[student_data.math_score >=70]
pass_math_total = len(pass_math_count)
pass_math_percent =(pass_math_total / student_total)*100

pass_read_count = student_data[student_data.reading_score >=70]
pass_read_total = len(pass_read_count)
pass_read_percent =(pass_read_total / student_total)*100

overall_pass_rate= ((pass_read_percent + pass_math_percent)/2)


# In[63]:

#Display District Summary Calculations
print("Total_Schools = ", school_total)
print("Total_Students = ", student_total)
print("Total_Budget = ", budget_total)
print("Avg_Math_Score = ", avgmath_score)
print("Avg_Read_Score = ", avgread_score)
print("%_Pass_Math = ", pass_math_percent)
print("%_Pass_Read = ", pass_read_percent)
print("Overall_Pass_Rate = ", overall_pass_rate)


# In[64]:

#Convert district summary data into a dataframe (table)
district_summary = pd.DataFrame({'Total_Schools': [school_total],'Total_Students': [student_total], 
                                 'Total_Budget': [budget_total], 'Avg_Math_Score': [avgmath_score],
                                 'Avg_Read_Score': [avgread_score], '%_Pass_Math': [pass_math_percent], 
                                 '%_Pass_Read': [pass_read_percent], 'Overall_Pass_Rate': [overall_pass_rate]
                                })


# In[65]:

#Order district summary data into a specific order in the table and round data to 2 decimal places
district_summary = district_summary[['Total_Schools','Total_Students','Total_Budget', 'Avg_Math_Score', 
                                     'Avg_Read_Score', '%_Pass_Math', '%_Pass_Read', 'Overall_Pass_Rate']]

district_summary = district_summary.round(2)

district_summary = district_summary


# In[66]:

#Display completed District Summary table
district_summary_df = pd.DataFrame(district_summary)
district_summary_df


# In[67]:

#Plot the District Summary data on a bar graph
get_ipython().magic('matplotlib inline')
district_summary_df.plot(kind='barh')


# In[68]:

#Take out only fields in school data needed for School Summary
subset_school = school_data[['name','type','budget']]
subset_school.reset_index(inplace=True)
subset_school


# In[69]:

#Rename columns in school data from name to school to merge data later
subset_school_summary = subset_school.rename(columns={'name':'school_name', 'type':'school_type', 'budget':'school_budget'})
subset_school_summary


# In[70]:

#School Summary Calculations
sch_stu_total = student_data['school'].value_counts()
sch_per_budget = school_data.groupby('name').budget.sum()
sch_stu_avgmath = student_data.groupby('school').math_score.mean()
sch_stu_avgread = student_data.groupby('school').reading_score.mean()

sch_pass_math_count = student_data[student_data.math_score >=70]
sch_pass_math_total = sch_pass_math_count.groupby("school")['Student ID'].count()
sch_pass_math_percent =(sch_pass_math_total / sch_stu_total)*100

sch_pass_read_count = student_data[student_data.reading_score >=70]
sch_pass_read_total = sch_pass_read_count.groupby("school")['Student ID'].count()
sch_pass_read_percent =(sch_pass_read_total / sch_stu_total)*100

grp_overall_pass_rate= ((sch_pass_read_percent + sch_pass_math_percent)/2)


# In[71]:

#Display School Summary Calculations
print("Total_Students_By_School = ", sch_stu_total)
print("")
print("Total_Budget_By_School = ", sch_per_budget)
print("")
print("")
print("Avg_Math_Score_By_School = ", sch_stu_avgmath)
print("")
print("")
print("Avg_Read_Score_By_School = ", sch_stu_avgread)
print("")
print("")
print("%_Pass_Math_By_School = ", sch_pass_math_percent)
print("")
print("")
print("%_Pass_Read_By_School = ", sch_pass_read_percent)
print("")
print("")
print("Overall_Pass_Rate_By_School = ", grp_overall_pass_rate)
print("")
print("")


# In[72]:

#Create table for school summary and reset index for later use
school_summary = pd.concat([sch_stu_total, sch_per_budget,sch_stu_avgmath,
                            sch_stu_avgread,sch_pass_math_percent,sch_pass_read_percent, grp_overall_pass_rate], axis=1)

school_summary.reset_index(inplace=True)
school_summary


# In[73]:

#Rename column names
school_summary_final = school_summary.rename(columns={'index':'school_name', 'school':'total_students', 
                                                      'budget': 'school_budget', 'math_score': 'avg_math_score', 
                                                      'reading_score': 'avg_read_score', 0: '%_Pass_Math', 1:'%_Pass_Read', 
                                                      2:'Overall_Pass_Rate'})

school_summary_final


# In[74]:

#Combine subset school summary and school summary final into one table
merged_school_summary = pd.merge(subset_school_summary, school_summary_final, on="school_name")
merged_school_summary


# In[75]:

#Add total budget and rename columns
merged_school_summary['school_budget_x'] = budget_total

merged_school_summary = merged_school_summary.rename(columns={'school_name':'School_Name', 'school_type':'School_Type', 
                                                      'total_students': 'Total_Students', 'school_budget_x': 'Total_Budget', 
                                                      'school_budget_y':'School_Budget', 'math_score': 'Avg_Math_Score', 
                                                      'reading_score': 'Avg_Read_Score', '%_Pass_Math': '%_Pass_Math', 
                                                        '%_Pass_Read':'%_Pass_Read', 'Overall_Pass_Rate':'Overall_Pass_Rate'})

merged_school_summary


# In[76]:

#Plot the School Summary data on a bar graph
get_ipython().magic('matplotlib inline')
merged_school_summary.plot(kind='barh')


# In[77]:

#Top Performing Schools By Passing Rate
merged_school_summary.nlargest(5, 'Overall_Pass_Rate')


# In[78]:

#Plot Top Performing Schools By Passing Rate
get_ipython().magic('matplotlib inline')
merged_school_summary.nlargest(5, 'Overall_Pass_Rate').plot(kind='barh')


# In[79]:

#Bottom Performing Schools By Passing Rate
merged_school_summary.nsmallest(5, 'Overall_Pass_Rate')


# In[80]:

#Plot Bottom Performing Schools By Passing Rate
get_ipython().magic('matplotlib inline')
merged_school_summary.nsmallest(5, 'Overall_Pass_Rate').plot(kind='barh')


# In[81]:

#Math Scores by Grade
stu_grd_avgmath = student_data.groupby(['school', 'grade'])['math_score'].mean()
stu_grd_avgmath=pd.DataFrame(stu_grd_avgmath)
stu_grd_avgmath


# In[82]:

#Plot Math Scores by Grade
get_ipython().magic('matplotlib inline')
stu_grd_avgmath.plot(kind='barh')


# In[83]:

#Reading Scores by Grade
stu_grd_avgread = student_data.groupby(['school', 'grade'])['reading_score'].mean()
stu_grd_avgread = pd.DataFrame(stu_grd_avgread)
stu_grd_avgread


# In[84]:

#Plot Reading Scores by Grade
get_ipython().magic('matplotlib inline')
stu_grd_avgread.plot(kind='barh')


# In[85]:

#Scores By School Spending
merged_school_summary


# In[86]:

#Calculate Average Spending Ranges (per Student)
avgspend = (sch_per_budget/sch_stu_total)
avgspendbin = (sch_per_budget/sch_stu_total)


# In[87]:

#Create table, reset index, and rename columns
avg_spend_summary = pd.concat([avgspend, avgspendbin], axis=1)

avg_spend_summary.reset_index(inplace=True)

avg_spend_summary=avg_spend_summary.rename(columns={'index':'school_name', 0:'avg_spend', 1:'avg_spend_bin'})
avg_spend_summary


# In[88]:

#Create Bins to bucket average spending
bins = [500, 550, 600, 650, 700]
avg_spend_summary['avg_spend_bin'] = pd.cut(avg_spend_summary['avg_spend'], bins)
avg_spend_summary


# In[89]:

#Merge and average spending data together with summary data
merged_school_spending = pd.merge(subset_school_summary, avg_spend_summary, on="school_name")
merged_school_spending


# In[90]:

#Display Scores by School Spending in Bins
grp_merged_school_spending = merged_school_spending.groupby('avg_spend_bin').mean()
grp_merged_school_spending


# In[91]:

#Plot Scores by School Spending in Bins
get_ipython().magic('matplotlib inline')
grp_merged_school_spending.plot(kind='barh')


# In[92]:

#Take out only fields in school data needed for School Summary
subset_school_2 = school_data[['name','type','size']]
subset_school_2.reset_index(inplace=True)
subset_school_2 = subset_school_2.rename(columns={'name':'school_name', 'type':'type', 'size':'size'})
subset_school_2


# In[93]:

#Combine subset school 2 and merged school spending to create one table for school size
merged_school_size = pd.merge(subset_school_2, merged_school_spending, on="school_name")
merged_school_size


# In[94]:

#Create bins for school size
bins = [100, 1500, 2500, 5000]
group_names = ['Small', 'Medium', 'Large']
merged_school_size['avg_spend_bin'] = pd.cut(merged_school_size['size'], bins, labels=group_names)

merged_school_size = merged_school_size.rename(columns={'avg_spend_bin':'School_Size'})


# In[95]:

#Display Scores by School Size in Bins
grp_merged_school_size = merged_school_size.groupby('School_Size').mean()
grp_merged_school_size


# In[96]:

#Plot Scores by School Size in Bins
get_ipython().magic('matplotlib inline')
grp_merged_school_size.plot(kind='barh')


# In[97]:

#Group by School Type and display it
merged_school_type = merged_school_size.groupby('type').mean()
merged_school_type


# In[98]:

#Plot by School Type and display it
get_ipython().magic('matplotlib inline')
merged_school_type.plot(kind='barh')


# In[ ]:




# In[ ]:



