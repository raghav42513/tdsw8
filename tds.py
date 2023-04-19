import streamlit as st

st.title("Find the largest number")
n1 = st.number_input("Enter 1st Number")
n2 = st.number_input("Enter 2nd Number")
n3 = st.number_input("Enter 4rd Number")
calculate = st.button("Find the largest number")

def largest(n1,n2,n3):
    if n1>n2 and n1>n3:
      return n1
    elif n2>n1 and n2>n3:
      return n2
    else:
      return n3
if calculate:
  largest_num = largest(n1,n2,n3)
  st.write("The largest number is: ", largest_num)
    