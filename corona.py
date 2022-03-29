from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name(input('enter the country name to show current status covid19 in the country :'))
for x in cases:
    print(x,':',cases[x])
