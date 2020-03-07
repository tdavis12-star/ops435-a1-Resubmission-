#!/usr/bin/env python3

#OPS435 Assignment 1 - Winter 2020
#Program: a1_tdavis12.py
#Author: "Theodore Davis"
#The python code in this file a1_tdavis12.py is original work written by
#"Student Name". No code in this file is copied from any other source 
#except those provided by the course instructor, including any person, 
#textbook, or on-line resource. I have not shared this python script 
#with anyone or anything except for submission for grading.  
#I understand that the Academic Honesty Policy will be enforced and 
#violators will be reported and appropriate action will be taken.




import sys

def dbda():

    '''
    ################################### DOC FOR FUNCTION def dbda() #########################
    The dbda() function should be the main function of your script. The dbda() function will take a date in "YYYY-MM-DD" format, 
    a positive or negative integer, and return a date either before or after the given date according to the value of the given integer in the same format. 
    Your dbda() function should delegate the actual calculation of the target date to either the after() function or the before() function.
    '''

    if sys.argv[1][0] in '-':
        UserDate = sys.argv[2]
        DesiredDays = sys.argv[3]
        if int(DesiredDays) > 0: # for displaying the steps if the function 'after' is used
            listRange = list(range(1,int(DesiredDays)))
            checkedDate = dateValid(UserDate)
            v_days = int(DesiredDays)
            new_checkedDate = checkedDate
            for value in listRange:
                new_checkedDate = after(new_checkedDate,1)
                print(new_checkedDate) # prints the after steps
                result = new_checkedDate
        elif int(DesiredDays) < 1: # for displaying the steps if the function 'before' is used
            listRange = list(range(int(DesiredDays), -1))
            checkedDate = dateValid(UserDate)
            v_days = int(DesiredDays)
            new_checkedDate = checkedDate
            for value in listRange:
                new_checkedDate = before(new_checkedDate,-1)
                print(new_checkedDate) # prints the before steps
                result = new_checkedDate
         
    else:
        UserDate = sys.argv[1]
        DesiredDays = sys.argv[2]
        checkedDate = dateValid(UserDate)
        v_days = int(DesiredDays)
        if int(DesiredDays) > 0:    
            result = after(checkedDate,v_days)
        else:
            result = before(checkedDate,v_days)
    print(result)

def after(UserDate, DesiredDays):
    '''    
    ################ DOC FOR FUNCTION after() ##########################################
    # The after() function will take a date in "YYYY-MM-DD" format and return the date of the next day in the same format. 
    Next paragraph is a sample python code for the after() function. To earn the maximum possible mark for the assignment, 
    you should modify the sample after() function to make use of the days_in_mon() function.
    '''    

    date = UserDate.split('-')
    yr = date[0]
    month = date[1]
    og_day = int(date[2])
     
    if (og_day + int(DesiredDays)) > days_in_mon(month,yr):
        counter = days_in_mon(month,yr) - (og_day + int(DesiredDays))
        timer = 0
        n_month = month
        n_yr = yr
        while not counter >= 0:

            if int(n_month) <= 8:
                n_month =  '0' + str(int(n_month) + 1)
            elif 9 <= int(n_month) <= 11:
                n_month = str(int(n_month) + 1)
            else:
                n_month = '01'
                n_yr = str(int(n_yr) + 1)
                
            n_day = counter * -1 
            #if n_day in list(range(1,13)):
               # n_day = '0' + str(n_day)

            counter = days_in_mon(n_month,n_yr) - int(n_day)

            
            if 1 <= int(n_day) <= 9:
                FutureDay= '-'.join([n_yr, n_month, '0' + str(n_day)])
            else:
                FutureDay = '-'.join([n_yr, n_month, str(n_day)])

    else:
        n_day = str(og_day + int(DesiredDays))
        if 1 <= int(n_day) <= 9:
            FutureDay = '-'.join([yr, month, '0' + str(n_day)])
        else:
            FutureDay = '-'.join([yr, month, str(n_day)])

    return FutureDay

def before(UserDate, DesiredDays):

    '''    
    ####################### DOC FOR FUNCTION before()########################################
    #  The before() function will take a date in "YYYY-MM-DD" format and return the date of the previous day in the same format.
    '''    
    

    date = UserDate.split('-')
    yr = date[0]
    month = date[1]
    og_day = int(date[2])

    if og_day + int(DesiredDays) <= 0:
        counter = (og_day + int(DesiredDays))
        n_month = month
        n_yr = yr
        while counter <= 0:
            if 1 < int(n_month) <= 10:
                n_month = '0' + str(int(n_month) - 1)
            elif int(n_month) == 12 or int(n_month) == 11:
                n_month = str(int(n_month) - 1)
            else:
                n_month = '12'
                n_yr = str(int(n_yr) - 1)

            counter = days_in_mon(n_month,n_yr) + int(counter)
            n_day = counter
            
            if 1 <= int(n_day) <= 9:
                FutureDay= '-'.join([n_yr, n_month, '0' + str(n_day)])
            else:
                FutureDay= '-'.join([n_yr, n_month, str(n_day)])
    else:
        n_day = str(og_day + int(DesiredDays))
        if 1 <= int(n_day) <= 9:
            FutureDay= '-'.join([yr, month, '0' + str(n_day)])
        else:
            FutureDay= '-'.join([yr, month, str(n_day)])

    return FutureDay

    

def days_in_mon(month,yr):
    '''
    ############ DOC FOR FUNCTION days_in_mon #############
    #This function checks how many days are their in each month
    '''
   

    months = {"JAN":31,"FEB":28,"MAR":31,"APR":30,"MAY":31,"JUN":30,"JUL":31,"AUG":31,"SEP":30,"OCT":31,"NOV":30,"DEC":31}

    month = str(month)
    if leap_yr(yr) == True:
        months["FEB"]= 29
    days = list(months.values())
    month_index1 = str(month[0]) 
    month_index2 = str(month[1])
    if month_index1 == "0": # checks the first index of the string to see if it is '0' so we it can be removed later when converting the string into an integer
        month_index2 = int(month_index2) - 1
        monthDays= days[month_index2]
    elif month_index1 == "1": # checks the second index of the string and if it is '1' it will just retain it and add the first index into it then convert into an integer
        month_index1 = int(month_index1 + month_index2) - 1
        monthDays= days[month_index1]
    else:
        monthDays= 0
    return monthDays



def leap_year(yr): 

    '''
    ############### Leap Year #################
   # This function checks whether the given yr is a leap yr or not
    '''

    yr = int(yr)
    leapyr = yr % 4
    if leapyr == 0:
        status = True
    else:
        status = False

    leapyr = yr % 100
    if leapyr == 0:
        status = False

    leapyr = yr % 400
    if leapyr == 0:
        status = True

    return status
 


def valid_date(date): 

    '''    
    ############# Valid Date  ##############
   # This function checks whether the user inputted date 
    '''

    for value in date:
        if value not in ['0','1','2','3','4','5','6','7','8','9','-']:
            print('Error: wrong date entered')
            sys.exit()
        else:
            pass
    dateList = date.split('-')
    yr = dateList[0]
    month = dateList[1]
    og_day = dateList[2]

    if int(month) > 12 or int(month) < 1: # checks if the user inputted a correct month
        print('Error: wrong month entered')
        sys.exit()
    elif int(og_day) > days_in_mon(month,yr): # checks if the user inputted a correct day
        print('Error: wrong day entered')
        sys.exit()
    else:
        pass


    yr_length = len(yr) 
    month_length = len(month) 
    day_length = len(og_day) 


# making sure length of yr, month, and day is correct

    if int(yr_length) != 4: 
            print("Error: wrong year entered") 
            sys.exit() 
    if int(month_length) != 2: 
            print("Error: wrong month entered") 
            sys.exit()    
    if int(day_length) != 2: 
            print("Error: wrong day entered") 
            sys.exit()    



# making sure that only numerical values are used

    for value in yr:
        if value not in ['0','1','2','3','4','5','6','7','8','9']:
            print('Error: wrong year entered')
            sys.exit()
        else:
            pass
    for value in month:
        if value not in ['0','1','2','3','4','5','6','7','8','9']:
            print('Error: wrong month entered')
            sys.exit()
        else:
            pass
    for value in og_day:
        if value not in ['0','1','2','3','4','5','6','7','8','9']:
            print('Error: wrong day entered')
            sys.exit()
        else:
            pass

    return date



def usage():
       
      '''
########################## Usage #####################################
    print("Usage:" + sys.argv[0] + " [--step] yr-month-og_day +/-n")
    sys.exit()
      '''

if __name__ == '__main__':
    if ((len(sys.argv) >= 5 or len(sys.argv) <= 2)):
        usage()

    if sys.argv[1] == '--step':
        UserDate = sys.argv[2]
        DesiredDays = sys.argv[3]
    else:
        UserDate = sys.argv[1]
        DesiredDays = sys.argv[2]


