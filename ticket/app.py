import streamlit as st
import pandas as pd
import datetime

# Initialize session state for the ticket_dict if it doesn't already exist
if 'ticket_dict' not in st.session_state:
    st.session_state.ticket_dict = {
        'Name': [],
        'Batch': [],
        'Topic': [],
        'Description': [],
        'Time': [],
        'Teacher': [],
        'Solved?': []
    }

# Create a form for submitting tickets
with st.form("Ticket"):
    st.header("Raise a Ticket🎫")
    name = st.text_input("Name", placeholder='ex. Jiwon Shin')
    batch = st.radio(
        "Batch",
        key="visibility",
        options=["1792", '1793']),
    topic = st.selectbox("Topic"
                        , ('Google Sheet', 'SQL',
                           'Looker Studio', 'PowerBI',
                           'Python', 'ML', 'Kaggle', 'Mini-Project',
                           'Pitch', 'Others')
                        , placeholder = 'ex. SQL')
    description = st.text_input("Description", max_chars = 20, placeholder = 'ex. How to use window function with GWZ sales dataset? (Week2 Day5) - 20 chars max')
    time = st.time_input("Time?", value=datetime.datetime.now())

    # Form submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.warning('Your ticket is waiting to be assigned')
        # Append submitted data to session state ticket_dict
        st.session_state.ticket_dict['Name'].append(name)
        st.session_state.ticket_dict['Batch'].append(batch)
        st.session_state.ticket_dict['Topic'].append(topic)
        st.session_state.ticket_dict['Description'].append(description)
        st.session_state.ticket_dict['Time'].append(time.strftime("%H:%M"))
        st.session_state.ticket_dict['Teacher'].append('')  # Placeholder for teacher
        st.session_state.ticket_dict['Solved?'].append(False)

# Convert the session state ticket_dict to a DataFrame
ticket_df = pd.DataFrame(st.session_state.ticket_dict)

# Ensure that the "Solved?" column is explicitly set as a boolean
ticket_df['Solved?'] = ticket_df['Solved?'].astype(bool)


# Editable data table with Selectbox for Teacher and Checkbox for Solved?
edited_ticket_df = st.data_editor(
    ticket_df,
    column_config={
        "Teacher": st.column_config.SelectboxColumn(
            "Teacher",
            options=['Gigi', 'Izzy', 'Dani', 'Tomi', 'Yuqing', 'Leo', 'Andrii'],
        ),
        "Solved?": st.column_config.CheckboxColumn(
            "Solved?"
        ),
    },
    hide_index=True,
)

# Update the session state to reflect any changes made in the UI
st.session_state.ticket_dict['Teacher'] = edited_ticket_df['Teacher'].tolist()
st.session_state.ticket_dict['Solved?'] = edited_ticket_df['Solved?'].tolist()




# ticket_dict = {
#     'Name': [],
#     'Batch': [],
#     'Topic': [],
#     'Description': [],
#     'Time': []
# }


# with st.form("Ticket"):
#     st.header("Raise a Ticket🎫")
#     name = st.text_input("Name", placeholder='ex. Jiwon Shin')
#     batch = st.selectbox("Batch", ('1792', '1793'), placeholder = "ex. 1792")
#     topic = st.selectbox("Topic"
#                         , ('Google Sheet', 'SQL',
#                            'Looker Studio', 'PowerBI',
#                            'Python', 'ML', 'Kaggle', 'Mini-Project',
#                            'Pitch', 'Others')
#                         , placeholder = 'ex. SQL')
#     description = st.text_input("Description", placeholder = 'ex. How to use window function with GWZ sales dataset? (Week2 Day5)')
#     time = st.time_input("Time?", value=datetime.datetime.now())
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         st.write("Your ticket is waiting to be assigned")
#         ticket_dict['Name'].append(name)
#         ticket_dict['Batch'].append(batch)
#         ticket_dict['Topic'].append(topic)
#         ticket_dict['Description'].append(description)
#         ticket_dict['Time'].append(time)

#     ticket_dict = ticket_dict
#         # st.write("name",name, "batch", batch,
#         #          'topic', topic, 'description', description,
#         #          'time', time)

# ticket_df = pd.DataFrame(ticket_dict)
# ticket_df['Teacher'] = [''] * len(ticket_df)
# # teacher_df = pd.DataFrame({'Teacher': ['Izzy', 'Yuqing', 'Dani', 'Tomi', 'Gigi', 'Leo', 'Andrii']})

# st.data_editor(
#         ticket_df,
#         column_config={
#             # "Name": st.column_config.Column(required=True),
#             # "Batch":st.column_config.Column(required=True),
#             # "Topic":st.column_config.Column(required=True),
#             # "Description":st.column_config.Column(required=True),
#             # "Time":st.column_config.Column(required=True),
#             "Teacher": st.column_config.SelectboxColumn(
#                 "Teacher",
#                 options=['Izzy', 'Yuqing', 'Dani', 'Tomi', 'Gigi', 'Leo', 'Andrii'],
#             ),
#         },
#         hide_index=True,
#     )















# Filter DataFrame based on selection



# with col2:
#     st.data_editor(
#         teacher_df,
#         column_config={
#             # "Name": st.column_config.Column(required=True),
#             # "Batch":st.column_config.Column(required=True),
#             # "Topic":st.column_config.Column(required=True),
#             # "Description":st.column_config.Column(required=True),
#             # "Time":st.column_config.Column(required=True),
#             "Teacher": st.column_config.SelectboxColumn(
#                 "Teacher",
#                 help="Teacher will be assigned to you",
#                 options=['Izzy', 'Yuqing', 'Dani', 'Tomi', 'Gigi', 'Leo', 'Andrii'],
#             ),

#         },
#         hide_index=True,
#     )

# with col3:
#     st.write('Ticket solved')

# st.write(ticket_df)


# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.header("Gigi")

# with col2:
#     st.header("Izzy")

# with col3:
#     st.header("Yuqing")

# with col4:
#     st.header("Dani")

# with col5:
#     st.header("Tomi")
