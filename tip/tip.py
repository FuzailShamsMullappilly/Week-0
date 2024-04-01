def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #This function removes dollar sign
    remove_dollar = d.replace("$","")
    return float(remove_dollar)


def percent_to_float(p):
    #This frunction removes persentage sign
    remove_percent = p.replace("%","")
    percent_converted = float(remove_percent) / 100
    return percent_converted
#Calling main
main()
