import streamlit as st
import requests
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Weather App", layout="centered")

# -------------------- HIDE STREAMLIT UI --------------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------- GET TIME FOR BACKGROUND --------------------
hour = datetime.now().hour

if 6 <= hour < 18:
    bg_image = "https://images.unsplash.com/photo-1501973801540-537f08ccae7b"
else:
    bg_image = "https://images.unsplash.com/photo-1501785888041-af3ef285b470"

# -------------------- CUSTOM CSS (GLASSMORPHISM + IOS STYLE) --------------------
st.markdown(f"""
<style>

body {{
    background-image: url('{bg_image}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.main {{
    background: transparent;
}}

.center {{
    text-align: center;
    color: white;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
}}

.temp {{
    font-size: 80px;
    font-weight: 200;
}}

.city {{
    font-size: 40px;
    font-weight: 300;
}}

.desc {{
    font-size: 22px;
    margin-bottom: 20px;
}}

.glass {{
    background: rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    color: white;
    margin-top: 20px;
}}

.row {{
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
    font-size: 18px;
}}

input {{
    background-color: rgba(255,255,255,0.2) !important;
    color: white !important;
}}

</style>
""", unsafe_allow_html=True)

# -------------------- CITY INPUT --------------------
city = st.text_input("Enter city (in English):", "Erbil")

# -------------------- FETCH WEATHER --------------------
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()
    return data

try:
    data = get_weather(city)

    current = data["current_condition"][0]
    weather = data["weather"][0]

    temp = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind = current["windspeedKmph"]
    chance_rain = weather["hourly"][0]["chanceofrain"]
    max_temp = weather["maxtempC"]
    min_temp = weather["mintempC"]

    # -------------------- MAIN UI --------------------
    st.markdown(f"""
    <div class="center">
        <div class="city">{city}</div>
        <div class="temp">{temp}°</div>
        <div class="desc">{desc}</div>
        <div class="desc">H:{max_temp}°  L:{min_temp}°</div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------- GLASS CARD --------------------
    st.markdown(f"""
    <div class="glass">
        <div class="row">
            <span>🌧 باران</span>
            <span>{chance_rain}%</span>
        </div>
        <div class="row">
            <span>💧 شڵەیی</span>
            <span>{humidity}%</span>
        </div>
        <div class="row">
            <span>🌬 با</span>
            <span>{wind} km/h</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

except:
    st.error("Could not fetch weather data. Try another city.")
