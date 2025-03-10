import streamlit as st
import random
import base64
import os

# Set page config
st.set_page_config(page_title="Number_guessing_game", page_icon="🎮", layout="centered")

# Function to Convert Local Image to Base64
def set_bg(local_img_path):
    if os.path.exists(local_img_path):
        with open(local_img_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(bg_img, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ Background image not found: {local_img_path}")

# Set background image
set_bg("number_game.jpg")

# Custom CSS for orange title and light orange input field
st.markdown(
    """
    <style>

    /* Light orange input field */
    div.stNumberInput > div > div > input {
        background-color: rgba(255, 165, 0, 0.2) !important; /* Light orange background */
        border: 1px solid #FFA500 !important; /* Orange border */
        border-radius: 5px !important;
        # padding: 10px !important;
        color: #FF4500 !important; /* Dark orange text color */
        font-weight: bold !important;
    }

    /* Placeholder text color */
    div.stNumberInput > div > div > input::placeholder {
        color: #FF4500 !important; /* Dark orange placeholder text */
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.markdown(
    """
    <h1 style='text-align: center; background-color: black; opacity: 80%; color: #FF4500; border-radius: 30px;'>
        🎲Random Number Guessing Game <span style='color: white;'>(Computer Vs User)</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# Initialize the random number in session state
if "com_number" not in st.session_state:
    st.session_state.com_number = random.randint(1, 11)

# Get the user's guess
import streamlit as st

# Custom CSS to style the label
st.markdown(
    """
    <style>
    .big-font {
        font-size: 20px !important; /* Adjust the size as needed */
        font-weight: bold;
        color:black !important;
        border-radius:40px;
        background-color:white !important;
        margin-bottom:none;
        margin-top:none;
        display:inline-block;        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the styled label using st.markdown
st.markdown(
    "<p class='big-font'> 🔶 Enter a number between 1 and 11 🔸🔸</p>",
    unsafe_allow_html=True
)

# Use st.number_input without a label
user_input = st.number_input(
    "",  # Empty label
    min_value=1,
    max_value=11,
    step=1
)


if st.button("Submit Guess"):
    if user_input > st.session_state.com_number:
        st.write(f"Computer's number is: {st.session_state.com_number}")
        st.error("Your number is too high! Try again.")
    elif st.session_state.com_number > user_input:
        st.write(f"Computer's number is: {st.session_state.com_number}")
        st.warning("Your number is too low! Try again.")
    else:
        st.write(f"💻 Computer's number is: {st.session_state.com_number}")
        st.success("Congratulations! You guessed the right number.")

        # Reset the game
        if st.button("Play Again"):
            st.session_state.com_number = random.randint(1, 11)
            st.rerun()
# Footer
st.markdown(
    """
    <hr>
    <div style="text-align: center; padding: 10px; font-size: 18px; color: white;">
        © 2025 | Developed by <b style='color:black; font-size:20px; font-weight:bold;'>Sana Faisal
        <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank" style="color: #FF4500; text-decoration:none;">
            🔗 Connect on LinkedIn
        </a>
    </div>
    """,
    unsafe_allow_html=True
)            