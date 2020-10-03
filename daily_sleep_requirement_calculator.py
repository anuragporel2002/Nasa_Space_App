#Daily Sleep Requirement Calculator based User Input Parameters
#-------------------Constants (Age vs. Sleep Hour)-------------------
global sleep_hour
sleep_hour={'newborn':15,
            'infants':13.5,
            'toddler':12,
            'pre-school':12,
            'elementary-age':10.5,
            'teens':9,
            'adults':7.5}

#-------------------Functions---------------------------------------
def sleep_requirement(age):
    if age==1:
#-------------------Newborns----------------------------------------
        required_hour=sleep_hour['newborn']
    elif age==2:
#-------------------Infants-----------------------------------------
        required_hour=sleep_hour['infants']
    elif age==3:
#-------------------Toddler-----------------------------------------
        required_hour=sleep_hour['toddler']
    elif age==4:
#-------------------Pre-School--------------------------------------
        required_hour=sleep_hour['pre-school']
    elif age==5:
#-------------------Elementary-Age----------------------------------
        required_hour=sleep_hour['elementary-age']
    elif age==6:
#-------------------Teens-------------------------------------------
        required_hour=sleep_hour['teens']
    elif age==7:
#-------------------Adults-----------------------------
        required_hour=sleep_hour['adults']
    sleep_cycle=required_hour/1.5
    return required_hour,sleep_cycle

#-------------------Running the Code--------------------------------
if __name__=="__main__":
#-------------------Parameter Input from User-----------------------
    print("Press 1 if age is between 0-3 months")
    print("Press 2 if age is between 4-12 months")
    print("Press 3 if age is between 1-2 year")
    print("Press 4 if age is between 3-5 year")
    print("Press 5 if age is between 6-12 year")
    print("Press 6 if age is between 13-18 year")
    print("Press 7 if age is greater than 18 year")
    age=int(input("Enter your choice: "))

#-------------------Function Calling & Output Formatting------------
    outputs=sleep_requirement(age)
    required_hour=outputs[0]
    sleep_cycle=int(outputs[1])
#-------------------Print Result----------------------------------
    print()
    print("Your Daily Required Sleep Hour: ",required_hour)
    print("Number of Sleep Cycles (90 mins/cycle): ",sleep_cycle)