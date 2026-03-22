import streamlit as st
import requests
from datetime import datetime

# 1. سڕینەوەی ڕەگ و ڕیشەی هەموو نیشانە و لۆگۆ و دوگمە زیادەکان
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    /* 1. سڕینەوەی لۆگۆی ستریملێت و دوگمەی دیپلۆی و فووتەر */
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    .stDeployButton {display:none !important;}
    div[data-testid="stToolbar"] {display:none !important;}
    iframe[title="Managed Navigation"] {display:none !important;}
    
    /* 2. پاککردنەوەی باکگراوند و ڕەنگی بنچینەیی */
    .stApp { background-color: #000; }
    
    /* 3. دیزاینی مۆدێرنی ئایفۆن (زۆر خاوێن) */
    .iphone-wrapper {
        text-align: center;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
        padding-top: 50px;
    }
    
    .city { font-size: 38px; font-weight: 500; margin-bottom: 0px; text-shadow: 0px 4px 15px rgba(0,0,0,0.4); }
    .temp { font-size: 110px; font-weight: 200; margin: -10px 0px; text-shadow: 0px 4px 20px rgba(0,0,0,0.4); }
    .status { font-size: 22px; font-weight: 400; opacity: 0.9; margin-bottom: 5px; }
    .hl { font-size: 19px; font-weight: 400; opacity: 0.8; margin-bottom: 35px; }
    
    /* 4. کارتی زانیارییەکان (Glassmorphism) */
    .details-grid {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 22px;
        padding: 25px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        max-width: 360px;
        margin: 0 auto;
    }
    
    .detail-item { text-align: center; }
    .detail-label { font-size: 13px; opacity: 0.6; display: block; margin-bottom: 5px; }
    .detail-value { font-size: 19px; font-weight: 600; }

    /* 5. جوانکردنی شوێنی نووسینی شار */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        text-align: center;
        height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. دانانی باکگراوندی ڕاستەقینەی ئایفۆن بەپێی کات
def apply_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        # وێنەی ڕۆژی هەوراوی ئایفۆن
        bg = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        # وێنەی شەوی ئەستێرە و مانگی ئایفۆن
        bg = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url("{bg}"); background-size: cover; background-position: center; }}
        </style>
        """, unsafe_allow_html=True)

apply_bg()

# 3. بەشی گەڕان
city = st.text_input("", placeholder="Search City...", label_visibility="collapsed")

if city:
    try:
        # هێنانی زانیارییەکان
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        weather = res['weather'][0]
        
        st.markdown(f"""
            <div class="iphone-wrapper">
                <div class="city">{city.capitalize()}</div>
                <div class="temp">{curr['temp_C']}°</div>
                <div class="status">{curr['weatherDesc'][0]['value']}</div>
                <div class="hl">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</div>
                
                <div class="details-grid">
                    <div class="detail-item">
                        <span class="detail-label">🌧 Chance of Rain</span>
                        <span class="detail-value">{weather['hourly'][0]['chanceofrain']}%</span>
                    </div>
                    <div class="detail-item">
