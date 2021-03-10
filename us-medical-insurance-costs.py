#!/usr/bin/env python
# coding: utf-8

# # United States Medical Insurance Costs
# 
# In this project, a file with medical insurance costs will be investigated using Python fundamentals. The goal with this project will be to analyze various attributes within insurance.csv to learn more about the patient information in the file and gain insight into potential use cases for the dataset.

# In[17]:


# import CSV Library 
import csv 


# To begin, we will need all necessaries libraries to be imported. For this project, the only library that is required would be the `csv` library. In this project, we will be working with the **insurance.csv** data. Let's begin!
# 

# It is important to look through the **insurance.csv** file so that we know the data that we are working with. The following aspects of the file will be checked in order to plan out how to import the data in **insurance.csv** into a Python file.
# 
# * The names of columns and rows
# * To check if there are any missing data
# * Types of values (numerical or categorical)

# In[31]:


# Create empty lists for various attributes in insurance.csv
ages = []
sexes = []
bmi = []
children = []
smoker = []
region = []
charges = []
patient_info = []


# **insurance.csv** contains the following columns:
# * Patient's age
# * Patient's sex
# * Patient's BMI
# * Patient's number of children
# * Patient's smoking status
# * Patient's U.S geographical location
# * Patient's yearly medical insurance cost
# 
# Thankfully, there are no signs of missing data. To store this information, seven empty lists have been created to store the individual column data from **insurance.csv**.

# In[58]:


# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as insurance_info:
        # read the data from the csv file
        insurance_dict = csv.DictReader(insurance_info)
        # loop through the data in each row of the csv 
        for row in insurance_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst  


# The helper function above was created to make loading data into the lists as efficient as possible. Without this function, one would have to open **insurance.csv** and rewrite the `for` loop seven times; however, with this function, one can simply call `load_list_data()` each time as shown below.
# 
# For the **insurance.csv** file, we will need to use the pathname for the data to appear, hence, we will input ``/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv`` as instead of **insurance.csv**.

# In[60]:


# look at the data in insurance_csv_dict
load_list_data(ages, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'age')
load_list_data(sexes, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'sex')
load_list_data(bmi, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'bmi')
load_list_data(children, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'children')
load_list_data(smoker, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'smoker')
load_list_data(region, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'region')
load_list_data(charges, "/Users/bryanng77/Downloads/Insurance CSV folder/insurance.csv", 'charges')


# Now that all the data from **insurance.csv** neatly organized into labeled lists, we can finally begin our analysis! **YAY!!** This is where one must plan out what to investigate and how to perform the analysis. There are many aspects of the data that could be looked into. The following operations will be implemented:
# * Find average age of the patients
# * Return the number of males vs. females counted in the dataset
# * Find geographical location of the patients
# * Return the average yearly medical charges of the patients
# * Creating a dictionary that contains all patient information
# 
# To perform these inspections, I will build a class called `PatientsInfo`  which will contains fives methods:
# * `average_age()`
# * `analyze_sexes()`
# * `unique_regions()`
# * `average_charges()`
# * `create_dictionary()`
# 
# In order to do this, we will try to work our way around it using ``class`` and ``functions``.
# 
#         

# In[84]:


# initiate "Class"
class PatientsInfo:
    # init method that will take in each list parameter
    def __init__(self, ages, sexes, bmi, children, smoker, region, charges):
        self.ages = ages
        self.sexes = sexes
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges
    
    # Now, let us solve the first question, which is the fund out the average age of patients
    def average_age(self):
        # initialize total age at zero
        total_age = 0
        # interate through all the ages in the ages list
        for age in self.ages:
            # sim of the total age
            total_age += int(age)
        # return total age divided by the total number of patients 
        return ("Average Patient's Age: " + str(round(total_age/len(self.ages))) + " years")
    
    # Let us move on the the second question, which is to calculate the number of males and females in this dataset
    def analyze_sexes(self):
        males = 0
        females = 0
        for sex in self.sexes:
            # use "if" to add to male variable
            if sex == "male":
                males += 1
            # use "else" to add to the female variable
            elif sex == "female":
                females += 1
        # we will now print out both variables to get our results!
        print("Number of male patients: " + str(males))
        print("Number of female patients: " + str(females))
    
    # We will now move on to the third question, which is to find out each unique region the patients are from
    def unique_regions(self):
        # create an empty list
        unique_regions = []
        # iterate through each region in the region list
        for region in self.region:
            # if the region is not in the unique regions list, we will add it to the list :)
            if region not in unique_regions:
                unique_regions.append(region)
        # return unique_regions list
        return unique_regions
    
    # Last but not least, we will find out the average yearly medical charges for the patients in insurance.csv
    def average_charges(self):
        # initialize total charges at zero
        total_charges = 0
        # Let's iterate through charges in patients charges list and add each charge to total_charge
        for charge in self.charges:
            total_charges += float(charge)
        # return the average charges rounded to two decimal places
        return ("Average Yearly Medical Insurance Charges: " + str(round(total_charges/len(self.charges), 2)))
    
    
    # To conclude this section, we will use a method to create a dictionary with all the patient's information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["ages"] = [int(age) for age in self.ages]
        self.patients_dictionary["sexes"] = self.sexes
        self.patients_dictionary["bmi"] = self.bmi
        self.patients_dictionary["children"] = self.children
        self.patients_dictionary["smoker"] = self.smoker
        self.patients_dictionary["regions"] = self.region
        self.patients_dictionary["charges"] = self.charges
        return self.patients_dictionary


# The next step is to create an instance of the class called `patient_info`. With this instance, each method can be used to see the results of the analysis.

# In[78]:


patient_info = PatientsInfo(ages, sexes, bmi, children, smoker, region, charges)


# In[79]:


patient_info.average_age()


# The average age of the patients in **insurance.csv** is about 39 years old. This is important to check in order to ensure the data in **insurance.csv** is representative for a broader population. If it is decided to use the dataset to make inferences about other populations, the data must abundant and broad enough for such use cases.

# In[80]:


patient_info.analyze_sexes()


# The next step of the analysis is to check the balance of males vs. females in **insurance.csv**. Similar to above, it is important to check that this dataset is representative of a broader population of individuals. If a person were to use this dataset to create a classification model, it is important to make sure that the attributes are balanced.

# In[85]:


patient_info.unique_regions()


# There are four unique geographical regions in this dataset, and it is important to note that all the patients come from the United States.

# In[86]:


patient_info.average_charges()


# The average yearly medical insurance charge per individual is 13270 USD. Some further analysis could be done to see what patient attributes contribute most strongly to low and/or high medical insurance charges. For example, one could check if patient age correlates with the amount of money they spend yearly.

# In[87]:


patient_info.create_dictionary()


# All patient data is now neatly organized in a dictionary. This is convenient for further analysis if a decision is made to continue making investigations for the attributes in **insurance.csv**.
