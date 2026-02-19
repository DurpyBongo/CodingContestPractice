countries = []
temperatures = []

while True:
    city_temp = input()
    temporary = city_temp.split(' ')
    temperatures.append(int(temporary[1]))
    countries.append(temporary[0])
    if temporary[0] == 'Waterloo':  
        break
temperatures.index(min(temperatures))
print(countries[temperatures.index(min(temperatures))])