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

# Quiz Questions for SDG 8
sdg_8_questions = [
    ("What is the main focus of SDG 8?", ["End poverty", "Promote decent work and economic growth", "Ensure quality education", "Achieve gender equality"], "Promote decent work and economic growth"),
    ("Which of the following is a key target of SDG 8?", ["Achieve universal healthcare", "Promote sustained economic growth", "Increase fossil fuel use", "Decrease job training"], "Promote sustained economic growth"),
    ("Which sector is most associated with SDG 8's focus on decent work?", ["Agriculture", "Technology", "Service sector", "All of the above"], "All of the above"),
    ("What is a major challenge in achieving SDG 8?", ["Increased automation and job displacement", "Overpopulation", "Lack of clean water", "Shortage of renewable energy"], "Increased automation and job displacement"),
    ("What is the target year for achieving SDG 8?", ["2025", "2030", "2040", "2050"], "2030"),
    ("Which of the following promotes economic growth in SDG 8?", ["Increasing investments in infrastructure", "Decreasing global trade", "Fewer job opportunities", "Cutting down on green energy projects"], "Increasing investments in infrastructure"),
    ("Which is essential for creating decent work conditions?", ["Job insecurity", "Fair wages and safe working conditions", "High unemployment rates", "Child labor"], "Fair wages and safe working conditions"),
    ("Which of the following contributes to achieving sustainable economic growth?", ["Reduced access to education", "Promotion of entrepreneurship", "Limiting technological innovation", "Increased use of natural resources"], "Promotion of entrepreneurship"),
    ("What is the role of women in SDG 8?", ["Reducing gender equality", "Promoting economic growth through equal employment opportunities", "Limiting job creation", "Decreasing wage gaps"], "Promoting economic growth through equal employment opportunities"),
    ("Which type of economy is crucial for SDG 8’s long-term success?", ["Closed economy", "Digital economy", "Circular economy", "Informal economy"], "Circular economy")
]

# Quiz Questions for SDG 9
sdg_9_questions = [
    ("What is the main goal of SDG 9?", ["Education", "Infrastructure & innovation", "Hunger", "Health"], "Infrastructure & innovation"),
    ("Which is a target of SDG 9?", ["Education", "Innovation", "Hunger", "Climate"], "Innovation"),
    ("What is key for infrastructure development?", ["Fossil fuels", "Sustainable transport", "Emissions", "Deforestation"], "Sustainable transport"),
    ("What role do small industries play?", ["Slow growth", "Contribute to growth", "Increase inequality", "Limit innovation"], "Contribute to growth"),
    ("What supports innovation and industry?", ["Limited tech", "R&D investment", "Education decline", "Trade limits"], "R&D investment"),
    ("What type of infrastructure is key?", ["Coal plants", "Renewable energy", "Roads", "Deforestation"], "Renewable energy"),
    ("What is key to innovation?", ["Limited tech", "Sustainable industry", "Slow progress", "Traditional methods"], "Sustainable industry"),
    ("What is sustainable industrialization?", ["More plastics", "Green tech", "Fossil fuels", "Less transport"], "Green tech"),
    ("Which sector benefits from SDG 9?", ["Health", "Tech", "Mining", "Agriculture"], "Tech"),
    ("How does SDG 9 help growth?", ["Large industries", "Innovation & infrastructure", "Less diversity", "Limited connectivity"], "Innovation & infrastructure")
]

# Quiz Questions for SDG 10
sdg_10_questions = [
    ("What is the main goal of SDG 10?", ["Improve education", "Reduce inequality within and among countries", "End hunger", "Achieve gender equality"], "Reduce inequality within and among countries"),
    ("Which of the following is a key target of SDG 10?", ["Promote fossil fuel use", "Increase income for the bottom 40%", "Limit migration", "Restrict access to education"], "Increase income for the bottom 40%"),
    ("SDG 10 emphasizes the inclusion of which of the following?", ["Only wealthy individuals", "Social, economic, and political inclusion of all people", "Only urban populations", "Only people with higher education"], "Social, economic, and political inclusion of all people")
]
