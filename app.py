import streamlit as st
import requests

# 1. ڕێکخستنی لاپەڕە و شاردنەوەی هەموو لۆگۆ زیادەکان
st.set_page_config(page_title="M C H A Weather", page_icon="🌤️", layout="centered")

hide_all_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QS1n {display: none !important;}
    #stDecoration {display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    </style>
    """
st.markdown(hide_all_style, unsafe_allow_html=True)

# 2. فانکشنی باکگراوند
def set_bg(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .weather-card {{
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 20px;
            color: white;
            text-align: center;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 10px;
        }}
        .mcha-title {{
            font-size: 80px !important;
            font-weight: 900;
            text-align: center;
            color: #FFD700;
            text-shadow: 4px 4px 15px black;
            margin-bottom: -10px;
        }}
        </style>
        """, unsafe_allow_html=True)

# 3. فانکشنی وێنەی جوڵاو
def get_weather_gif(desc):
    desc = desc.lower()
    if "rain" in desc or "drizzle" in desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/t7Qb8655Z1VfBGr5XB/giphy.gif"
    elif "cloud" in desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/cnXvL06uK9Tf8U54fD/giphy.gif"
    elif "snow" in desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKQuYm7908t3I9W/giphy.gif"
    return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/0hNftA9q66y3Xq8BfH/giphy.gif"

# 4. نیشاندانی ناونیشان
st.markdown('<p class="mcha-title">M C H A</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-size:20px;">دیزاینەری کەشوهەوا</p>', unsafe_allow_html=True)

city = st.text_input("", placeholder="ناوی شار بنووسە... (بۆ نموونە: Erbil)")

if city:
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        
        temp = curr['temp_C']
        feels_like = curr['FeelsLikeC']
        desc = curr['weatherDesc'][0]['value']
        humidity = curr['humidity']
        wind = curr['windspeedKmph']
        
        set_bg(get_weather_gif(desc))
        
        # نیشاندانی زانیارییەکان وەک مۆبایل
        st.markdown(f"""
            <div class="weather-card">
                <h1 style="font-size: 70px; margin:0;">{temp}°C</h1>
                <p style="font-size: 25px;">{desc}</p>
                <p>هەستپێکراو: {feels_like}°C</p>
            </div>
            <div style="display: flex; justify-content: space-around;">
                <div class="weather-card" style="width: 45%;"> 💨 با <br> {wind} km/h</div>
                <div class="weather-card" style="width: 45%;"> 💧 شێ <br> {humidity}%</div>
            </div>
        """, unsafe_allow_html=True)
        
    except:
        st.error("شارەکە نەدۆزرایەوە!")
else:
    set_bg("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/u01ioCe6G8URG/giphy.gif")
