# # student_details.py

# import streamlit as st

# # Sample data to mimic a student database (In production, you would fetch this from a database)
# students = []

# def run_student_details_app():
#     st.title("Student Details")

#     # Display student details in a table
#     if students:
#         st.subheader("Existing Student Details")
#         student_data = []
#         for student in students:
#             student_data.append([student['name'], student['usn'], student['roll_no'], student['parents_contact'], student['semester'], student['section'], student['branch']])
#         st.table(student_data)
#     else:
#         st.write("No student details available.")

#     # Add new student details
#     st.subheader("Add New Student")
#     with st.form(key="add_student_form"):
#         name = st.text_input("Name")
#         usn = st.text_input("USN")
#         roll_no = st.text_input("Roll Number")
#         parents_contact = st.text_input("Parents' Contact Number")
#         semester = st.selectbox("Semester", ["1", "2", "3", "4", "5", "6", "7", "8"])
#         section = st.text_input("Section")
#         branch = st.text_input("Branch")
#         submit_button = st.form_submit_button("Add Student")

#         if submit_button:
#             # Create a student dictionary to store
#             new_student = {
#                 "name": name,
#                 "usn": usn,
#                 "roll_no": roll_no,
#                 "parents_contact": parents_contact,
#                 "semester": semester,
#                 "section": section,
#                 "branch": branch
#             }

#             # Add the new student to the list (In production, save to a database)
#             students.append(new_student)
#             st.success("Student added successfully!")
#             st.experimental_rerun()  # Rerun to show the updated student list


import streamlit as st
import pandas as pd

# Sample data to mimic a student database (In production, you would fetch this from a database)
students = []

def run_student_details_app():
    st.title("Student Details")

    # Display student details in a table format (using DataFrame for better visual)
    if students:
        st.subheader("Existing Student Details")
        student_data = []
        for index, student in enumerate(students, 1):
            student_data.append([index, student['name'], student['usn'], student['roll_no'], student['parents_contact'], student['semester'], student['section'], student['branch']])

        # Convert the student data to DataFrame for better table display
        df = pd.DataFrame(student_data, columns=["S.No", "Name", "USN", "Roll No", "Parents' Contact", "Semester", "Section", "Branch"])
        st.dataframe(df)  # Display the DataFrame as a table
    else:
        st.write("No student details available.")

    # Add new student details
    st.subheader("Add New Student")
    with st.form(key="add_student_form"):
        name = st.text_input("Name")
        usn = st.text_input("USN")
        roll_no = st.text_input("Roll Number")
        parents_contact = st.text_input("Parents' Contact Number")
        semester = st.selectbox("Semester", ["1", "2", "3", "4", "5", "6", "7", "8"])
        section = st.text_input("Section")
        branch = st.text_input("Branch")
        submit_button = st.form_submit_button("Add Student")

        if submit_button:
            # Create a student dictionary to store
            new_student = {
                "name": name,
                "usn": usn,
                "roll_no": roll_no,
                "parents_contact": parents_contact,
                "semester": semester,
                "section": section,
                "branch": branch
            }

            # Add the new student to the list (In production, save to a database)
            students.append(new_student)
            st.success("Student added successfully!")
            # Streamlit will automatically rerun after form submission

    # Update existing student details
    st.subheader("Update Student Details")
    if students:
        student_serial_no = st.selectbox("Select Student to Update", [i for i in range(1, len(students)+1)])
        selected_student = students[student_serial_no - 1]  # Indexing starts from 0

        with st.form(key="update_student_form"):
            new_name = st.text_input("Name", selected_student['name'])
            new_usn = st.text_input("USN", selected_student['usn'])
            new_roll_no = st.text_input("Roll Number", selected_student['roll_no'])
            new_parents_contact = st.text_input("Parents' Contact Number", selected_student['parents_contact'])
            new_semester = st.selectbox("Semester", ["1", "2", "3", "4", "5", "6", "7", "8"], index=int(selected_student['semester'])-1)
            new_section = st.text_input("Section", selected_student['section'])
            new_branch = st.text_input("Branch", selected_student['branch'])
            update_button = st.form_submit_button("Update Student")

            if update_button:
                # Update the student details
                students[student_serial_no - 1] = {
                    "name": new_name,
                    "usn": new_usn,
                    "roll_no": new_roll_no,
                    "parents_contact": new_parents_contact,
                    "semester": new_semester,
                    "section": new_section,
                    "branch": new_branch
                }
                st.success(f"Student {student_serial_no} updated successfully!")
                # Streamlit will automatically rerun after form submission

    # Delete student details
    st.subheader("Delete Student")
    if students:
        student_serial_no_delete = st.selectbox("Select Student to Delete", [i for i in range(1, len(students)+1)])
        delete_button = st.button("Delete Selected Student")

        if delete_button:
            # Remove the student from the list
            students.pop(student_serial_no_delete - 1)
            st.success(f"Student {student_serial_no_delete} deleted successfully!")
            # Streamlit will automatically rerun after form submission

if __name__ == "__main__":
    run_student_details_app()
