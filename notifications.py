# this is the program starts
# import streamlit as st

# def run_notifications_app():
#     st.title("Notifications")

#     # Example form for sending notifications
#     with st.form("notification_form"):
#         student_name = st.text_input("Student Name")
#         parent_contact = st.text_input("Parent Contact Number")
#         notification_message = st.text_area("Notification Message")
#         submitted = st.form_submit_button("Send Notification")

#         if submitted:
#             if student_name and parent_contact and notification_message:
#                 st.success(f"Notification sent to {student_name}'s parents.")
#             else:
#                 st.error("Please fill out all fields.")

#     # Example list of sent notifications
#     st.subheader("Sent Notifications")
#     st.write("Here you can display a list of previously sent notifications.")

################# end of program


# import streamlit as st
# from datetime import date, time
# from twilio.rest import Client

# # Twilio credentials (replace with your actual credentials)
# account_sid = 'your_account_sid'
# auth_token = 'your_auth_token'
# twilio_phone_number = 'your_twilio_phone_number'

# # Sample notification data (can be replaced with database integration)
# notifications = []

# def send_sms_to_parents(parent_phone_number, student_name, selected_date, selected_time):
#     """Send an SMS notification to the parent when a student is absent."""
#     client = Client(account_sid, auth_token)
#     message_body = (
#         f"Dear Parent, your child {student_name} is marked as absent on {selected_date} during {selected_time}."
#     )
#     message = client.messages.create(
#         body=message_body,
#         from_=twilio_phone_number,
#         to=parent_phone_number
#     )
#     st.success(f"Message sent to {parent_phone_number} with SID: {message.sid}")

# def run_notification_app():
#     st.title("Notification Management")

#     # Display notification details in a table
#     st.subheader("Notification Table")
#     if notifications:
#         for idx, notification in enumerate(notifications):
#             col1, col2, col3, col4, col5 = st.columns(5)
#             with col1:
#                 st.write(notification['name'])
#             with col2:
#                 st.write(notification['parents_contact'])
#             with col3:
#                 st.write(notification['date'])
#             with col4:
#                 st.write(notification['time'])
#             with col5:
#                 # Check attendance status and display button
#                 if notification['status'] == 'absent':
#                     if st.button("Send", key=f"send_{idx}", help="Click to send notification", disabled=False):
#                         send_sms_to_parents(
#                             notification['parents_contact'],
#                             notification['name'],
#                             notification['date'],
#                             notification['time']
#                         )
#                         notification['status'] = 'notified'  # Mark as notified
#                 else:
#                     st.button("Send", key=f"send_{idx}", disabled=True, help="Student is present")
#     else:
#         st.write("No notifications available.")

#     # Add new notification
#     st.subheader("Add New Notification")
#     with st.form(key="add_notification_form"):
#         student_name = st.text_input("Student Name")
#         parents_contact = st.text_input("Parents' Contact Number")
#         notification_date = st.date_input("Date", min_value=date.today())
#         notification_time = st.selectbox(
#             "Select Time",
#             ["9:00-9:50", "9:50-11:00", "11:00-11:50", "11:55-12:45", "1:50-2:40", "2:40-3:35", "3:35-4:30"]
#         )
#         attendance_status = st.selectbox("Attendance Status", ["present", "absent"])
#         submit_button = st.form_submit_button("Add Notification")

#         if submit_button:
#             new_notification = {
#                 "name": student_name,
#                 "parents_contact": parents_contact,
#                 "date": str(notification_date),
#                 "time": notification_time,
#                 "status": attendance_status
#             }
#             notifications.append(new_notification)
#             st.success("Notification added successfully!")
#             st.experimental_rerun()

#     # Delete a notification
#     st.subheader("Delete Notification")
#     delete_index = st.number_input(
#         "Enter Notification Serial Number to Delete", min_value=1, max_value=len(notifications), step=1
#     )
#     if st.button("Delete Notification"):
#         notifications.pop(delete_index - 1)
#         st.success("Notification deleted successfully!")
#         st.experimental_rerun()

#     # Update a notification
#     st.subheader("Update Notification")
#     update_index = st.number_input(
#         "Enter Notification Serial Number to Update", min_value=1, max_value=len(notifications), step=1
#     )
#     if st.button("Update Notification"):
#         notification = notifications[update_index - 1]
#         with st.form(key="update_notification_form"):
#             student_name = st.text_input("Student Name", value=notification['name'])
#             parents_contact = st.text_input("Parents' Contact Number", value=notification['parents_contact'])
#             notification_date = st.date_input("Date", value=date.fromisoformat(notification['date']))
#             notification_time = st.selectbox(
#                 "Select Time",
#                 ["9:00-9:50", "9:50-11:00", "11:00-11:50", "11:55-12:45", "1:50-2:40", "2:40-3:35", "3:35-4:30"],
#                 index=["9:00-9:50", "9:50-11:00", "11:00-11:50", "11:55-12:45", "1:50-2:40", "2:40-3:35", "3:35-4:30"]
#                 .index(notification['time'])
#             )
#             attendance_status = st.selectbox(
#                 "Attendance Status", ["present", "absent"], index=["present", "absent"].index(notification['status'])
#             )
#             update_button = st.form_submit_button("Update Notification")

#             if update_button:
#                 notification.update({
#                     "name": student_name,
#                     "parents_contact": parents_contact,
#                     "date": str(notification_date),
#                     "time": notification_time,
#                     "status": attendance_status
#                 })
#                 st.success("Notification updated successfully!")
#                 st.experimental_rerun()

# # Run the Notification Management App
# if __name__ == "__main__":
#     run_notification_app()



# import streamlit as st
# from twilio.rest import Client

# # Twilio credentials
# account_sid = "ACe828c8023a56310a80f11d06eae803b2"  # Replace with your actual Account SID
# auth_token = "bb4cf9f3ddc00ef01ebd5fec7728b5c7"    # Replace with your actual Auth Token
# twilio_phone_number = "+1 231 570 9154"  # Your Twilio phone number
# client = Client(account_sid, auth_token)

# def send_sms(to_number, message):
#     try:
#         message = client.messages.create(
#             to=to_number,
#             from_=twilio_phone_number,
#             body=message
#         )
#         return message.sid
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return None

# # Streamlit Notification Form
# def run_notifications_app():
#     st.title("Notifications")

#     with st.form("notification_form"):
#         student_name = st.text_input("Student Name")
#         parent_contact = st.text_input("Parent Contact Number (e.g., +1234567890)")
#         notification_message = st.text_area("Notification Message")
#         submitted = st.form_submit_button("Send Notification")

#         if submitted:
#             if student_name and parent_contact and notification_message:
#                 message_sid = send_sms(parent_contact, notification_message)
#                 if message_sid:
#                     st.success(f"Notification sent to {student_name}'s parents. Message SID: {message_sid}")
#                 else:
#                     st.error("Failed to send notification.")
#             else:
#                 st.error("Please fill out all fields.")

#     # Example list of sent notifications
#     st.subheader("Sent Notifications")
#     st.write("Here you can display a list of previously sent notifications.")

# if __name__ == "__main__":
#     run_notifications_app()


import streamlit as st
from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    """
    Send an SMS notification using Twilio API.
    Args:
        to_number (str): The recipient's phone number (e.g., "+1234567890").
        message (str): The message to send.

    Returns:
        str: The SID of the sent message if successful, None otherwise.
    """
    try:
        message = client.messages.create(
            to=to_number,
            from_=twilio_phone_number,
            body=message
        )
        return message.sid
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit Notification Form
def run_notifications_app():
    """
    Runs the Streamlit application for sending notifications.
    """
    st.title("Send Notifications to Parents")

    with st.form("notification_form"):
        student_name = st.text_input("Student Name", placeholder="Enter the student's name")
        parent_contact = st.text_input("Parent Contact Number", placeholder="Enter contact number (e.g., +1234567890)")
        notification_message = st.text_area("Notification Message", placeholder="Enter the message to send")
        submitted = st.form_submit_button("Send Notification")

        if submitted:
            if student_name and parent_contact and notification_message:
                # Attempt to send the notification
                message_sid = send_sms(parent_contact, notification_message)
                if message_sid:
                    st.success(f"Notification sent to {student_name}'s parents. Message SID: {message_sid}")
                else:
                    st.error("Failed to send the notification. Check the error message above.")
            else:
                st.error("All fields are required!")

    st.subheader("Notification Logs")
    st.write("In the future, you can implement a database to store and display sent notifications here.")

if __name__ == "__main__":
    run_notifications_app()
