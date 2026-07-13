def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if (year%100==0):
        if(year%400==0):
            return True
        else:
            return False
    elif (year%4 == 0):
            return True
    else:
        return False
        

print(is_leap_year(2100))