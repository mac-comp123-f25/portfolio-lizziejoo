income = {}
years = {"Lizzie": 2006, "Bob": 1990, "Susan": 1968}

years2 = years.copy()

print(years["Susan"])

years["Henry"] = 2004
print(years)

del years["Susan"]
print(years)