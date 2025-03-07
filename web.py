import streamlit as st
import json
import random

# Sustainable Development Goals Data
sdg_goals = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere."},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition."},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all ages."},
    {"id": 4, "title": "Quality Education", "description": "Ensure inclusive and equitable quality education for all."},
    {"id": 5, "title": "Gender Equality", "description": "Achieve gender equality and empower all women and girls."},
    {"id": 6, "title": "Clean Water and Sanitation", "description": "Ensure availability and sustainable management of water and sanitation for all."},
    {"id": 7, "title": "Affordable and Clean Energy", "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all."},
    {"id": 8, "title": "Decent Work and Economic Growth", "description": "Promote sustained, inclusive, and sustainable economic growth."},
    {"id": 9, "title": "Industry, Innovation and Infrastructure", "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization."},
    {"id": 10, "title": "Reduced Inequalities", "description": "Reduce inequality within and among countries."},
    {"id": 11, "title": "Sustainable Cities and Communities", "description": "Make cities inclusive, safe, resilient, and sustainable."},
    {"id": 12, "title": "Responsible Consumption and Production", "description": "Ensure sustainable consumption and production patterns."},
    {"id": 13, "title": "Climate Action", "description": "Take urgent action to combat climate change and its impacts."},
    {"id": 14, "title": "Life Below Water", "description": "Conserve and sustainably use the oceans, seas, and marine resources."},
    {"id": 15, "title": "Life on Land", "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems."},
    {"id": 16, "title": "Peace, Justice and Strong Institutions", "description": "Promote peaceful and inclusive societies for sustainable development."},
    {"id": 17, "title": "Partnerships for the Goals", "description": "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development."}
]

# Quiz questions for SDG 1 - No Poverty
quiz_questions = [
    {"question": "As of 2019, what percentage of the world’s population lived in extreme poverty (earning less than $1.90 per day)?", "options": ["5.2%", "9.2%", "12.5%", "15.1%"], "answer": "9.2%"},
    {"question": "In 2021, due to the COVID-19 pandemic, the number of people living in extreme poverty increased for the first time in 20 years. Approximately how many million people fell into poverty?", "options": ["50 million", "75 million", "90 million", "120 million"], "answer": "120 million"},
    {"question": "Which region had the highest extreme poverty rate in 2022?", "options": ["South Asia", "Sub-Saharan Africa", "Latin America", "East Asia"], "answer": "Sub-Saharan Africa"},
    {"question": "In 2015, what percentage of children under 5 in low-income countries were malnourished due to poverty?", "options": ["10%", "20%", "30%", "40%"], "answer": "30%"},
    {"question": "According to the UN, what is the target year for eradicating extreme poverty for all people under SDG 1?", "options": ["2030", "2040", "2050", "2060"], "answer": "2030"},
    {"question": "What percentage of people in low-income countries lack access to social protection programs?", "options": ["25%", "50%", "70%", "90%"], "answer": "70%"},
    {"question": "Between 2010 and 2019, the global poverty rate declined from 15.7% to what percentage?", "options": ["12.3%", "9.2%", "7.8%", "6.4%"], "answer": "9.2%"}
]

# Quiz questions for SDG 2 (Zero Hunger)
sdg_2_questions = [
    {"question": "As of 2022, approximately how many people worldwide suffered from hunger?", "options": ["500 million", "670 million", "735 million", "900 million"], "answer": "735 million"},
    {"question": "What percentage of children under 5 globally were affected by stunting (low height for age) in 2021?", "options": ["10%", "15%", "22%", "30%"], "answer": "22%"},
    {"question": "Which region had the highest prevalence of undernourishment in 2022?", "options": ["Sub-Saharan Africa", "South Asia", "Latin America", "Middle East"], "answer": "Sub-Saharan Africa"},
    {"question": "How many people globally were affected by food insecurity in 2021 (moderate or severe)?", "options": ["1.2 billion", "2.3 billion", "3 billion", "3.5 billion"], "answer": "2.3 billion"},
    {"question": "By what year does SDG 2 aim to end all forms of hunger and malnutrition?", "options": ["2025", "2030", "2040", "2050"], "answer": "2030"}
]


# Streamlit UI
st.set_page_config(layout="wide")
st.title("🌍 Sustainable Development Goals (SDGs) Dashboard")
st.write("Explore the 17 Sustainable Development Goals set by the United Nations.")

# Display SDG goals as a grid dashboard
cols = st.columns(3)  # Create a 3-column layout

for index, goal in enumerate(sdg_goals):
    with cols[index % 3]:
        with st.container():
            st.markdown(f"### {goal['title']}")
            st.write(goal["description"])
            
            if goal["id"] == 1:  # Only add quiz for SDG 1
                if st.button(f"Let's Start Quiz! 📝", key=f"quiz_{goal['id']}"):
                    st.session_state["selected_sdg"] = goal["title"]
                    st.session_state[f"quiz_started_{goal['id']}"] = True
                    st.session_state[f"random_questions_{goal['id']}"] = random.sample(quiz_questions, 5)
                
                if st.session_state.get(f"quiz_started_{goal['id']}", False):
                    st.subheader(f"Quiz for {goal['title']}")
                    for i, q in enumerate(st.session_state[f"random_questions_{goal['id']}"]):
                        st.write(f"Q{i+1}: {q['question']}")
                        answer = st.radio("Choose an answer:", q["options"], key=f"quiz_question_{goal['id']}_{i}")
                        if st.button(f"Submit Answer {i+1}", key=f"submit_{goal['id']}_{i}"):
                            if answer == q["answer"]:
                                st.success("Correct! 🎉")
                            else:
                                st.error("Incorrect. Try again! ❌")
            
            st.markdown("---")  # Add a horizontal line for separation

# JSON API-like data preview
if st.checkbox("Show SDG Data (JSON format)"):
    st.json(sdg_goals)
