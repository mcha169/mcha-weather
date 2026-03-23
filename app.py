import streamlit as st
import requests
from datetime import datetime

# 1. شاردنەوەی هەموو شتە زیادەکانی ستریملێت بە شێوەیەکی توند
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    /* لادانی لۆگۆ و تاج و مینیو */
    header, footer, .viewerBadge_container__1QS1n, #stDecoration, .stDeployButton {display:none !important;}
    [data-testid="stStatusWidget"], [data-testid="stToolbar"] {display:none !important;}
    
    .stApp {
        background-color: #000;
        color: white;
    }
    
    /* دیزاینی ناوەڕاست وەک ئایفۆن */
    .weather-main {
        text-align: center;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        margin-top: 30px;
    }
    .city { font-size: 32px; font-weight: 500; margin-bottom: 0; }
    .temp { font-size: 90px; font-weight: 200; margin: -10px 0; }
    .desc { font-size: 20px; opacity: 0.8; }
    .hl { font-size: 18px; font-weight: 400; }
    
    /* کارتی زانیاری خوارەوە */
    .info-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 20px;
        margin-top: 40px;
        display: flex;
        justify-content: space-around;
        border: 0.5px solid rgba(255, 255, 255, 0.1);
    }
    .info-box { text-align: center; }
    .info-label { font-size: 12px; opacity: 0.6; display: block; }
    .info-value { font-size: 16px; font-weight: 600; }

    /* جوانکردنی شوێنی گەڕان */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. فانکشنی باکگراوند (هەور و ئەستێرەکان)
def set_bg():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        bg = "https://w0.peakpx.com/wallpaper/354/660/HD-wallpaper-iphone-ios-15-weather-cloudy-day.jpg"
    else:
        bg = "https://w0.peakpx.com/wallpaper/934/547/HD-wallpaper-weather-iphone-stars.jpg"
    st.markdown(f'<style>.stApp {{ background-image: url("{bg}"); background-size: cover; background-position: center; }}</style>', unsafe_allow_html=True)

set_bg()

# 3. بەشی سێرچ
city = st.text_input("", placeholder="ناوی شار بنووسە...", label_visibility="collapsed")

if city:
    try:
        data = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = data['current_condition'][0]
        weather = data['weather'][0]
        
        # نیشاندانی زانیارییەکان ڕاستەوخۆ بەبێ ئەوەی ئیرۆر بدات
        st.markdown(f"""
            <div class="weather-main">
                <div class="city">{city.capitalize()}</div>
                <div class="temp">{curr['temp_C']}°</div>
                <div class="desc">{curr['weatherDesc'][0]['value']}</div>
                <div class="hl">H:{weather['maxtempC']}°  L:{weather['mintempC']}°</div>
                
                <div class="info-container">
                    <div class="info-box"><span class="info-label">🌧 Rain</span><span class="info-value">{weather['hourly'][0]['chanceofrain']}%</span></div>
                    <div class="info-box"><span class="info-label">💧 Humid</span><span class="info-value">{curr['humidity']}%</span></div>
                    <div class="info-box"><span class="info-label">💨 Wind</span><span class="info-value">{curr['windspeedKmph']}km</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown('<p style="text-align:center; color:red;">ناوی شارەکە بە دروستی بنووسە</p>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align:center; margin-top:100px; opacity:0.5;">Enter City Name</div>', unsafe_allow_html=True)
