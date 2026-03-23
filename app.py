import streamlit as st
import requests
from datetime import datetime

# 1. ڕێکخستنی لاپەڕە و سڕینەوەی هەموو نیشانە و لۆگۆ زیادەکان
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    /* سڕینەوەی لۆگۆی ستریملێت، دوگمەی دیپلۆی، و هەموو شتە زیادەکانی خوارەوە */
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    .stDeployButton {display:none !important;}
    div[data-testid="stToolbar"] {display:none !important;}
    iframe[title="Managed Navigation"] {display:none !important;}
    
    /* ڕەنگی ڕەشی بنچینەیی */
    .stApp { background-color: #000; }
    
    /* دیزاینی ناوەوە وەک ئایفۆن */
    .iphone-container {
        text-align: center;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
        padding-top: 30px;
    }
    
    .city-name { font-size: 38px; font-weight: 500; margin-bottom: 0px; text-shadow: 0px 4px 10px rgba(0,0,0,0.5); }
    .temp-value { font-size: 110px; font-weight: 200; margin: -15px 0px; text-shadow: 0px 4px 20px rgba(0,0,0,0.5); }
    .description { font-size: 22px; opacity: 0.9; font-weight: 400; }
    .hi-lo { font-size: 19px; opacity: 0.8; margin-bottom: 30px; }
    
    /* کارتی زانیارییەکان (Glassmorphism) */
    .details-box {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 22px;
        padding: 25px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        max-width: 380px;
        margin: 20px auto;
    }
    
    .info-item { text-align: center; }
    .info-label { font-size: 13px; opacity: 0.6; display: block; margin-bottom: 4px; }
    .info-val { font-size: 19px; font-weight: 600; }

    /* ستایلی سێرچ */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        text-align: center;
        height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. فانکشنی باکگراوند بۆ شەو و ڕۆژ
def apply_iphone_style():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        # وێنەی ڕۆژی هەوراوی ئایفۆن
        bg_url = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        # وێنەی شەوی ئەستێرە و مانگی ئایفۆن
        bg_url = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url("{bg_url}"); background-size: cover; background-position: center; }}
        </style>
        """, unsafe_allow_html=True)

apply_iphone_style()

# 3. بەشی گەڕان بۆ شارەکان
city = st.text_input("", placeholder="ناوی شار بنووسە... (بۆ نموونە: Erbil)", label_visibility="collapsed")

if city:
    try:
        # وەرگرتنی زانیاری کەشوهەوا
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        weather = res['weather'][0]
        
        # نیشاندانی زانیارییەکان بە ستایلی ئایفۆن
        st.markdown(f"""
            <div class="iphone-container">
                <div class="city-name">{city.capitalize()}</div>
                <div class="temp-value">{curr['temp_C']}°</div>
                <div class="description">{curr['weatherDesc'][0]['value']}</div>
                <div class="hi-low">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</div>
                
                <div class="details-box">
                    <div class="info-item">
                        <span class="info-label">🌧 باران</span>
                        <span class="info-val">{weather['hourly'][0]['chanceofrain']}%</span>
                    </div>
                    <div class="info-item">
