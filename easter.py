from matplotlib import pyplot as plt

while True:
    low = input("Year low bound: (default --> 1000) ") or 1000
    try:
        low = int(low)
        print("Using year as low bound: ", low)
        break
    except ValueError:
        print("This is not a valid year. Please enter a valid year")

while True:
    high = input("Year high bound: (default --> 3000) ") or 3000
    try:
        high = int(high)
        print("Using year as high bound: ", high)
        break
    except ValueError:
        print("This is not a valid year. Please enter a valid year")

# g - Golden year - 1
# c - Century
# h - (23 - Epact) mod 30
# i - Number of days from March 21 to Paschal Full Moon (PFM)
# j - Weekday for PFM (0=Sunday, etc)
# p - Number of days from March 21 to Sunday on or before PFM (-6 to 28)
for y in range(low, high, 1):
    g = y % 19
    c = y // 100
    h = (c - c // 4 - (8 * c + 13) // 25 + 19 * g + 15) % 30
    i = h - (h // 28) * (1 - (h // 28) * (29 // (h + 1)) * ((21 - g) // 11))
    j = (y + y // 4 + i + 2 - c + c // 4) % 7

    # p can be from -6 to 28
    p = i - j
    d = 1 + (p + 27 + (p + 6) // 40) % 31
    m = 3 + (p + 26) // 30
    # plotting the points on the graph
    # x --> date (p)
    # y --> year (y)
    plt.plot(p, y, marker="o", markersize=2, markeredgecolor="red",
             markerfacecolor="red")  # print(datetime.date(int(y), int(m), int(d)))

# show the graph :D
plt.xlabel("The date number")
plt.ylabel("Year")
plt.title("Easter day in  a given year")
plt.show()
