# Add the DEPENDENCIES
    # Add the Pandas dependency (library)
import pandas as pd 
    # Add Indirect Path to file (not needed in Direct Path)
import os


# DIRECT PATH - csv files to load from Resources Folder 
# school_data_to_load = "Resources/schools_complete.csv"
# student_data_to_load = "Resources/students_complete.csv"



# INDIRECT PATH - csv files to load from Resources Folder
school_data_to_load = os.path.join("Resources" , "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")


# READ SCHOOL DATA
    #read the school data file and store it in a Pandas Data Frame
school_data_df = pd.read_csv(school_data_to_load)
    #print entire DataFrame
school_data_df


#PRINT HEAD of CSV  
    #print HEAD of dataframe (default is top 5 rows unless you enter amount in () parentheses)
school_data_df.head()


#PRINT TAIL of CSV
    #print TAIL of dataframe (default is last 5 rows unless you enter amount in () parentheses)
school_data_df.tail(10)


#READ THE STUDENT DATA FILE
    #read the student data file and store it in the Pandas DataFrame
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


#FIND MISSING VALUES
    #the COUNT() Method - count number of rows
     #determine if there are any missing values in the school data using count() method
school_data_df.count()


#FIND MISSING VALUES
    #the COUNT() Method - count number of rows
     #determine if there are any missing values in the student data using Count() method
student_data_df.count()


#FIND MISSING VALUES
    #the ISNULL() Method - used to determine empty rows
     #determine if there are any missing values in the school data using isnull() method
school_data_df.isnull()


#FIND MISSING VALUES
    #the ISNULL() Method - used to determine empty rows
     #determine if there are any missing values in the student data using isnull() method
student_data_df.isnull()



#FIND MISSING VALUES
    #the NOTNULL() Method - used return the opposite Boolen value
     #determine if there are any missing values in the school data using notnull() method 
school_data_df.notnull()


#FIND MISSING VALUES
    #the NOTNULL() Method - used return the opposite Boolen value
     #determine if there are any missing values in the student data using notnull() method and sum () method to determine if any row is true
student_data_df.notnull().sum()


# DETERMINE DATA TYPES (All Columns)
    #detemine datatypes fo the school data frame = dytype(s) for all columns
school_data_df.dtypes


# DETERMINE DATA TYPES (Single Columns)
    #detemine datatypes fo the school data frame = dytype(s) for single columens
        # if column name has NO spaces in the title
school_data_df.budget.dtype
        # if column name has spaces in the title use [""]
school_data_df["budget"].dtype        


# DETERMINE DATA TYPES (All Columns)
    #detemine datatypes fo the STUDENT data frame = dytype(s) for all columns
student_data_df.dtypes    


# add each prefix and suffix to remove to a list
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD", "PhD", "MD", "DDS"]


# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word, "")
student_data_df.head(10)    


#MERGE DATA FRAMES
    # you must have column that matches to merge a data frames (ours is school_name)
        #combine the data into a single data set
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head(10)


# GET THE NUMBER OF STUDENTS (ALL COLUMNS) = COUNT() method
    # get the total number of students using count() method
student_count =  school_data_complete_df.count()
student_count


# GET THE NUMBER OF STUDENTS (SINGLE COLUMN) = COUNT() method
    # get the total number of students using count() method
student_count =  school_data_complete_df["Student ID"].count()
student_count


# GET THE NUMBER OF SCHOOLS (Unmerged DataFrame) = COUNT() method
    # calcutate the total number of schools
school_count = school_data_df["school_name"].count()
school_count


# UNIQUE() method (merged DataFrame)
    #  unique method will retrn a "ndarray", or n-dimensional array of all the unique values of that column 
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# GET THE NUMBER OF SCHOOLS (merged DataFrame) = UNIQUE() method
    # calcutate the total number of schools using unique() method
school_count_2 = len(school_data_complete_df["school_name"].unique())
school_count_2


# GET TOTAL BUDGET & SUM() METHOD [unmerged DataFrame]
    #calculate the total budget using sum() method
total_budget = school_data_df["budget"].sum()
total_budget



# GET THE SCORE AVERAGES: MEAM() method [READING SCORE]
    # calculate the average reading score using mean method
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# GET THE SCORE AVERAGES: MEAM() method [MATH SCORE]
    # calculate the average math score using mean method
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


#DETERMINE PASSING GRADE
    #assign variables
passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70



#DETERMINE PASSING GRADE (TEST EXAMPLE)
passing_math = school_data_complete_df["math_score"] >= 70
passing_math.head(10)
    # returns Boolean values



# FILTER STUDENTS WHO PASSED MATH 
    # get all the students who are passing math in a new DataFrame 
        #placing DataFrame inside [] brakets returns filtered DataFrame
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# FILTER STUDENTS WHO PASSED READING 
    # get all the students who are passing reading in a new DataFrame 
        #placing DataFrame inside [] brakets returns filtered DataFrame
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_reading.head()


# GET THE NUMBER OF STUDENTS WHO PASSED MATH & READING
    # since we are calculating a percentage, we need to conver the student count to a number with a decimal, or folating-point decimal, by using float()
    # Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

    # Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()

print(passing_math_count)
print(passing_reading_count)


# GET THE PERCENTAGE OF Students who passed MATH AND READING
    # Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100
    # Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100

print(passing_math_percentage)
print(passing_reading_percentage)


#CALCULATE THE OVERALL PASSING PERCENTAGE ["&" LOGICAL OPERATOR]
    # calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
passing_math_reading.head()


# CALCULATE THE NUMBER OF STUDENTS WHO PASSED BOTH MATH & READING
passing_math_reading["student_name"].count()
# or
passing_math_reading.student_name.count()



# CALCULATE THE NUMBER OF STUDENTS WHO PASSED BOTH MATH & READING
    # Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count


# CALCULATE THE OVERALL PASSING PERCENTAGE

    # calculate the overall passing percentage
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


#CREATE A DISTRICT SUMMARY DATA FRAME
    #adding a list of values with keys to create a new DataFrame by creating a list of dictionaryies
district_summary_df = pd.DataFrame(
     [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


#CREATE A FUNCTION 
#define a function that calculates tHE percentage of students that passed both math and readin and print the passing precentages to the output when the function is called
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100.0


#CREATE A FUNCTION
passing_math_count = 29370
total_student_count = 39170

#call the function
passing_math_percent(passing_math_count, total_student_count)


#CHAINING THE MAP() & FORMAT FUNCTIONS
    # Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
district_summary_df["Total Students"]


#CHAINING THE MAP() & FORMAT FUNCTIONS
    # Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
district_summary_df["Total Budget"] 



#CHAINING THE MAP() & FORMAT FUNCTIONS
   # Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

district_summary_df


#REORDER COLUMNS
# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


#SET THE INDEX TO THE SCHOOL NAME
    #determine the school type
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_types
    # this codes uses set_index this return a Series with the index


# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(per_school_types)
df


#GET THE STUDENT COUNT PER SCHOOL (SCHOOL_DATA)
    #Calculate the total student count.
        #returns a single series with preset indext
per_school_counts = school_data_df["size"]
per_school_counts


#GET THE STUDENT COUNT PER SCHOOL (SCHOOL_DATA)
    #Calculate the total student count.(parentses) sets index name and [brackets] set the column
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# VALUE_COUNTS METHOND - GET THE STUDENT COUNT PER SCHOOL (SCHOOL_DATA_COMPLETE_DF) 
    # value_counts() returns a sercies of data with the number of times data appears (does not show repeating values)
    # Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts



#GET THE BUDGET PER STUDENT (school_data)
    # create series for calculation
    # Calculate the total school budget.
per_school_budget = school_data_df.set_index(['school_name'])['budget']
per_school_budget


#GET THE BUDGET PER STUDENT (school_data)
    # Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita
    # We can perform this calculation because the per_school_budget and per_school_counts are Series, both data types are int64, and both have the same index.


#GET THE SCORES AVERAGES PER SCHOOL
    # Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]
student_school_math


#GROUPBY() METHOD - GET THE SCORES AVERAGES PER SCHOOL
    # groupby() function will  split an object(like DataFrame), apply a mathematical operation, and combine the results. This can be used to group large amounts of data when we want to compute 
    # mathematical operations on the groups
        # Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(['school_name']).mean()
per_school_averages


#GROUPBY() METHOD - GET THE SCORES AVERAGES PER SCHOOL
   # Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(['school_name']).mean()['reading_score']
#view one of them
per_school_math


#GET THE PASSING PERCENTAGE PER SCHOOL
#pseudocode
 # To get the passing percentages, we need to:
 # 1. Determine what is the passing grade.
 # 2. Get the number of students who passed math and reading.
 # 3. Get the students who passed math and passed reading


#GET THE PASSING PERCENTAGE PER SCHOOL
    # Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
#view one of them
per_school_passing_math.head()


#GET THE PASSING PERCENTAGE PER SCHOOL
    # Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
# view one of them
per_school_passing_math


#GET THE PASSING PERCENTAGE PER SCHOOL - COMBINED - (&) OPERATOR
    # Calculate the students who passed both math AND reading.
        #create data frame
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
per_passing_math_reading.head()


#GET THE PASSING PERCENTAGE PER SCHOOL
    #index as school_name, and then we need to get the number of students
per_passing_math_reading = per_passing_math_reading.groupby(['school_name']).count()['student_name']    


#GET THE PASSING PERCENTAGE PER SCHOOL
    # Calculate the overall passing percentage.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100  
per_overall_passing_percentage


#CREATE THE SCHOOL SUMMMARY DATA FRAME
    #To create per_school_summary_df, the column names will be the keys, and the values will be each piece of data we retrieved or calculated.
    # Adding a list of values with keys to create a new DataFrame.
per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()


#CLEAN UP THE DATA FRAME - FORMAT
    # Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Display the data frame
per_school_summary_df.head()


#CLEAN UP THE DATA FRAME 
# Reorder the columns in the order you want them to appear.
new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]
# Assign district summary df the new column order.
per_school_summary_df = per_school_summary_df[new_column_order]
per_school_summary_df.head()


