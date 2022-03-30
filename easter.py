import datetime

from matplotlib import pyplot as plt

print("""
(1) --> Calculate easter in year range
(2) --> Calculate easter for specific year
""")

while True:
    option = input("Choose (1) / (2) ")
    try:
        option = int(option)
        if option in (1, 2):
            break
    except ValueError:
        print("This is not a valid option")


# g - Golden year - 1
# c - Century
# h - (23 - Epact) mod 30
# i - Number of days from March 21 to Paschal Full Moon (PFM)
# j - Weekday for PFM (0=Sunday, etc)
# p - Number of days from March 21 to Sunday on or before PFM (-6 to 28)
def p_grabber():
    g = y % 19
    c = y // 100
    h = (c - c // 4 - (8 * c + 13) // 25 + 19 * g + 15) % 30
    i = h - (h // 28) * (1 - (h // 28) * (29 // (h + 1)) * ((21 - g) // 11))
    j = (y + y // 4 + i + 2 - c + c // 4) % 7

    # return can be from -6 to 28
    return i - j


if option == 1:
    while True:
        low = input("Year low bound: (default --> 1000) ") or 1000
        high = input("Year high bound: (default --> 3000) ") or 3000
        try:
            low = int(low)
            high = int(high)
            print("Calculating easter in range:", low, "-->", high)
            break
        except ValueError:
            print("This is not a valid year. Please enter a valid year")

    for y in range(low, high, 1):
        # plotting the points on the graph
        # x --> date (p)
        # y --> year (y)
        plt.plot(p_grabber(), y, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red")
    # show the graph :D
    plt.xlabel("The date number")
    plt.ylabel("Year")
    plt.title("Easter day in  a given year")
    plt.show()
else:
    while True:
        year = datetime.datetime.now().year
        year = input("Specify year ") or year
        try:
            y = int(year)
            print("Using year", year)
            break
        except ValueError:
            print("This is not a valid year. Please enter a valid year")
    p = p_grabber()
    d = 1 + (p + 27 + (p + 6) // 40) % 31
    m = 3 + (p + 26) // 30
    print(datetime.date(int(year), int(m), int(d)))
