import streamlit as st
import requests
from datetime import datetime

# 1. شاردنەوەی هەموو نیشانە و لۆگۆ زیادەکان (بە شێوەیەکی توند)
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"], .stDeployButton, div[data-testid="stToolbar"] {display:none !important;}
    
    .stApp { background-color: #000; }
    
    .iphone-ui {
        text-align: center;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
        padding-top: 20px;
    }
    
    .city-name { font-size: 35px; font-weight: 400; margin-bottom: 0px; }
    .temp-val { font-size: 95px; font-weight: 100; margin: -10px 0px; }
    .condition { font-size: 20px; opacity: 0.9; }
    .hi-lo { font-size: 18px; opacity: 0.8; margin-bottom: 30px; }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        max-width: 350px;
        margin: 20px auto;
    }
    
    .item-val { font-size: 18px; font-weight: 600; display: block; }
    .item-label { font-size: 12px; opacity: 0.6; }
    </style>
    """, unsafe_allow_html=True)

# 2. دانانی باکگراوند
def apply_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        url = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        url = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    st.markdown(f'<style>.stApp {{ background-image: url("{url}"); background-size: cover; }}</style>', unsafe_allow_html=True)

apply_bg()

# 3. سێرچ و وەرگرتنی داتا
city = st.text_input("", placeholder="Search City...", label_visibility="collapsed")

if city:
    try:
        # بەکارهێنانی لینکێکی جێگیرتر بۆ داتا
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url, timeout=10).json()
        curr = res['current_condition'][0]
        weather = res['weather'][0]
        
        st.markdown(f"""
            <div class="iphone-ui">
                <div class="city-name">{city.capitalize()}</div>
                <div class="temp-val">{curr['temp_C']}°</div>
                <div class="condition">{curr['weatherDesc'][0]['value']}</div>
                <div class="hi-lo">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</div>
                
                <div class="glass-card">
                    <div><span class="item-label">🌧 Chance of Rain</span><span class="item-val">{weather['hourly'][0]['chanceofrain']}%</span></div>
                    <div><span class="item-label">💧 Humidity</span><span class="item-val">{curr['humidity']}%</span></div>
                    <div><span class="item-label">💨 Wind Speed</span><span class="item-val">{curr['windspeedKmph']} km/h</span></div>
                    <div><span class="item-label">📅 Updated</span><span class="item-val">{datetime.now().strftime('%H:%M')}</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: تکایە ناوی شارەکە بە ئینگلیزی بنووسە")
else:
    st.markdown('<div style="text-align:center; color:white; margin-top:150px; opacity:0.6;">Search for a city...</div>', unsafe_allow_html=True)
