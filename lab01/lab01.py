temp = int(input("Enter the current temperature in degrees: "))
budget = float(input("Enter your available budget ($): "))
weather_condition = input("Enter the current weather condition (e.g., sunny, rainy, cloudy): ")

if((weather_condition == "sunny") and (temp > 75)):
   if(budget > 20):
        print("Go to the beach!")
   else:
       print("Have a picnic in the park.")
elif(weather_condition == "rainy"):
    if(budget > 15):
        print("Visit a museum.")
    else:
        print("Stay in and watch a movie at home.")
elif((weather_condition == "cloudy") or (temp < 60)):
    print("Go to a coffee shop and enjoy a warm drink.")