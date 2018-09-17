birthday = {
            'Som' : '1-11111',
            'Vanitha' : '2-22222',
            'Kavitha' : '33-333',

            }
def bd():
    n_key = birthday.keys()
    print n_key
    name = raw_input('Enter a name :')
    print(type(name))
    if (type(name)== str):
        if name in n_key:
            print birthday[name]
        else:
            print('We dont have the recods for %s, Do you want to add %s to the list Y/N :') %(name, name)
            op = raw_input()
            if op == 'Y':
                birthday[name] = input('Enter the date of birth : ')
                print('Do you want to print the new Name and Birthday : Y/N')
                if (raw_input() == 'Y') :
                    bd()
                else :
                    print ("Good bye")
            else:
                name = raw_input('Enter valid name : ')
    else:
        pirnt('Please enter a valid name : ')
        bd()
bd()
