import streamlit as st
import re

st.set_page_config(page_title="Make Your Password Stronger", page_icon="🔒")

st.title("Password Strength Checker 🔒")
st.markdown("Enter your password below to check its strength.")

password = st.text_input("Enter your password", type="password")
check_button = st.button("Enter to Check")

if check_button:
    feedback = []
    score = 0

    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain both uppercase and lowercase letters.")

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")

        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

        if score == 4:
            feedback.append("✅ Your password is strong.")
        elif score == 3:
            feedback.append("🟡 Your password is medium, make it stronger.")
        else:
            feedback.append("🔴 Your password is weak, make it stronger.")

        if feedback:
            st.markdown("## Improvement Suggestions")
            for tip in feedback:
                st.write(tip)
    else:
        st.warning("Please enter your password before checking.")
