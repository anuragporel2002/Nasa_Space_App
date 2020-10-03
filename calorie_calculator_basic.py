# Daily Calorie Need Calculator based on Harris-Benedict Equation
#-------------------Constants (Activity Index)--------------------
global activity_factor
activity_factor={'Sedentary':1.2,
                'Lightly_Active':1.375,
                'Moderately_Active':1.55,
                'Very_Avtive':1.725,
                'Extra_Active':1.9}

#-------------------Functions--------------------------------------
def BMR_male(system,weight,height,age):
    if system=='Metric':
        bmr_value=66.5+(13.75*weight)+(5.003*height)-(6.755*age)
    elif system=='Imperial':
        bmr_value=66+(6.2*weight)+(12.7*height)-(6.76*age)
    return bmr_value

def BMR_female(system,weight,height,age):
    if system=='Metric':
        bmr_value=655.1+(9.563*weight)+(1.85*height)-(4.676*age)
    elif system=='Imperial':
        bmr_value=655.1+(4.35*weight)+(4.7*height)-(4.7*age)
    return bmr_value

def calorie_calculator(system,weight,height,age,activity_status,sex):
    if sex=='M':
        bmr_value=BMR_male(system,weight,height,age)
    elif sex=='F':
        bmr_value=BMR_female(system,weight,height,age)
    
    if activity_status==1:
        calorie_required=bmr_value*activity_factor['Sedentary']
    elif activity_status==2:
        calorie_required=bmr_value*activity_factor['Lightly_Active']
    elif activity_status==3:
        calorie_required=bmr_value*activity_factor['Moderately_Active']
    elif activity_status==4:
        calorie_required=bmr_value*activity_factor['Very_Active']
    elif activity_status==5:
        calorie_required=bmr_value*activity_factor['Extra_Active']
    
    return calorie_required

#-------------------Running the Code------------------------------
if __name__=="__main__":
#-------------------Parameter Input from User---------------------
    system=str(input("Select A System (Metric or Imperial): "))
    weight=float(input("Enter your weight (in kgs for Metric System and lbs for Imperial System): "))
    height=float(input("Enter your height (in cms for Metric System and inches for Imperial System): "))
    age=int(input("Enter your age in years: "))
    sex=str(input("Enter your sex (M or F): "))
    print()
    print("Press 1 for Sedentary")
    print("Press 2 for Lightly Active")
    print("Press 3 for Moderately Active")
    print("Press 4 for Very Active")
    print("Press 5 for Extra Active")
    activity_status=int(input("Select your Activity Status: "))

#-------------------Function Calling & Output Formatting----------
    calorie_required=calorie_calculator(system,weight,height,age,activity_status,sex)
    calorie_required=round(calorie_required)

#-------------------Print Result----------------------------------
    print()
    print("Your Daily Calorie Requirement is ",calorie_required)



