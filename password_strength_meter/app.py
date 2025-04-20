import streamlit as st 
import re 
import random as rd

st.set_page_config(page_title="PASSWORD STRENGTH CHECKER", page_icon="🔒")
st.title("PASSWORD STRENGTH CHECKER")
st.subheader("Check the strength of your password and get suggestions for a stronger one.")
#ENTERED PASSWORD
user_input = st.text_input("🔑Enter your password", type="password") 
chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '^',
    '_', '`', '~']


#FUNCTION 02
def suggestedpassword():
    while True:
        suggest_password = '' .join(rd.choices(chars, k=11))
        if (len(suggest_password) >= 8 and re.search('[A-Z]', suggest_password) and
            re.search('[a-z]', suggest_password) and
            re.search('[0-9]', suggest_password) and
            re.search("[!@#$%^&*(),.?]", suggest_password)):
            return suggest_password

#FUNCTION 01
def password_strength_check(password):
    score = 0
# LENGTH CHECK 
    if len(password) >=  8:
        score += 1
    else:
        st.warning("🔴 Password should be at least 8 characters long.")
# CHARACHTER_CHECK 
    if re.search('[A-Z]', password) and re.search('[a-z]',password):
        score += 1
    else:
        st.warning("🔴 Password should contain both uppercase and lowercase letters.")
# DIGIT CHECK
    if re.search('[0-9]', password):
        score += 1
    else:   
        st.warning("🔴 Password should contain at least one digit.")
# SPECIAL CHARACTER CHECK
    if re.search("[!@#$%^&*(),.?]" , password):
        score +=1 
    else:
        st.warning("🔴 Password should contain at least one special character.")
# SCORE CHECKING AND FEEDBACK
    if score == 4:
        st.success("✅ Password is strong.")
    elif score == 3:
        st.info("❗Password is medium.")
    else:
        st.warning("❌ Password is weak.")

#ENTERED PASSWORD CHECKING
if user_input:
    password_strength_check(user_input)
#SUGGESTED PASSWORDS
if st.button("🔑 Suggest Passwords"):
        st.subheader("💡 Suggested Passwords:")
        for _ in range(3):  # Show 3 suggestions We can do as much as we want like 5 suggestions ...6..7
            st.code(suggestedpassword(), language="text")