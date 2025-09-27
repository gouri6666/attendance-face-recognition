
# import streamlit as st
# from attendance import run_attendance_app
# from student_details import run_student_details_app
# from notifications import run_notifications_app
# from academic_calendar import run_timetable_calendar_app
# from analytical_graph import run_analytical_graph_app
# from firebase_database import mark_attendance, get_attendance, get_attendance_by_date


# # Function to render the main dashboard
# def main_dashboard():
#     # Check if the user is logged in
#     if "logged_in" not in st.session_state or not st.session_state.logged_in:
#         st.write("Please login first!")
#     else:
#         # Display a welcome message
#         st.write(f"Welcome to the Student Attendance System Dashboard, {st.session_state.username}!")

#         # Sidebar navigation options
#         pages = ["Attendance", "Student Details", "Notifications", "Analytics", "Timetable and Calendar"]
#         page = st.sidebar.selectbox("Select a section", pages)

#         # Render the selected page
#         if page == "Attendance":
#             run_attendance_app()  # Function from attendance.py for attendance
#         elif page == "Student Details":
#             run_student_details_app()  # Function from student_details.py for student details
#         elif page == "Notifications":
#             run_notifications_app()  # Function from notifications.py for notifications
#         elif page == "Analytics":
#             run_analytical_graph_app()  # Function from analytical_graph.py for analytics and graphs
#         elif page == "Timetable and Calendar":
#             run_timetable_calendar_app()  # Function from academic_calendar.py for timetable/calendar

# # Run the main dashboard
# if __name__ == "__main__":
#     main_dashboard()

# main_dashboard.py

# import streamlit as st
# from attendance import attendance_app

# #from attendance import run_attendance_app
# from student_details import run_student_details_app
# from notifications import run_notifications_app
# from academic_calendar import run_timetable_calendar_app
# from analytical_graph import run_analytical_graph_app
# #from firebase_database import mark_attendance, get_attendance, get_attendance_by_date


# # Function to render the main dashboard
# def main_dashboard():
#     # Check if the user is logged in
#     if "logged_in" not in st.session_state or not st.session_state.logged_in:
#         st.write("Please login first!")
#     else:
#         # Display a welcome message
#         st.write(f"Welcome to the Student Attendance System Dashboard, {st.session_state.username}!")

#         # Sidebar navigation options
#         pages = ["Attendance", "Student Details", "Notifications", "Analytics", "Timetable and Calendar"]
#         page = st.sidebar.selectbox("Select a section", pages)

#         # Render the selected page
#         if page == "Attendance":
#             run_attendance_app()  # Function from attendance.py for attendance
#         elif page == "Student Details":
#             run_student_details_app()  # Function from student_details.py for student details
#         elif page == "Notifications":
#             run_notifications_app()  # Function from notifications.py for notifications
#         elif page == "Analytics":
#             run_analytical_graph_app()  # Function from analytical_graph.py for analytics and graphs
#         elif page == "Timetable and Calendar":
#             run_timetable_calendar_app()  # Function from academic_calendar.py for timetable/calendar

# # Run the main dashboard
# if __name__ == "__main__":
#     main_dashboard()

import streamlit as st

from attendance import run_attendance_app

# Now you can call attendance_app() when needed

  
#from attendance import attendance_app
from student_details import run_student_details_app
from notifications import run_notifications_app
from academic_calendar import run_timetable_calendar_app
from analytical_graph import run_analytical_graph_app

# Function to render the main dashboard
def main_dashboard():
    # Check if the user is logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.write("Please login first!")
    else:
        # Display a welcome message
        st.write(f"Welcome to the Student Attendance System Dashboard, {st.session_state.username}!")

        # Sidebar navigation options
        pages = ["Attendance", "Student Details", "Notifications", "Analytics", "Timetable and Calendar"]
        page = st.sidebar.selectbox("Select a section", pages)

        # Render the selected page
        if page == "Attendance":
            run_attendance_app()  # Function from attendance.py for attendance
        elif page == "Student Details":
            run_student_details_app()  # Function from student_details.py for student details
        elif page == "Notifications":
            run_notifications_app()  # Function from notifications.py for notifications
        elif page == "Analytics":
            run_analytical_graph_app()  # Function from analytical_graph.py for analytics and graphs
        elif page == "Timetable and Calendar":
            run_timetable_calendar_app()  # Function from academic_calendar.py for timetable/calendar

# Run the main dashboard
if __name__ == "__main__":
    main_dashboard()


