import streamlit as st
import requests
from datetime import datetime

# 1. شاردنەوەی هەموو نیشانەکان (لۆگۆکەی خوارەوە و دوگمەی ڕاوەشاو)
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    /* شاردنەوەی لۆگۆی ستریملێت و دوگمەی بڵاوکردنەوە لە خوارەوە */
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    
    /* ئەم بەشە ئەو لۆگۆ و تاجەی کە نیشانت داوە لادەبات */
    .stDeployButton {display:none !important;}
    footer {display:none !important;}
    div[data-testid="stToolbar"] {display:none !important;}
    
    .stApp { background-color: #000; }
    
    .iphone-ui {
        text-align: center;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        padding-top: 40px;
    }
    
    .city-name { font-size: 38px; font-weight: 500; margin-bottom: 0px; }
    .temp-main { font-size: 110px; font-weight: 200; margin: -10px 0px; }
    .condition { font-size: 22px; opacity: 0.9; }
    .high-low { font-size: 19px; opacity: 0.8; margin-bottom: 30px; }
    
    /* کارتی زانیاری شەفاف وەک ئایفۆن */
    .info-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 25px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px auto;
        max-width: 350px;
    }
    
    .val { font-size: 20px; font-weight: 600; display: block; }
    .lab { font-size: 13px; opacity: 0.7; }
    </style>
    """, unsafe_allow_html=True)

# 2. باکگراوندی شەو و ڕۆژ
def set_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        url = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        url = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url("{url}"); background-size: cover; background-position: center; }}
        </style>
        """, unsafe_allow_html=True)

set_bg()

# 3. سێرچ و داتا
city = st.text_input("", placeholder="ناوی شار بنووسە...", label_visibility="collapsed")

if city:
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        weather = res['weather'][0]
        
        st.markdown(f"""
            <div class="iphone-ui">
                <div class="city-name">{city.capitalize()}</div>
                <div class="temp-main">{curr['temp_C']}°</div>
                <div class="condition">{curr['weatherDesc'][0]['value']}</div>
                <div class="high-low">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</div>
                
                <div class="info-card">
                    <div><span class="lab">🌧 باران</span><span class="val">{weather['hourly'][0]['chanceofrain']}%</span></div>
                    <div><span class="lab">💧 شێ</span><span class="val">{curr['humidity']}%</span></div>
                    <div><span class="lab">💨 با</span><span class="val">{curr['windspeedKmph']} km/h</span></div>
                    <div><span class="lab">📅 کات</span><span class="val">{datetime.now().strftime('%H:%M')}</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.error("Error!")
else:
    st.markdown('<div style="text-align:center; color:white; margin-top:150px; opacity:0.6;">ناوی شارێک بنووسە</div>', unsafe_allow_html=True)
