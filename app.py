Import streamlit as st
import requests
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(layout="centered")

# -------------------- EXTREME CSS (HIDE EVERYTHING) --------------------
st.markdown("""
<style>

/* Hide ALL Streamlit UI */
.stDeployButton,
footer,
#stDecoration,
header,
[data-testid="stStatusWidget"],
[data-testid="stFooter"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
#MainMenu {
    display: none !important;
    visibility: hidden !important;
}

/* Extra aggressive removal (new Streamlit versions) */
div[class*="st-emotion-cache"] footer {
    display: none !important;
}
div[data-testid="stFooter"] {
    display: none !important;
    visibility: hidden !important;
}

/* Remove padding */
.block-container {
    padding: 0 !important;
}

/* Remove gaps */
div[data-testid="stVerticalBlock"] {
    gap: 0rem !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------- BACKGROUND --------------------
hour = datetime.now().hour

if 6 <= hour < 18:
    bg = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1920"
else:
    bg = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920"

# -------------------- GLOBAL STYLE --------------------
st.markdown(f"""
<style>

.stApp {{
    background: url("{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: white;
}}

.container {{
    text-align: center;
    margin-top: 90px;
}}

.city {{
    font-size: 42px;
    font-weight: 300;
}}

.temp {{
    font-size: 95px;
    font-weight: 200;
}}

.desc {{
    font-size: 20px;
    opacity: 0.9;
}}

.hl {{
    font-size: 18px;
    opacity: 0.85;
}}

/* Glassmorphism */
.glass {{
    width: 85%;
    margin: 40px auto;
    padding: 20px;
    background: rgba(255,255,255,0.15);
    border-radius: 25px;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.25);
}}

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

</style>
""", unsafe_allow_html=True)

# -------------------- CITY SELECT --------------------
cities = [
    "Erbil", "Sulaymaniyah", "Duhok", "Kirkuk",
    "Baghdad", "Basra",
    "London", "Paris", "New York", "Los Angeles",
    "Dubai", "Istanbul", "Berlin", "Tokyo",
    "Toronto", "Sydney", "Moscow", "Rome"
]

city = st.selectbox("", cities)

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
    max_t = today["maxtempC"]
    min_t = today["mintempC"]

    # FIXED RAIN LOGIC (MAX OF ALL HOURS)
    hourly = today["hourly"]
    rain = max([int(h["chanceofrain"]) for h in hourly])

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
        </div>
    </div>
    """, unsafe_allow_html=True)

except:
    st.markdown("""
    <div style="text-align:center; margin-top:100px;">
        Failed to load weather data.
    </div>
    """, unsafe_allow_html=True)
