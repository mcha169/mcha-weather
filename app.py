import streamlit as st
import requests
from datetime import datetime

# 1. شاردنەوەی لۆگۆ و نیشانە زیادەکان
st.set_page_config(page_title="Weather", layout="centered")
st.markdown("""
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    .stApp { background-color: #000; }
    .main-box {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        font-family: 'Helvetica Neue', sans-serif;
    }
    .temp { font-size: 100px; font-weight: 200; margin: 0; }
    .city { font-size: 40px; margin-bottom: 0; }
    .info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. فانکشنی دیاریکردنی باکگراوندی ڕۆژ و شەو
def set_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        # وێنەی ڕۆژی ڕووناک
        img = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        # وێنەی شەوی ئەستێرە و مانگ (وەک ئەو وێنەیەی ناردت)
        img = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{img}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """, unsafe_allow_html=True)

set_bg()

# 3. بەشی گەڕان و هێنانی زانیاری
city = st.text_input("", placeholder="Erbil...", label_visibility="collapsed")

if city:
    try:
        data = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = data['current_condition'][0]
        weather = data['weather'][0]
        
        temp = curr['temp_C']
        desc = curr['weatherDesc'][0]['value']
        high = weather['maxtempC']
        low = weather['mintempC']
        humidity = curr['humidity']
        wind = curr['windspeedKmph']
        rain_prob = weather['hourly'][0]['chanceofrain']

        st.markdown(f"""
            <div class="main-box">
                <p class="city">{city.capitalize()}</p>
                <h1 class="temp">{temp}°</h1>
                <p style="font-size: 20px;">{desc}</p>
                <p>H:{high}°  L:{low}°</p>
                
                <div class="info-grid">
                    <div>🌧 ئەگەری باران<br><b>{rain_prob}%</b></div>
                    <div>💧 شێ<br><b>{humidity}%</b></div>
                    <div>💨 خێرایی با<br><b>{wind} km/h</b></div>
                    <div>📅 ئەمڕۆ<br><b>{datetime.now().strftime('%A')}</b></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.error("شارەکە نەدۆزرایەوە!")
else:
    st.markdown('<p style="text-align:center; color:white; margin-top:100px;">ناوی شارێک بنووسە بۆ بینینی کەشوهەوا</p>', unsafe_allow_html=True)
