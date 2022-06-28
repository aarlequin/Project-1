#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#CW1 Software Development_BMI Calculator by Andrea Arlequin _ ARL2152503 
                #Date of last update: 15/06/2022


#Welcome the user to the BMI Calculator and ask them to enter their preferred measuring units. Create a variable using the unit that is entered here. It should be “metric” or imperial”.  
units= str(input("Welcome to the NHC BMI Calulator. What measuring units would you like to use to calculate your BMI today? Metric or imperial?:  ").lower()) 


#Create two different sets of codes depending on the user’s choice of units.  

#If the user has chosen to use metric units. Ask the user to enter their measurements using metric units. Their weight should be entered in kilograms and their height entered in metres. 
if units=="metric": 

        weight_kg= float(input("Enter your weight in kilograms:  "  )) 
        height_m=  float(input("Enter your height in metres:  "   )) 

#Write the mathematical code for calculating the user’s BMI with metric units.  Create the variable “BMI” to capture this calculation.     
        bmi = round(weight_kg / height_m ** 2,2) 
    
#If the user has chosen to use imperial units for measure their BMI. Ask the user to enter their measurements using imperial units. Their weight should be measured in pounds and their height and inches.        
if units=="imperial":

        weight_lb = float(input("Enter your weight in pounds:   " ))  
        height_inches = float(input("Enter your height in inches:  "))

#Write the mathematical code for calculating the user’s BMI with imperial units. Create the variable “BMI” to capture this calculation. 
        bmi = round(weight_lb / height_inches ** 2*703,2)

#Create branching statements to print the user’s results for both metric and imperial data inputs using data captured from the two different “BMI” calculations.   
#The user receives their BMI results based on the World Health Organisation's health standards.  
#Write if the BMI is smaller than 18.5 print the corresponding WHO category the user falls into.
if bmi < 18.5:
    print(f"Your BMI is {bmi}. Your results suggest that you are underweight and they also indicate malnutrition.")
#Write if something else and the BMI is less than 25 print the corresponding WHO category the user falls into.     
elif bmi< 25:
    print(f"Your BMI is {bmi}. Congratulations, you have a normal body weight.")
#Write if something else and the BMI is greater than or equal to 25 print the corresponding WHO category the user falls into.     
elif bmi>= 25:
    print(f"Your BMI is {bmi}. Your results suggest that you are overweight.") 
#Write if something else and the BMI is greater than or equal to 30 print the corresponding WHO category the user falls into.     
elif bmi>= 30:
    print(f"Your BMI is {bmi}.  Your results suggest that you are obese.") 

