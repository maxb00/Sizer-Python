# Name:
# Section:
# hw3.py


# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'6.01':'Introduction to EECS'}

def add_class(class_num, desc):

    my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    for i in my_classes:
        listClasses = list(i)
        if course in listClasses:
            print(i, '-',  my_classes[i])
        else:
            print("No Course", course, "classes taken.")

# Test Cases for Exercise 3.3
print_classes('6')
print_classes('7')
##### YOUR CODE HERE #####

# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    return comb_dict

# combined_dict = combine_lists(??, ??) # Finish this line...

def people(age):
    # Use combined_dict within this function...
    return "Not Yet Implemented"

# Test Cases for Exercise 3.4 (all should be True)
#print 'Dan' in people(18) and 'Cathy' in people(18)
#print 'Ed' in people(19) and 'Helen' in people(19) and\
#       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
#print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
#print people(21) ==   ['Bob']
#print people(22) ==   ['Kelly']
#print people(23) ==   []

# **********  Exercise 3.5 **********

#def zellers(month, day, year):
#   ##### YOUR CODE HERE #####

 #   return "Not Yet Implemented"

# Test Cases for Exercise 3.5
#print zellers("March", 10, 1940) == "Sunday" # This should be True
##### YOUR CODE HERE #####
input()