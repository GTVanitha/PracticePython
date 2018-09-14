import datetime

while True:
    try: 
        name = raw_input("Enter your name:")
        age = int(input("Enter your age and I will tell you when you will turn 100 :"))

    except:
        print "Enter valid input"
        continue
    else:
        break

print "Hello %s" %(name)

# Get current time
now = datetime.datetime.now()


age_diff = 100-age
c_year = now.year

done_year = c_year + age_diff
exp_year = c_year + age_diff


if age > 100:
    print "You have crossed 100 %d years back. Year:%d" %(abs(age_diff), done_year)
else:
    print "You will turn 100 in %d years. Year:%d" %(age_diff, exp_year) 

