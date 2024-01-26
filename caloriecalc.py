import streamlit as st

# Constants for calorie burn rates
walk = 177; run = 596; bike = 650; sit = 68

def main():
    st.title("Calorie Counter App")
    calories_dict = {
        "Hamburger": 250, "Big Mac": 563, "Hotdog": 272, "Slice of pizza": 277, "Ham sandwich": 447,
        "PB&J sandwich": 376, "French fries": 400, "Can of coke": 140, "Energy drink": 52, "Milkshake": 690
    }

    # CSS to hide the label of number_input
    hide_label_css = """
        <style>
            .stNumberInput > label {
                display: none;
            }
        </style>
    """
    st.markdown(hide_label_css, unsafe_allow_html=True)

    total_calories = 0

    st.write("### Select Food Items and Enter Quantity:")
    for item in calories_dict.keys(): 
        col1, col2 = st.columns([2, 1])  # Adjust the ratio to change the size of columns
        with col1:
            st.markdown(f"<p style='text-align: left; display: table-cell; vertical-align: middle;'>{item}</p>", unsafe_allow_html=True)
        with col2:
            quantity = st.number_input("", min_value=0, max_value=100, key=f"{item}_input")
            total_calories += quantity * calories_dict[item]

    # Display the total calories and the exercise equivalents
    st.write("Your total calorie intake is:", total_calories)
    st.write("Walking for", round(total_calories / walk, 1), "hours will burn these calories.")
    st.write("Running for", round(total_calories / run, 1), "hours will burn these calories.")
    st.write("Cycling for", round(total_calories / bike, 1), "hours will burn these calories.")
    st.write("Sitting for", round(total_calories / sit, 1), "hours will burn these calories.")


if __name__ == "__main__":
    main()
