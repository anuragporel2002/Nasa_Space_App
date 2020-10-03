#Nutrient Breaker and Diet Suggester
#-------------------Constants (Cal/gm)------------------------------
global nutrient_value
nutrient_value={'Carbohydrate':4,
                'Protein':4,
                'Fat':9}

#-------------------Functions---------------------------------------
def nutrient_breaker(program,daily_calorie_need):
    if program==1:
#-------------------Mussle Gain Program-----------------------------
#-------------------Calorie Breakdown Nutrients-wise----------------
        carbohydrate=(daily_calorie_need*60)/100
        protein=(daily_calorie_need*35)/100
        fat=daily_calorie_need-carbohydrate-protein
#-------------------Breakdown in gms--------------------------------
        carb_gm=round(carbohydrate/4)
        prot_gm=round(protein/4)
        fat_gm=round(fat/9)
#-------------------Set Program Name--------------------------------
        target='Mussle Gain Program'
    elif program==2:
#-------------------Maintain Weight Program-------------------------
#-------------------Calorie Breakdown Nutrients-wise----------------
        carbohydrate=(daily_calorie_need*50)/100
        protein=(daily_calorie_need*25)/100
        fat=daily_calorie_need-carbohydrate-protein
#-------------------Breakdown in gms--------------------------------
        carb_gm=round(carbohydrate/4)
        prot_gm=round(protein/4)
        fat_gm=round(fat/9)
#-------------------Set Program Name--------------------------------
        target='Maintain Weight Program'
    elif program==3:
#-------------------Weight Lose Program-----------------------------
#-------------------Calorie Breakdown Nutrients-wise----------------
        carbohydrate=(daily_calorie_need*10)/100
        protein=(daily_calorie_need*50)/100
        fat=daily_calorie_need-carbohydrate-protein
#-------------------Breakdown in gms--------------------------------
        carb_gm=round(carbohydrate/4)
        prot_gm=round(protein/4)
        fat_gm=round(fat/9)
#-------------------Set Program Name--------------------------------
        target='Loose Fat Program'
#-------------------Final Report Printing---------------------------
    print()
    print("-----------------Your Personalised Diet Breakdown Chart-----------------")
    print()
    print("Your Selected Program: ",target)
    print("Your Daily Calorie Need: ",daily_calorie_need)
    print()
    print("Adjust the Amount of Carbohydrate as per the Quantity Prescribed Below")
    print("Carbohydrates: ",carb_gm,'gm')
    print("Protein: ",prot_gm,'gm')
    print("Fat: ",fat_gm,'gm')
    return

#-------------------Running the Code--------------------------------
if __name__=="__main__":
#-------------------Parameter Input from User-----------------------
    print("Press 1 for Mussle Gain Program")
    print("Press 2 for Maintain Weight Program")
    print("Press 3 for Lose Fat Program")
    program=int(input("Select a Program: "))
    daily_calorie_need=int(input("Enter the amount of calorie needed everyday: "))
#-------------------Function Calling--------------------------------
    nutrient_breaker(program,daily_calorie_need)

