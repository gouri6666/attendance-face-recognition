# # visual_graph.py

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# def run_analytical_graph_app():
#     st.title("Analytics - Attendance Graph")
    
#     # Example data for plotting
#     dates = ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05"]
#     attendance = [20, 22, 19, 21, 23]  # Example attendance count for each day
    
#     # Plot the attendance data
#     plt.figure(figsize=(10, 6))
#     plt.plot(dates, attendance, marker='o', linestyle='-', color='b', label='Attendance')
#     plt.title("Daily Attendance", fontsize=16)
#     plt.xlabel("Date", fontsize=12)
#     plt.ylabel("Number of Students Present", fontsize=12)
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.tight_layout()

#     # Display the plot using Streamlit
#     st.pyplot(plt)

#     # Display attendance data in a table
#     data = {"Date": dates, "Attendance": attendance}
#     st.write("Attendance Data", data)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch the attendance data from the session state
def get_attendance_data():
    if "attendance_df" not in st.session_state:
        st.error("Attendance data not found. Please ensure that the attendance has been taken.")
        return None
    return st.session_state.attendance_df

# Function to generate attendance graph
def generate_attendance_graph(df):
    # Count present students for each day
    attendance_counts = {date: df[date].value_counts().get("P", 0) for date in df.columns[2:-1]}  # Ignore Name, USN, and Percentage columns
    dates = list(attendance_counts.keys())
    present_counts = list(attendance_counts.values())

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, present_counts, marker='o', color='b', label="Present Students")
    plt.xlabel('Date')
    plt.ylabel('Number of Students Present')
    plt.title('Attendance Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    st.pyplot(plt)

# Main function to render the graph update feature
def run_analytical_graph_app():
    st.title("Attendance Analytics Graph")

    # Fetch the attendance data
    df = get_attendance_data()

    if df is not None:
        # Show the data (optional, just for reference)
        st.write("### Attendance Data", df)

        # Add the "Update Graph" button
        if st.button("Update Graph"):
            st.write("Generating the attendance graph...")
            generate_attendance_graph(df)
        else:
            st.write("Click the 'Update Graph' button to see the attendance graph.")

# Run the app
if __name__ == "__main__":
    run_analytical_graph_app()
