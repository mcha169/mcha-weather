import streamlit as st
import requests
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(layout="centered")

# -------------------- FORCE HIDE ALL STREAMLIT UI --------------------
st.markdown("""
<style>

/* EXTREME CLEAN MODE */
.stDeployButton {display:none !important; visibility:hidden !important;}
footer {display:none !important; visibility:hidden !important;}
#stDecoration {display:none !important; visibility:hidden !important;}
header {display:none !important; visibility:hidden !important;}
[data-testid="stStatusWidget"] {display:none !important; visibility:hidden !important;}
[data-testid="stToolbar"] {display:none !important; visibility:hidden !important;}
[data-testid="stHeader"] {display:none !important; visibility:hidden !important;}
[data-testid="stFooter"] {display:none !important; visibility:hidden !important;}
button[kind="header"] {display:none !important; visibility:hidden !important;}
#MainMenu {display:none !important; visibility:hidden !important;}

/* Remove padding */
.block-container {
    padding: 0 !important;
}

/* Remove extra spacing */
div[data-testid="stVerticalBlock"] {
    gap: 0rem !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------- TIME-BASED BACKGROUND --------------------
hour = datetime.now().hour

if 6 <= hour < 18:
    bg = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1920"
else:
    bg = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920"

# -------------------- GLOBAL STYLE --------------------
st.markdown(f"""
<style>

html, body {{
    margin: 0;
    padding: 0;
}}

.stApp {{
    background: url("{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: white;
}}

/* MAIN CONTAINER */
.container {{
    text-align: center;
    margin-top: 90px;
}}

/* TEXT STYLES */
.city {{
    font-size: 42px;
    font-weight: 300;
}}

.temp {{
    font-size: 95px;
    font-weight: 200;
    margin-top: -10px;
}}

.desc {{
    font-size: 20px;
    opacity: 0.9;
}}

.hl {{
    font-size: 18px;
    opacity: 0.85;
    margin-top: 5px;
}}

/* GLASS EFFECT */
.glass {{
    width: 85%;
    margin: 40px auto;
    padding: 20px;

    background: rgba(255, 255, 255, 0.15);
    border-radius: 25px;

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.25);
}}

/* ROW */
.row {{
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    font-size: 18px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
}}

.row:last-child {{
    border-bottom: none;
}}

/* SELECTBOX STYLING */
div[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.2) !important;
    border-radius: 12px !important;
    color: white !important;
    text-align: center;
}}

</style>
""", unsafe_allow_html=True)

# -------------------- CITY LIST (AUTOCOMPLETE) --------------------
cities = [
    "Erbil", "Sulaymaniyah", "Duhok", "Kirkuk",
    "Baghdad", "Basra",
    "London", "Paris", "New York", "Los Angeles",
    "Dubai", "Istanbul", "Berlin", "Tokyo",
    "Toronto", "Sydney", "Moscow", "Rome"
]

city = st.selectbox("", cities, index=0)

# -------------------- WEATHER FUNCTION --------------------
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    return requests.get(url).json()

# -------------------- FETCH DATA --------------------
try:
    data = get_weather(city)

    current = data["current_condition"][0]
    today = data["weather"][0]

    temp = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind = current["windspeedKmph"]
    rain = today["hourly"][0]["chanceofrain"]
    max_t = today["maxtempC"]
    min_t = today["mintempC"]

    # -------------------- MAIN DISPLAY --------------------
    st.markdown(f"""
    <div class="container">
        <div class="city">{city}</div>
