# datetime module is used to get date and time from your computer
# the date or time from your computer is considered as naive date and time
# so for that reason you must convert it to UTC format and then you can change it aware date and time
# an aware date and time is just date and time that is according to a persons location
# the modern way of doing this is to use zoneinfo.ZoneInfo that converts UTC to date and time of ther user
# naive and aware date and time cannot be compared and would result in a TypeError
# strftime stands for string from time - returns a string by converting time obj 
# strptime stands for string parsing time - takes in a string and changes it to a time obj 
# format should be given in strptime methods
# date class gives date like 14-08-1947
# time class gives time in 24 hours
# timedelta can be used for operations such as add, subtract, multiply and divide on time obj 


# example
from datetime import datetime, date, time, timedelta

cur_time = datetime.now()  # gets current date and time
formatted_time = cur_time.strftime("%S-%M-%H, %d:%m:%Y")
print(formatted_time)
formatted_time = cur_time.strptime("8-14-1947","%m-%d-%Y")
print(formatted_time)

today = date.today()
next_week = timedelta(days=7)
print(f"today: {today}, next week: {today + next_week}")