import streamlit as st
import pandas as pd
import random

# Load quiz questions
df = pd.read_csv("sdg_quiz.csv")

# Function to display SDG cards
def show_sdg_cards():
    st.title("🌍 Choose an SDG to Explore!")
    
    col1, col2, col3 = st.columns(3)
    sdg_goals = [f"SDG {i}" for i in range(1, 18)]
    
    selected_sdg = None
    for i, sdg in enumerate(sdg_goals):
        with [col1, col2, col3][i % 3]:
            if st.button(sdg):
                selected_sdg = sdg
                
    return selected_sdg

# Function to conduct quiz
def quiz(sdg):
    st.subheader(f"🎯 {sdg} Quiz!")
    questions = df[df["SDG"] == sdg].sample(3)  # Select 3 random questions
    
    score = 0
    for i, row in questions.iterrows():
        st.write(f"*Q{i+1}: {row['Question']}*")
        options = [row["Option A"], row["Option B"], row["Option C"], row["Option D"]]
        answer = st.radio("Choose your answer:", options, key=i)
        
        if answer == row["Correct Answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong! The correct answer is: {row['Correct Answer']}")

    st.write(f"🎯 *Final Score: {score}/3*")
    st.button("🔄 Play Again", on_click=lambda: st.experimental_rerun())

# Main function
def main():
    sdg = show_sdg_cards()
    if sdg:
        quiz(sdg)

if _name_ == "_main_":
    main()
