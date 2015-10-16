class Conversions:
    def monthconv(x):
        x = str(x)
        if x.lower() == "march":
            x = 1
        elif x.lower() == "april":
            x = 2
        elif x.lower() == "may":
            x = 3
        elif x.lower() == "june":
            x = 4
        elif x.lower() == "july":
            x = 5
        elif x.lower() == "august":
            x = 6
        elif x.lower() == "september":
            x = 7
        elif x.lower() == "october":
            x = 8
        elif x.lower() == "november":
            x = 9
        elif x.lower() == "december":
            x = 10
        elif x.lower() == "january":
            x = 11
        elif x.lower() == "february":
            x = 12

        return x

    def dayconv(a, b, c, d):
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        g = (13 * a - 1) / 5
        l = c/4
        h = d/4
        f = g + l + h + b + c - 2*d
        q = f % 7
        q = int(q)

        if q == 0:
            q = "Sunday"
        elif q == 1:
            q = "Monday"
        elif q == 2:
            q = "Teusday"
        elif q == 3:
            q = "Wednesday"
        elif q == 4:
            q = "Thursday"
        elif q == 5:
            q = "Friday"
        elif q == 6:
            q = "Staurday"

        return q
class Main:
    print("Enter a date:")
    A = Conversions.monthconv(input("Month:"))
    day = input("Day:")
    B = int(day)
    print("Note: If the date is in January or February, please input the year BEFORE the date.")
    yearX = input("Enter the last 2 numbers of the year:")
    yearY = input("Enter the first 2 numbers of the year:")
    C = int(yearX)
    D = int(yearY)

    print(Conversions.dayconv(A, B, C, D))