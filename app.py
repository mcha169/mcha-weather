import streamlit as st
import requests

# 1. شاردنەوەی هەموو نیشانە و لۆگۆ زیادەکان
st.set_page_config(page_title="Weather", layout="centered")

hide_style = """
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    .stApp {
        background-color: #111;
    }
    /* ستایلی نووسینەکان وەک مۆبایل */
    .weather-container {
        text-align: center;
        color: white;
        margin-top: -50px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .city-text { font-size: 35px; font-weight: 400; margin-bottom: 0px; }
    .temp-text { font-size: 90px; font-weight: 200; margin-top: -10px; margin-bottom: 0px; }
    .desc-text { font-size: 20px; font-weight: 400; opacity: 0.9; }
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 2. فانکشنی باکگراوندی جوڵاو (ڕێک وەک وێنەکەی جەنابت)
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

# 3. بەشی گەڕان (بە شێوەیەکی تەنک و جوان)
city = st.text_input("", placeholder="ناوی شار بنووسە... (بۆ نموونە: Erbil)", label_visibility="collapsed")

if city:
    try:
        # هێنانی زانیارییەکان
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        temp = curr['temp_C']
        desc = curr['weatherDesc'][0]['value']
        
        # دیاریکردنی وێنەی پشتەوە (هەور و ئەستێرە بۆ شەو، هەور و تیشک بۆ ڕۆژ)
        import datetime
        hour = datetime.datetime.now().hour
        if 6 <= hour < 18:
            # وێنەی ڕۆژ
            bg_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/cnXvL06uK9Tf8U54fD/giphy.gif"
        else:
            # وێنەی شەو (ئەو وێنەیەی ویستت)
            bg_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif"
        
        set_bg(bg_url)
        
        # نیشاندانی زانیارییەکان وەک iPhone
        st.markdown(f"""
            <div class="weather-container">
                <p class="city-text">{city.capitalize()}</p>
                <h1 class="temp-text">{temp}°</h1>
                <p class="desc-text">{desc}</p>
            </div>
        """, unsafe_allow_html=True)
        
    except:
        st.error("ناوی شارەکە دروست نییە!")
else:
    # وێنەی سەرەتایی پێش سێرچ کردن
    set_bg("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif")
    st.markdown('<p style="text-align:center; color:gray; margin-top:100px;">بۆ بینینی کەشوهەوا، ناوی شارێک بنووسە</p>', unsafe_allow_html=True)
