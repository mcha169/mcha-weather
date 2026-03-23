import streamlit as st
import requests
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(layout="centered")

# -------------------- HIDE ALL STREAMLIT UI --------------------
st.markdown("""
<style>

/* Hide everything */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
[data-testid="stToolbar"] {display:none !important;}
[data-testid="stDecoration"] {display:none !important;}
[data-testid="stStatusWidget"] {display:none !important;}
[data-testid="stFooter"] {display:none !important;}
[data-testid="stHeader"] {display:none !important;}
button[kind="header"] {display:none !important;}

/* Remove padding */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------- TIME-BASED BACKGROUND --------------------
hour = datetime.now().hour

if 6 <= hour < 18:
    bg = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1920"
else:
    bg = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920"

# -------------------- GLOBAL CSS --------------------
st.markdown(f"""
<style>

html, body, [class*="css"] {{
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: white;
}}

.stApp {{
    background: url("{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* CENTER CONTENT */
.container {{
    text-align: center;
    margin-top: 80px;
}}

/* CITY */
.city {{
    font-size: 42px;
    font-weight: 300;
}}

/* TEMP */
.temp {{
    font-size: 90px;
    font-weight: 200;
    margin-top: -10px;
}}

/* DESCRIPTION */
.desc {{
    font-size: 20px;
    opacity: 0.9;
}}

/* H/L */
.hl {{
    font-size: 18px;
    margin-top: 5px;
    opacity: 0.85;
}}

/* GLASS CARD */
.glass {{
    width: 85%;
    margin: 40px auto;
    padding: 20px;

    background: rgba(255, 255, 255, 0.15);
    border-radius: 25px;

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.2);
}}

/* ROW ITEMS */
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

/* INPUT BOX */
input {{
    background: rgba(255,255,255,0.2) !important;
    border-radius: 10px !important;
    color: white !important;
    text-align: center;
}}

</style>
""", unsafe_allow_html=True)

# -------------------- INPUT --------------------
city = st.text_input("", "Erbil")

# -------------------- WEATHER FUNCTION --------------------
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    return requests.get(url).json()

# -------------------- MAIN APP --------------------
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
        <div class="temp">{temp}°</div>
        <div class="desc">{desc}</div>
        <div class="hl">H:{max_t}°  L:{min_t}°</div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------- GLASS CARD --------------------
    st.markdown(f"""
    <div class="glass">
        <div class="row">
            <span>🌧 ئەگەری باران</span>
            <span>{rain}%</span>
        </div>
        <div class="row">
            <span>💧 شێ</span>
            <span>{humidity}%</span>
        </div>
        <div class="row">
            <span>💨 خێرایی با</span>
            <span>{wind} km/h</span>
