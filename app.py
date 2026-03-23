import streamlit as st
import requests
from datetime import datetime

# 1. ڕێکخستنی لاپەڕە و سڕینەوەی هەموو نیشانەکان (تاج، لۆگۆ، مینیو)
st.set_page_config(layout="centered", page_title="Weather App")

st.markdown("""
<style>
/* سڕینەوەی هەموو شتە زیادەکانی ستریملێت */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none !important;}
[data-testid="stToolbar"] {display:none !important;}
[data-testid="stDecoration"] {display:none !important;}
[data-testid="stStatusWidget"] {display:none !important;}
[data-testid="stFooter"] {display:none !important;}
[data-testid="stHeader"] {display:none !important;}

/* لادانی بۆشایی سەرەوە */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* فۆنت و ڕەنگی گشتی */
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 2. دیاریکردنی باکگراوند بەپێی کات (ڕۆژ و شەو)
hour = datetime.now().hour
if 6 <= hour < 18:
    bg = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1920" # ڕۆژ
else:
    bg = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920" # شەو

st.markdown(f"""
<style>
.stApp {{
    background: url("{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* دیزاینی ناوەڕاست */
.container {{
    text-align: center;
    margin-top: 60px;
}}

.city {{ font-size: 42px; font-weight: 300; }}
.temp {{ font-size: 90px; font-weight: 200; margin-top: -10px; }}
.desc {{ font-size: 20px; opacity: 0.9; }}
.hl {{ font-size: 18px; margin-top: 5px; opacity: 0.85; }}

/* کارتی شوشەیی (Glassmorphism) */
.glass {{
    width: 90%;
    margin: 40px auto;
    padding: 20px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 25px;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.2);
}}

.row {{
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    font-size: 18px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
}}
.row:last-child {{ border-bottom: none; }}

/* سندووقی گەڕان */
input {{
    background: rgba(255,255,255,0.2) !important;
    border-radius: 12px !important;
    color: white !important;
    text-align: center;
    border: none !important;
}}
</style>
""", unsafe_allow_html=True)

# 3. بەشی نووسین و گەڕان
city = st.text_input("", "Erbil", label_visibility="collapsed")

try:
    # وەرگرتنی زانیارییەکان
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    
    current = data["current_condition"][0]
    today = data["weather"][0]
    
    # نیشاندانی زانیارییەکان
    st.markdown(f"""
    <div class="container">
        <div class="city">{city.capitalize()}</div>
        <div class="temp">{current["temp_C"]}°</div>
        <div class="desc">{current["weatherDesc"][0]["value"]}</div>
        <div class="hl">H:{today["maxtempC"]}°  L:{today["mintempC"]}°</div>
    </div>
    
    <div class="glass">
        <div class="row">
            <span>🌧 ئەگەری باران</span>
            <span>{today["hourly"][0]["chanceofrain"]}%</span>
        </div>
        <div class="row">
            <span>💧 شێ</span>
            <span>{current["humidity"]}%</span>
        </div>
        <div class="row">
            <span>💨 خێرایی با</span>
            <span>{current["windspeedKmph"]} km/h</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

except:
    st.markdown('<p style="text-align:center;">Error: City not found</p>', unsafe_allow_html=True)
