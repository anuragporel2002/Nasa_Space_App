# Nasa_Space_App
# Sleep Shift Scheduling Tool

## Summary
Shift workers often don’t find an easy way to balance their sleep with the various activities they need to do. They often remain drowsy and cannot work properly. Our application aims to solve this major issue. The user would have to enter their shift timings and our specialized algorithm will suggest sleeping slots and the number of sleeping cycles. This will help the user’s body to rest properly and will help them balance their busy schedules. Also, depending on the user’s entered activity status and program, the daily calorie requirement and customized carbohydrate, protein and fat will be shown.

## Adressing the Challenge
We have developed a desktop application which works as a sleep scheduling tool and a diet planning tool which suggests required nutritional requirements.

It will prove to be very beneficial for the user as it will completely solve the problem of sleep deprivation which people generally face during their time in space. It has been challenging for them to manage their sleep well so our application we created gives a complete solution for this problem.

The application is designed to take certain inputs from the user and then it accordingly suggests the amount of sleep and nutrition required by the user. It is very efficient in terms of time and efforts.

It works according to the sleep scheduling algorithm, the user can choose their preferred time to sleep and accordingly the application manages your sleep schedule. It also provides the information of the user’s required nutrition intake.

We are hoping that our application solves all the issues workers face with sleep and nutrition. This surely will provide then better suggestion for the sleep schedule and their nutrition intake.

## Development Process
##### Inspiration
Our team comes from Development countries where this tool can support people to take better decisions and prevent the spread of sleep shifting challenges. Also we tried to put our expertise on for the human benefit. This can help them to reduce stress and fatigue problems.
##### Approach
Our software has basically two major parts. One is a sleep shift scheduler and another one is a Diet Nutrition Breaker.
So, we first divided our software into 4 basic algorithms. Those are:
- Sleep Requirement Calculator
- Customized sleep time scheduler
- Daily Calorie Requirement Calculator
- Nutrients Breaker

To calculate daily Sleep Requirement we have used the standard minimum sleeping time according to age group. Ref: https://whentosleep.com/
To develop the sleep scheduler we used the python datetime module and we designed our own algorithm.
To calculate the daily calorie requirement we have used the Harris-Benedict Equation which calculates the BMR of a person based on some parameters like age, sex, height, weight. Then the BMR is multiplied by the Activity Factor which is a standard dataset based on how active the person is. Ref:https://www.kaa-yaa.com/the-most-accurate-way-to-calculate-your-daily-calorie-needs-and-macronutrient-breakdown/ 
Based on the user's daily calorie requirement , the fourth algorithm informs the user how much grams of Carbohydrates, Protein or Fat should be taken.
Then we developed the GUI and linked all the algorithms in the backend.

## Tools & Technology
- Python as language
- Tkinter Module for GUI
- Python datetime module to schedule the sleep shifts
- fpdf module to save the report in pdf format
- pyinstaller to make the .exe file from .py file 

## Problems Faced
We faced some minor issues while developing an application regarding the problem statement. We first had to decide a UI module as multiple modules for UI designing are available in Python. We also managed to create an algorithm for sleep scheduling. Creating a calorie counter and data validation was also a minor hurdle but we, as a team, managed to overcome it, by referring several websites to check data authentication.

## Reference:
- https://2020.spaceappschallenge.org/challenges/
- https://www.sleepfoundation.org/shift-work-disorder/tips
- https://www.youtube.com/watchv=wH2hL5Ua_m8
- https://journals.sagepub.com/doi/full/10.1155/2016/4134735
- https://www.nasa.gov/pdf/143163main_Space.Food.and.Nutrition.pdf
- https://www.nasa.gov/vision/earth/everydaylife/jamestown-needs-fs.html
- https://www.kaa-yaa.com/the-most-accurate-way-to-calculate-your-daily-calorie-needs-and-macronutrient-breakdown/
- https://youtu.be/627VBkAhKTc
- https://whentosleep.com/
