# Student Grades Analysis

This project analyzes student grades across different subjects and semesters using a dataset of student scores. 


## Installation

To run this project, you need Python and the following libraries installed:

- pandas==2.2.3
- matplotlib==3.9.2
- openpyxl==3.1.5

You can install the required libraries using pip:

```pip install pandas matplotlib ```

## Usage

- Download the dataset student_scores_random_names.csv and place it in the project directory.
- Run the script to perform the analysis and generate visualizations.

```python3 main.py```

## Data Description
The dataset student_scores_random_names.csv should contain the following columns:

- Student: Name of the student
- Semester: Semester numbers
- Math: Math scores
- Physics: Physics scores
- Chemistry: Chemistry scores
- Biology: Biology scores
- English: English scores


## Analysis
The script performs the following analyses:

- Students with Low Grades: Identifies students who scored less than 50 in all subjects.
- Mean Grades per Semester: Calculates the average score for each subject across all semesters.
- Top Student: Finds the student with the highest average score.
- Hardest Subject per Semester: Identifies the hardest subject for each semester based on the lowest mean grades.
- Mean Grades DataFrame: Creates a new DataFrame containing the mean grades for each subject per semester and exports it to an Excel file.

## Visualization
The script generates the following visualizations:

- Bar Chart of Mean Grades per Subject: Displays the average score of each subject across semesters.
- Line Chart of Overall Mean Grades per Semester: Illustrates the trend of overall average grades for each semester.
- Visualizations are saved as PNG files:
    - semester_means.png
    - overall_mean_per_semester.png


## Output Files
- semester_means.xlsx: Excel file containing the mean grades for each subject per semester.
- semester_means.png: Bar chart of mean grades per subject.
- overall_mean_per_semester.png: Line chart of overall mean grades per semester.
