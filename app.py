import streamlit as st
import requests

# 1. ڕێکخستنی لاپەڕە و شاردنەوەی هەموو لۆگۆ و نیشانە زیادەکان (سەوز و سوورەکە)
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

hide_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QS1n {display: none !important;}
    #stDecoration {display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    </style>
    """
st.markdown(hide_elements, unsafe_allow_html=True)

# 2. فانکشنی دیاریکردنی وێنەی جوڵاو (GIF) بەپێی کەشوهەوا و کات
def get_weather_gif(desc, is_day):
    desc = desc.lower()
    
    # ئەگەر شەو بوو (وەک وێنەکەی ناردت ئەستێرە و هەور)
    if not is_day:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif"
    
    # ئەگەر ڕۆژ بوو و باران بوو
    if "rain" in desc or "drizzle" in desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/t7Qb8655Z1VfBGr5XB/giphy.gif"
    
    # ئەگەر ڕۆژ بوو و هەور بوو
    elif "cloud" in desc or "overcast" in desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/cnXvL06uK9Tf8U54fD/giphy.gif"
    
    # ڕۆژی گەش و هەتاو
    return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/0hNftA9q66y3Xq8BfH/giphy.gif"

# 3. فانکشنی جێگیرکردنی باکگراوند و ستایلی کارتەکان
def apply_style(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .weather-info {{
            text-align: center;
            color: white;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .temp-text {{
            font-size: 100px !important;
            font-weight: 200;
            margin-bottom: -20px;
        }}
        .desc-text {{
            font-size: 25px;
            font-weight: 400;
            margin-bottom: 30px;
        }}
        .card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin: 10px 0;
        }}
        </style>
        """, unsafe_allow_html=True)

# 4. دەستپێکردنی بەرنامە
city = st.text_input("", placeholder="ناوی شار بنووسە... (وەک: Erbil)", label_visibility="collapsed")

if city:
    try:
        res = requests.get(f"https://wttr.in/{city}?format=j1").json()
        curr = res['current_condition'][0]
        
        temp = curr['temp_C']
        desc = curr['weatherDesc'][0]['value']
        is_day = curr['weatherDesc'][0]['value'] # هەندێک API کاتەکە دەدەن، لێرەدا بەپێی وەسفەکە دیاری دەکەین
        
        # دیاریکردنی ئەوەی ئایا کاتەکە شەوە یان نا (بۆ باکگراوندەکە)
        import datetime
        hour = datetime.datetime.now().hour
        daytime = 6 <= hour < 18
        
        apply_style(get_weather_gif(desc, daytime))
        
        # نیشاندانی زانیارییەکان ڕێک وەک وێنەی مۆبایلەکە
        st.markdown(f"""
            <div class="weather-info">
                <p style="font-size: 30px; margin-bottom: 0;">{city.capitalize()}</p>
                <h1 class="temp-text">{temp}°</h1>
                <p class="desc-text">{desc}</p>
                <div class="card">
                   <p>خێرایی با: {curr['windspeedKmph']} km/h | شێ: {curr['humidity']}%</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    except:
        st.
