import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_bg_from_local(image_path):
    encoded_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_local("C:/Users/Admin/Desktop/portofolio/python for Backend and Data Science/functions/Pizza Order Now Interface.png")


# Define pizza prices
def get_base_price(size):
    prices = {'Small': 5, 'Medium': 8, 'Large': 12}
    return prices.get(size, 0)

# Define topping cost
def get_topping_price(toppings):
    return len(toppings) * 1.5

# Calculate total
def calculate_total(size, toppings, quantity):
    base = get_base_price(size)
    topping_total = get_topping_price(toppings)
    return (base + topping_total) * quantity

# Streamlit UI
st.title("🍕 Pizza Ordering System")
name = st.text_input("Enter your name:")
size = st.selectbox("Choose pizza size:", ["Small", "Medium", "Large"])
toppings = st.multiselect("Choose toppings:", ["Pepperoni", "Mushrooms", "Extra Cheese", "Onions", "Olives"])
quantity = st.slider("How many pizzas?", 1, 10)

if st.button("Calculate Total"):
    total = calculate_total(size, toppings, quantity)
    st.success(f"{name}, your total is ${total:.2f}")
