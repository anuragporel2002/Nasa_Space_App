#Daily Sleep Scheduling Code based on sleep hour and working hours
#-------------------Import Modules----------------------------------
from datetime import datetime, date, timedelta

#-------------------Constants (00:00:00 hrs)------------------------
global time
time=datetime.strptime('00:00:00','%H:%M:%S').time()

#-------------------Functions---------------------------------------
def Sleep_Customiser(work_start,work_end,preparation,refresh,sleep_hour,sleep_buffer):
#-------------------Input Formatting--------------------------------
    work_start_format=datetime.strptime(work_start, '%H:%M:%S').time()
    work_end_format=datetime.strptime(work_end, '%H:%M:%S').time()
#-------------------Work Hour---------------------------------------
    temp_start=datetime.combine(date.min,work_start_format)-datetime.combine(date.min,time)
    temp_end=datetime.combine(date.min,work_end_format)-datetime.combine(date.min,time)
    if temp_end>temp_start:
        work_hour=datetime.combine(date.min,work_end_format)-datetime.combine(datetime.min,work_start_format)
    elif temp_end<temp_start:
        work_hour=datetime.combine(date.min+timedelta(days=1),work_end_format)-datetime.combine(datetime.min,work_start_format)
#------------------Min Active Hour, Total Sleep Hour, Available Sleep Hours---------------
    non_sleep_hours=work_hour+timedelta(hours=preparation)+timedelta(hours=refresh)
    total_sleep_hours=timedelta(hours=sleep_hour)+timedelta(minutes=sleep_buffer)
    available_sleep_time=timedelta(hours=24)-non_sleep_hours
#-----------------Start and End time of Sleep---------------------------------------------
    start_sleep_avail=(datetime.combine(date.min,work_end_format)+timedelta(hours=refresh)).time()
    end_sleep_avail=(datetime.combine(date.min,work_start_format)-timedelta(hours=preparation)-total_sleep_hours).time()
#-----------------Continuity checker------------------------------------------------------
    temp_start_avail=datetime.combine(date.min,start_sleep_avail)-datetime.combine(date.min,time)
    temp_end_avail=datetime.combine(date.min,end_sleep_avail)-datetime.combine(date.min,time)
    if temp_end_avail<temp_start_avail:
        temp_end_avail=datetime.combine(date.min+timedelta(days=1),end_sleep_avail)-datetime.combine(date.min,time)
#-----------------Time Slot Storage--------------------------------------------------------
    start_list=[]
    end_list=[]
#-----------------Work Load Checking-------------------------------------------------------
    if total_sleep_hours>available_sleep_time:
#-----------------Less Sleep Time----------------------------------------------------------
        print('Reduce Your Activity Hour')
    else:
        while temp_start_avail<=temp_end_avail:
            ts=(datetime.combine(date.min,time)+temp_start_avail).time()
            te=(datetime.combine(date.min,time)+temp_start_avail+total_sleep_hours).time()
            start_list.append(ts.strftime('%H:%M:%S'))
            end_list.append(te.strftime("%H:%M:%S"))
            temp_start_avail=temp_start_avail+timedelta(minutes=30)
        print()
        print("Your Customised Available Slots of Sleeping. Sweet Dreams.")
        for i in range(len(start_list)):
            print("Sleep: ",start_list[i]," Wake Up: ",end_list[i])            
    return

#-------------------Running the Code--------------------------------
if __name__=="__main__":
#-------------------Parameter Input from User-----------------------
    work_start=str(input("Enter the time you start for work (in HH:MM:SS and 24 hours format): "))
    work_end=str(input("Enter the time you finish work (in HH:MM:SS and 24 hours format): "))
    sleep_hour=float(input("Daily Required Sleep hours (in hours): "))
    sleep_buffer=float(input("Time required to fall asleep (in minutes): "))
    preparation=float(input("Time Require to be ready after waking up (in hours): "))
    refresh=float(input("Time required to refresh after work (in hours): "))
#-------------------Function Calling & Output Formatting------------
    Sleep_Customiser(work_start,work_end,preparation,refresh,sleep_hour,sleep_buffer)
