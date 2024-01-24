import streamlit as st

def main():
    st.title("Calorie Counter App")
    cal = 0

    while True:
        ask = st.text_input(
            """1. Hamburger - 250 cal
2. Big Mac - 563 cal
3. Hotdog - 272 cal
4. Slice of pizza - 277 cal
5. Ham sandwich - 447 cal
6. PB&J sandwich - 376 cal
7. French fries - 400 cal
8. Can of coke - 140 cal
9. Energy drink - 52 cal
10. Milkshake - 690 cal
11. Quit
Please enter the number of the food you want to eat:"""
        )

        if ask == "11":
            break

        cal += get_calories(ask)

    walk = 177
    run = 596
    bike = 650
    sit = 68

    st.write("Your total calorie intake is:", cal)
    st.write(
        "Walking:", (cal / walk).__round__(1),
        "hours\n",
        "Running:", (cal / run).__round__(1),
        "hours\n",
        "Biking:", (cal / bike).__round__(1),
        "hours\n",
        "Sitting:", (cal / sit).__round__(1),
        "hours"
    )

    chart_data = {
        "Activity": ["Walking", "Running", "Biking", "Sitting"],
        "Hours": [cal / walk, cal / run, cal / bike, cal / sit]
    }

    st.bar_chart(chart_data)

def get_calories(food_choice):
    calories_dict = {
        "1": 250, "2": 563, "3": 272, "4": 277, "5": 447,
        "6": 376, "7": 400, "8": 140, "9": 52, "10": 690
    }

    pizza = False
    if food_choice == "4":
        pizza = st.text_input("Pepperoni pizza ?(y/n)").lower() == "y"

    return calories_dict.get(food_choice, 0) + (309 if pizza else 0)

if __name__ == "__main__":
    main()
