#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 1
#calculate time from seconds to hours, minutes, and seconds

#get the time in seconds from the user
#convert input to integer
total = int(input("Enter a the time in seconds between 1 and 86400: "))

#convert seconds to hours (3600 seconds in 1 hour)
hours = int(total / 3600)

#convert remaining seconds to minutes (60 seconds in 1 minute)
minutes = int((total - (hours * 3600)) / 60)

#convert remaining seconds to seconds
seconds = int(total - (hours * 3600) - (minutes * 60))

#check whether the time is within range
#report the time in hours, minutes, and seconds
if total >= 1 and total <= 86400:
    print("The time is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
else:
    print("The total time is not within the range.")
