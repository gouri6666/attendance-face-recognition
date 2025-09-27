import streamlit as st
import pandas as pd
import cv2
import face_recognition
from datetime import datetime
import calendar
from io import BytesIO
import time 

# -------------------------
# 1. Load Known Faces
# -------------------------
@st.cache_data
def load_known_faces():
    known_faces = []  # List of known face encodings
    known_names = []  # Corresponding names of known faces

    # Example: Load images and encode them
    image_files = ["student.jpg"]  # Replace with your student image paths
    names = ["virat"]  # Replace with your student names

    for file, name in zip(image_files, names):
        img = face_recognition.load_image_file(file)
        encoding = face_recognition.face_encodings(img)[0]
        known_faces.append(encoding)
        known_names.append(name)

    return known_faces, known_names

known_faces, known_names = load_known_faces()

# -------------------------
# 2. Generate Dynamic Attendance Table for Selected Month
# -------------------------
def generate_attendance_table(year, month):
    _, days_in_month = calendar.monthrange(year, month)
    dates = [datetime(year, month, day).strftime('%a, %d') for day in range(1, days_in_month + 1)]
    columns = ['Name', 'USN'] + dates + ['Percentage']

    # Create an empty DataFrame for attendance
    df = pd.DataFrame(columns=columns)

    return df

# -------------------------
# # 3. Take Attendance using Face Recognition
# # -------------------------


import cv2
import face_recognition
import streamlit as st
from datetime import datetime
import time  # Import time module

def take_attendance(df, known_faces, known_names):
    st.write("Opening camera...")

    # Open camera feed
    video_capture = cv2.VideoCapture(0)

    present_students = []
    unknown_detected = False  # Flag to track unknown person detection

    capture_duration = 10  # Time in seconds for how long the camera should stay open
    start_time = time.time()  # Start tracking time

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert frame to RGB (required for face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces and encode them
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.6)
            name = "Unknown"  # Default name if no match is found

            if True in matches:
                matched_index = matches.index(True)
                name = known_names[matched_index]

                if name not in present_students:
                    present_students.append(name)
                    st.success(f"{name} is marked present!")
            else:
                # Handle unknown faces (display message only once)
                if not unknown_detected:
                    st.warning("Unknown person detected!")
                    unknown_detected = True  # Set flag so it doesn't repeat

        # Display the camera feed
        cv2.imshow('Video', frame)

        # Check if time duration is over
        elapsed_time = time.time() - start_time
        if elapsed_time > capture_duration:
            st.info("Camera capture time completed.")
            break

        # Stop if 'q' is pressed manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release camera and close window
    video_capture.release()
    cv2.destroyAllWindows()

    # Ensure today's date matches the column format in the DataFrame
    today = datetime.now().strftime('%a, %d')  # Example: "Mon, 01"

    # Mark attendance in the DataFrame
    for student in present_students:
        df.loc[df['Name'] == student, today] = "P"  # Mark 'P' for Present

    return df


# -------------------------
# 4. Generate and Download Excel File
# -------------------------
def to_excel(df):
    # Convert DataFrame to Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Attendance")
    output.seek(0)
    return output

# -------------------------
# 5. Main Attendance App Function
# -------------------------
def run_attendance_app():
    st.title("Face Recognition Attendance System")

    # Select Year and Month
    year = st.selectbox("Select Year", [datetime.now().year - 1, datetime.now().year, datetime.now().year + 1])
    month = st.selectbox("Select Month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    # Load or generate attendance sheet based on selected year and month
    if "attendance_df" not in st.session_state or st.session_state.selected_year != year or st.session_state.selected_month != month:
        st.session_state.attendance_df = generate_attendance_table(year, month)
        st.session_state.selected_year = year
        st.session_state.selected_month = month

    df = st.session_state.attendance_df

    # Display editable attendance table
    st.write("### Attendance Table")

    # Add Student Form
    with st.form("add_student_form"):
        new_name = st.text_input("Enter Student Name")
        new_usn = st.text_input("Enter USN")
        
        submit_add = st.form_submit_button("Add Student")
        if submit_add:
            # Add new student to the DataFrame
            new_row = pd.Series([new_name, new_usn] + ['' for _ in range(len(df.columns) - 3)] + [0], index=df.columns)
            # Use pd.concat to append the new row
            df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
            st.session_state.attendance_df = df

    # Delete Student Form
    with st.form("delete_student_form"):
        student_names = df['Name'].tolist()
        student_to_delete = st.selectbox("Select Student to Delete", student_names)
        
        submit_delete = st.form_submit_button("Delete Student")
        if submit_delete:
            # Ensure the student exists before attempting to delete
            if student_to_delete in df['Name'].values:
                df = df[df['Name'] != student_to_delete]
                st.session_state.attendance_df = df
                st.success(f"Student {student_to_delete} has been deleted.")
            else:
                st.error(f"Student {student_to_delete} not found.")

    # Update Student Form
    with st.form("update_student_form"):
        student_names = df['Name'].tolist()
        student_to_update = st.selectbox("Select Student to Update", student_names)

        submit_update = st.form_submit_button("Update Student")
        if submit_update and student_to_update:
            # Get the current details of the selected student
            current_row = df[df['Name'] == student_to_update].iloc[0]
            updated_name = st.text_input("Update Student Name", value=current_row['Name'])
            updated_usn = st.text_input("Update USN", value=current_row['USN'])

            # Update the student details in the DataFrame
            df.loc[df['Name'] == student_to_update, 'Name'] = updated_name
            df.loc[df['Name'] == student_to_update, 'USN'] = updated_usn
            st.session_state.attendance_df = df
            st.success(f"Student {student_to_update} has been updated.")
        else:
            if submit_update and not student_to_update:
                st.warning("Please select a student to update.")

    # Display the editable table with attendance marks
    edited_df = df.copy()

    # Set cell color for "P" (Present) and "A" (Absent)
    for date in edited_df.columns[2:-1]:  # Skip 'Name', 'USN' and 'Percentage'
        edited_df[date] = edited_df[date].apply(lambda x: "P" if x == "P" else "A")

    # Calculate the percentage
    def calculate_percentage(row):
        total_days = len(row) - 3  # Exclude Name, USN, and Percentage columns
        present_days = (row[2:-1] == "P").sum()  # Count how many "P" (Present)
        percentage = (present_days / total_days) * 100 if total_days > 0 else 0  # Avoid division by 0
        return f"{percentage:.2f}%" 

    # Calculate the percentage for each student
    edited_df['Percentage'] = edited_df.apply(calculate_percentage, axis=1)

    # Display the updated table
    st.write("### Updated Attendance Table")
    st.dataframe(edited_df)

    # Take attendance button
    if st.button("Take Attendance"):
        updated_df = take_attendance(edited_df, known_faces, known_names)
        st.session_state.attendance_df = updated_df
        st.write("### Updated Attendance Table")
        st.dataframe(updated_df)

    # Reload button to recalculate the percentage after taking attendance
    if st.button("Reload Table and Recalculate Percentages"):
        # Recalculate the percentage after attendance is updated
        st.session_state.attendance_df = edited_df
        st.write("### Attendance Table with Updated Percentages")
        st.dataframe(edited_df)

    # -------------------------
    # Add Excel Download Button
    # -------------------------
    if st.button("Download Excel"):
        excel_file = to_excel(edited_df)
        st.download_button(
            label="Download Excel File",
            data=excel_file,
            file_name="attendance.xlsx",
            mime="application/vnd.ms-excel"
        )

# -------------------------
# 6. Run the app
# -------------------------
if __name__ == "__main__":
    run_attendance_app()