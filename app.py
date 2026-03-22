import streamlit as st
import requests
from datetime import datetime

# 1. شاردنەوەی هەموو نیشانە زیادەکان و ڕێکخستنی لاپەڕە
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    
    .stApp { background-color: #000; }
    
    .iphone-box {
        text-align: center;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .city-name { font-size: 35px; font-weight: 400; margin-bottom: 0px; }
    .temp-main { font-size: 95px; font-weight: 200; margin: 0px; }
    .condition { font-size: 20px; font-weight: 500; margin-bottom: 5px; }
    .high-low { font-size: 18px; font-weight: 400; margin-bottom: 25px; }
    
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 15px;
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        border: 0.5px solid rgba(255, 255, 255, 0.2);
        margin-top: 20px;
    }
    
    .info-item { text-align: center; font-size: 14px; opacity: 0.9; }
    .info-val { font-size: 18px; font-weight: 600; display: block; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. دانانی باکگراوند بەپێی کات (ڕۆژ یان شەو)
def apply_iphone_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        # وێنەی ڕۆژ (هەوری سپی)
        url = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        # وێنەی شەو (مانگ و ئەستێرە - وەک ئەو وێنەیەی ویستت)
        url = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """, unsafe_allow_html=True)

apply_iphone_bg()

# 3. بەشی گەڕان
city = st.text_input("", placeholder="Search for a city...", label_visibility="collapsed")

if city:
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        weather = res['weather'][0]
        
        st.markdown(f"""
            <div class="iphone-box">
                <p class="city-name">{city.capitalize()}</p>
                <h1 class="temp-main">{curr['temp_C']}°</h1>
                <p class="condition">{curr['weatherDesc'][0]['value']}</p>
                <p class="high-low">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</p>
                
                <div class="info-card">
                    <div class="info-item">🌧 ئەگەری باران<br><span class="info-val">{weather['hourly'][0]['chanceofrain']}%</span></div>
                    <div class="info-item">💧 ڕێژەی شێ<br><span class="info-val">{curr['humidity']}%</span></div>
                    <div class="info-item">💨 خێرایی با<br><span class="info-val">{curr['windspeedKmph']} km/h</span></div>
                    <div class="info-item">📅 ڕۆژ<br><span class="info-val">{datetime.now().strftime('%A')}</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.error("Please enter a valid city name.")
else:
    st.markdown('<div style="text-align:center; color:white; margin-top:150px; font-size:20px; opacity:0.7;">Enter city to see weather</div>', unsafe_allow_html=True)
