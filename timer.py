"""
# This is a mini prject undertaken by me where i create a ccountdown timer
so this is how i am going to proceed
-a user to enter the time according to their needs ( hours, minutes,seconds)
-if user does not enter the either of the three it is considered to be zero
-natural working timer is the second is reducing by 1 and the minute reduces when second is reduced by 60 and hour is reduced when minute is reduced by 60
-so we take input of hour and minute and seconds 
-then set a 3 nested for loop where 60(min)=-hours,60 of the sec=-min,seconds=-1
-then naturally the output is refreshed everytime with the new set of values and not stored 


problems now
-don't know how to fix the "60 of 'smtg'"
-don't know how to not bring a set of outputs/iterations but a single set of output

solutions for the problem
-maybe we can put the above three loops in the while or for loop set the ultimate time limit (i.e..timer) we can tackle the second issue
-

 SORRY GUYS I WAS DUMB THERE WAS A MODULE WHERE WE CAN DO THIS MORE EASILY EFFICIENTLY
"""

"""
 I WILL STILL SAVE MY USELESS BRAINSTORMING THO
hours = int(input("hours:"))
minute = int(input("minute:"))
second = int(input("seconds:"))
if hours or minute or second == None:
    hours, minute, second = 0, 0, 0

while hours and minute and second>=0,0,0:
    for hour_count in range(hours):
        if minute == 60:
            hour_count = -1
        for minute_count in range(minute):
            if second == 60:
                minute_count = -1
            for second_count in range(second):
                second_count = -1
print()
"""

"""
  so i lost but i promise i will try well we can do it using time module
  so by the bro code channel method 
  bro code method is easy ngl and chatgpt method is more sophisticated
  method (chatgpt):
  -impot time
  -then set the time.sleep(-1): This pauses the execution of the program for 1 second in each iteration of the loop. It creates a one-second delay between each update of the countdown timer, making it look like a real-time countdown. 
  -input hours , minutes and seconds and then convert it to total seconds where total seconds=hours*3600+minutes*60+seconds
  -while the total seconds >0 then convert everything to the amount of hours and second and mintues left then print it in the form of HH:MM:SS with padding with end=\r  to rewrite the previous iterations
  -then iterate the total seconds by -1  
"""
import time

hours = int(input("Enter the hour:"))
minutes = int(input("Ente the minute:"))
seconds = int(input("Enter the second:"))
if hours is None:
    hours == 0
if minutes is None:
    minutes == 0
if seconds is None:
    seconds == 0
total_seconds = hours * 3600 + minutes * 60 + seconds
while total_seconds > 0:
    hour_count = total_seconds // 3600
    minutes_count = (total_seconds % 3600) // 60
    second_count = total_seconds % 60
    print(f"{hour_count:02d}:{minutes_count:02d}:{second_count:02d}", end="\r")
    total_seconds -= 1
    time.sleep(1)
print("time's up")
