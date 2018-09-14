
birthdays = {
        'Vanitha' : '05/05/90',
        'Som' : '02/04/84',
        'Vino' : '08/08/91'
        } 

def b_days(): 
    print "Welcome to birthday dictionary! We know the birthdays of:"
    
    names =  birthdays.keys()
    
    print ',\n'.join(names)
    
    whose = raw_input("Who's birthday do you want to look up?")
    
    if (whose in names):
    
        print whose , "'s birthday is ", birthdays[whose]
        print "Thank you for using birthday dictionary. Happy day :)"
    else:
        print "Sorry. We do not have ", whose, " birthday date."
    
        add = raw_input(" Do you want to add it ? (y/n)" )
    
        if add == 'y':
            name = raw_input("Enter name:")
            bday = raw_input("Enter birth date:")
            birthdays[name] = bday
            print "Added ", name, "'s birthday to dictionary. Try accessing it!"
            b_days()
        else:
            print "Thank you for using birthday dictionary. Happy day :)"
    


b_days()

