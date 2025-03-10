import streamlit as st
import re

st.set_page_config(page_title="Make Your Password Stronger", page_icon="🔒")

st.title("Password Strength Checker 🔒")
st.markdown("Enter your password below to check its strength.")

password = st.text_input("Enter your password", type="password")
check_button = st.button("Enter to Check")

def evaluate_password(password):
    rules = {
            "❌ Password should be at least 8 characters long.": len(password) >= 8,
            "❌ Password should contain both uppercase and lowercase letters.": re.search(r"[A-Z]", password) and re.search(r"[a-z]", password),
            "❌ Password should contain at least one digit.": re.search(r"\d", password),
            "❌ Password should contain at least one special character (!@#$%^&*).": re.search(r"[!@#$%^&*]", password),
    }

    score = sum(rules.values())
    feedback = [msg for msg, passed in rules.items() if not passed]

    strenght_msg = {
        4: "✅ Your password is strong.",
        3: "🟡 Your password is medium, make it stronger.",
        2: "🔴 Your password is weak, make it stronger.",
        1: "🔴 Very weak password! Change it immediately.",
        0: "🚨 Extremely weak password! Use a more secure one."
    }

    feedback.append(strenght_msg.get(score, "🚨 Extremely weak password! Use a more secure one"))
    return feedback

if check_button:
    if password:
        feedback = evaluate_password(password)
        st.markdown("## Improvement Suggestions")
        for tip in feedback: 
            st.write(tip)
    else:
        st.warning("Please enter your password before checking.")