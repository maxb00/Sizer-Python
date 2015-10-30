def cumulative_sum(number_list):
    # number_list is a list of numbers
    culm = []
    x = 0
    for num in number_list:
        if x == 0:
            culm.append(num)
            x = x + 1
        elif x > 0:
            culm.append(num + culm[x-1])
            x += 1
    return culm


# Test Cases
print(cumulative_sum([4, 3, 6]))
##### YOUR CODE HERE #####

# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    c = int(input("How many classes did you take?"))
    names = []
    grades = []
    average = 0

    for i in range(0, c):
        names.append(str(input("What was the name of the class?")))
        grades.append(int(input("What was your grade? (number)")))
        
    for i in range(0, c):
        average = grades[i] + average
    average = average / c
    print("REPORT CARD:")
    for i in range(0, c):
        print(names[i], "-", grades[i])
              
    print("Overall GPA", average)
    
# Test Cases
report_card()
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    
    ##### YOUR CODE HERE #####
    x = None
    ext = "ay"
    wordList = list(word)
    try:
        x = VOWELS.index(wordList[0])
        if x == 1 or x == 2 or x == 3 or x == 4 or x == 0:
            wordList.extend(['h', 'a', 'y'])
            word = "".join(wordList)
    except ValueError:
        firstLetter = wordList[0]
        wordList.remove(wordList[0])
        wordList.extend([firstLetter, 'a', 'y'])
        word = "".join(wordList)
        
    return word    

# Test Cases
print(pig_latin("word"))
print(pig_latin("antimatter"))


input("Press any key to exit")
