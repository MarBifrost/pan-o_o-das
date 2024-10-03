import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'student_scores_random_names.csv')
grades = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']

# gets data of Students with grades less than 50
cln_data = data.dropna(how='all')
low_grades = (cln_data[grades].fillna(int(0)) < 50).all(axis=1).round(2)
students_with_low_grades = cln_data[low_grades]
print(
    f"სტუდენტები, რომელთა ქულაც ნაკლებია 50-ზე:\n {students_with_low_grades}")


# gets the grades for each sbuject in each semester
semester_means = data.groupby('Semester')[grades].mean().round(2)
print(
    f"თთოეული საგნისთვის თითოეულ სემესტრში საშუალო ქულაა: \n{semester_means}")


# the student with most mean of grades
students_mean = data.groupby(['Student'])[grades].mean().round(2)
overall_mean = students_mean.mean(axis=1).round(2)
max_mean = overall_mean.max()
students_with_max_mean = ''.join(overall_mean[overall_mean == max_mean].index)
print(
    f"სტუდენტი ყველაზე მაღალი საშუალო ქულით არის: {students_with_max_mean}, {max_mean}  საშუალო ქულით\n")

# The hardest subject per semester with the lowest grades' mean
hardest_subject = semester_means.idxmin(axis=1)
min_means = semester_means.min(axis=1)
hardest_subject_per_semester = pd.DataFrame({
    'Subject': hardest_subject,
    'Mean': min_means
})
print(
    "სემესტრების მიხედვით ყველაზე რთული საგნებია:\n",
    hardest_subject_per_semester)


# create new dataframe with the mean of subject's grades per semester
semester_list = [
    'Semester 1',
    'Semester 2',
    'Semester 3',
    'Semester 4',
    'Semester 5',
    'Semester 6',
    'Semester 7',
    'Semester 8']
new_dataframe = pd.DataFrame(data.groupby('Semester')[grades].mean().round(2))
new_dataframe.to_excel('semester_means.xlsx', index=True)
print("ახალი დატაფრეიმი:\n", new_dataframe)

# visually shows the grade of each subject per semester
semester_means.plot(
    kind='bar',
    title="Main grade of each subject per semester")
plt.savefig('semester_means.png', format='png')
plt.show()

# visually shows mean of grades fo each semester
overall_mean_per_semester = data.groupby(
    'Semester')[grades].mean().mean(axis=1).round(2)
overall_mean_per_semester.plot(kind='line',
                               title="Mean of total grade for each semester")
plt.savefig('overall_mean_per_semester.png', format='png')
plt.show()
