import streamlit as st

st.title("Calculator: Eg-2")

num1 = st.number_input("Enter 1st number")
num2 = st.number_input("Enter 2st number")

col1, col2, col3, col4 = st.columns(4)

if col1.button("Add"):
    result = num1 + num2
    st.success(f"Ans is {result}")
    st.balloons()

elif col2.button("Sub"):
    result = num1 - num2
    st.success(f"Ans is {result}")
    st.balloons()

elif col3.button("Mul"):
    result = num1 * num2
    st.success(f"Ans is {result}")
    st.balloons()

elif col4.button("Div"):
    if num2 != 0:
        result = num1 / num2
        st.success(f"Ans is {result}")
        st.balloons()
    else:
        st.error("Error: Cannot divide by zero!")
