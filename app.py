import streamlit as st
import requests
from datetime import datetime

# 1. ڕێکخستنی لاپەڕە
st.set_page_config(layout="centered", page_title="Weather App")

# 2. شاردنەوەی هەموو نیشانە زیادەکان
st.markdown("""
<style>
header, footer, #MainMenu { display: none !important; visibility: hidden !important; }
.stDeployButton { display: none !important; visibility: hidden !important; }
#stDecoration { display: none !important; visibility: hidden !important; }
[data-testid="stStatusWidget"] { display: none !important; visibility: hidden !important; }
div[data-testid="stFooter"] { display: none !important; }
.block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# 3. باکگراوند
hour = datetime.now().hour
bg = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1920" if 6 <= hour < 18 else "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920"

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
.container {{ text-align: center; margin-top: 90px; }}
.city {{ font-size: 42px; font-weight: 300; }}
.temp {{ font-size: 95px; font-weight: 200; }}
.desc {{ font-size: 20px; opacity: 0.9; }}
.hl {{ font-size: 18px; opacity: 0.85; }}
.glass {{
    width: 85%; margin: 40px auto; padding: 20px;
    background: rgba(255,255,255,0.15); border-radius: 25px;
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.25);
}}
.row {{ display: flex; justify-content: space-between; padding: 12px 0; font-size: 18px; border-bottom: 1px solid rgba(255,255,255,0.15); }}
.row:last-child {{ border-bottom: none; }}
</style>
""", unsafe_allow_html=True)

# 4. سێرچ
cities = ["Erbil", "Sulaymaniyah", "Duhok", "Kirkuk", "Halabja", "Baghdad", "London", "Paris", "New York", "Dubai", "Istanbul"]
city = st.selectbox("", cities)

# 5. وەرگرتنی داتا
try:
    res = requests.get(f"https://wttr.in/{city}?format=j1").json()
    curr = res["current_condition"][0]
    today = res["weather"][0]
    
    rain = max([int(h["chanceofrain"]) for h in today["hourly"]])

    st.markdown(f"""
    <div class="container">
        <div class="city">{city}</div>
        <div class="temp">{curr["temp_C"]}°</div>
        <div class="desc">{curr["weatherDesc"][0]["value"]}</div>
        <div class="hl">H:{today["maxtempC"]}°  L:{today["mintempC"]}°</div>
    </div>
    <div class="glass">
        <div class="row"><span>🌧 ئەگەری باران</span><span>{rain}%</span></div>
        <div class="row"><span>💧 شێ</span><span>{curr["humidity"]}%</span></div>
        <div class="row"><span>💨 خێرایی با</span><span>{curr["windspeedKmph"]} km/h</span></div>
    </div>
    """, unsafe_allow_html=True)
except:
    st.markdown('<div style="text-align:center; margin-top:100px;">Loading data...</div>', unsafe_allow_html=True)
