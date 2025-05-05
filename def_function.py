#1.declare 
#2.Call

# syntax def() name code : call to use it 
import streamlit as st

def get_name(name):
    return name


def get_pizza_size():
    pizza_size = {"small":5 , "medium": 7 ,"Large":8}
    return pizza_size.items(size,0)

def get_additions(pizza_additions):
    return len(pizza_additions) * 1.5

def get_numbers_ordered(numbers):
    return numbers

def calculate_total(size,additions,amount):
    size = get_pizza_size()
    additions = get_additions()
    amount = get_numbers_ordered()
    total = (size + additions) * amount
    return total

st.title("Pizza Ordering System")
name = st.text_input("Enter your name")
pizza_size = st.text_input("Choose Pizaa Size",["small","medium","large"])
topings = st.select_multiple("Choose The topings ",["paperonni","additional_cheese","onions"])
values = st.input("Enter The size")
calculate = st.button("Calculate The prize")

if __name__ == "__main__":
    get_name(name=name)
    get_pizza_size(pizza_size)
    get_additions(topings)
    get_numbers_ordered(values)
    if calculate == True:
        calculate_total(size=get_pizza_size(pizza_size),additions=get_additions(topings),
                        amount=get_numbers_ordered(values))
    
    



