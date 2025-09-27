
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

