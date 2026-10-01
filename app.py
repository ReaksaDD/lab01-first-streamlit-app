import streamlit as st
import pandas as pd

# page_config must be the first Streamlit command
st.set_page_config(
    page_title="EduRisk Analytics",
    page_icon="🎓",
    layout="centered"
)

# Sample student data
student_df = pd.DataFrame({
    "student_name": ["Dara", "Sophea", "Vuthy", "Malis", "Rithy"],
    "score": [85, 68, 45, 75, 75],
    "attendance": [92, 78, 55, 80, 65]
})

# Sidebar navigation
with st.sidebar:
    selected_page = st.radio(
        "Select Page",
        ["Home", "Student Data", "About"]
    )

# Page logic
if selected_page == "Home":
    st.title("🎓 EduRisk Analytics")
    st.subheader("Student Risk Prediction and Monitoring System")
    st.write("Welcome to your first Streamlit app.")
    st.success("Streamlit is working!")

elif selected_page == "Student Data":
    st.title("Student Data")

    total_students = len(student_df)
    average_score = round(student_df["score"].mean(), 1)
    average_attendance = round(student_df["attendance"].mean(), 1)
    low_score_students = int((student_df["score"] < 70).sum())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Students", total_students)
        st.metric("Average Score", average_score)

    with col2:
        st.metric("Average Attendance", f"{average_attendance}%")
        st.metric("Low Score Students", low_score_students)

    st.dataframe(student_df)

else:
    st.title("About")
    st.write("Lab 1: Environment Setup and First Streamlit App")
    st.write("Course: Web App Development for Data Science (DSE-305)")
    st.write("Project theme: EduRisk Analytics - Student Risk Prediction and Monitoring System")