import streamlit as st
import requests

# 1. ڕێکخستنی لاپەڕە و شاردنەوەی هەموو نیشانە سەوز و سوورەکان
st.set_page_config(page_title="Weather", layout="centered")

st.markdown("""
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    .stApp {
        background-color: black;
    }
    .weather-info {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 15px rgba(0,0,0,1);
        font-family: 'Segoe UI', sans-serif;
        margin-top: 50px;
    }
    .temp {
        font-size: 110px !important;
        font-weight: 200;
        margin: 0;
    }
    .city-name {
        font-size: 40px;
        font-weight: 400;
        margin-bottom: -20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. فانکشنی باکگراوند (هەوری جوڵاو و ئەستێرە)
def set_bg(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

# وێنەی ئەو هەورە جوڵاوەی کە ویستت (بۆ شەو و ڕۆژ)
moving_clouds_night = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif"
moving_clouds_day = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/cnXvL06uK9Tf8U54fD/giphy.gif"

# 3. سێرچ کردنی شار
city = st.text_input("", placeholder="ناوی شار بنووسە...", label_visibility="collapsed")

if city:
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        temp = curr['temp_C']
        
        # لێرە دیاری دەکەین ئایا ڕۆژە یان شەوە بۆ ئەوەی وێنە جوڵاوەکە بگۆڕدرێت
        import datetime
        hour = datetime.datetime.now().hour
        if 6 <= hour < 18:
            set_bg(moving_clouds_day)
        else:
            set_bg(moving_clouds_night)
            
        st.markdown(f"""
            <div class="weather-info">
                <p class="city-name">{city.capitalize()}</p>
                <h1 class="temp">{temp}°</h1>
                <p style="font-size: 20px;">{curr['weatherDesc'][0]['value']}</p>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.error("ناوی شارەکە بە دروستی بنووسە")
else:
    # وێنەی سەرەتایی (هەمان ئەو وێنە جوڵاوەی ویستت)
    set_bg(moving_clouds_night)
