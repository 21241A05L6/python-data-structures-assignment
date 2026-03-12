import streamlit as st

st.title("Price Calculator")

price = st.number_input("Enter product price", min_value=0.0)

discount = st.slider("Select discount (%)", 0, 50, 10)

if st.button("Calculate Price"):

    final_price = price - (price * discount / 100)

    st.success(f"Final Price: {final_price}")

    st.table([
        ["Original Price", price],
        ["Discount %", discount],
        ["Final Price", final_price]
    ])