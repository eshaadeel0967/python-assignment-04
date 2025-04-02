import streamlit as st
import random

# Constants
PROMPT = "Enter your name:"  # Prompt message
JOKES = [
    "Why did the stadium get hot after the game? All the fans left!",
    "Why don’t some fish play piano? Because you can’t tuna fish!",
    "Why do cows wear bells? Because their horns don’t work!",
    "Why did the golfer bring an extra pair of pants? In case he got a hole in one!",
    "Why don’t skeletons go to parties? Because they have no body to dance with!",
    "What do you call a belt with a watch on it? A waist of time!",
    "Why was the computer cold? It left its Windows open!",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
    "Why was the broom late? It swept in!",
    "Why did the orange stop? It ran out of juice!",
    "What kind of tea is hard to swallow? Reality!",
    "Why do ducks make great detectives? They always quack the case!",
    "Why do ghosts love elevators? Because they lift their spirits!",
    "Why do bank tellers always seem so calm? Because they know how to balance everything!",
    "Why did the tomato blush? Because it saw the salad dressing!",
    "Why do bicycles fall over? Because they are two-tired!",
    "Why don’t mountains get tired? Because they peak all the time!",
    "Why are frogs so happy? They eat whatever bugs them!",
    "Why did the banana go to the doctor? It wasn’t peeling well!",
    "Why do cats make great singers? Because they are always in purr-fect pitch!"
]
SORRY = "Sorry, I only tell jokes."

# Streamlit UI Enhancements
st.set_page_config(page_title="Joke Bot", page_icon="😂", layout="centered")

st.markdown(
    """
    <style>
    .big-title {
        font-size: 40px;
        font-weight: bold;
        color: #FF5733;
        text-align: center;
    }
    .sub-text {
        font-size: 20px;
        text-align: center;
        color: #666;
    }
    .joke-box {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #333;
        border: 2px solid #FF5733;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='big-title'>😂 Joke Bot 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-text'>Enter your name and I'll make you laugh!</h2>", unsafe_allow_html=True)

# User Input
user_input = st.text_input(PROMPT)
if user_input:
    st.write(f"Hello {user_input}! 😊 What do you want to do?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        joke_btn = st.button("Tell me a Joke 😂", key="joke_btn")
    
    with col2:
        exit_btn = st.button("Exit 🚪", key="exit_btn")

    # Handle Button Clicks
    if joke_btn:
        joke = random.choice(JOKES)
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)
    
    if exit_btn:
        st.warning(f"Goodbye! 👋 {user_input}")
        st.stop()
