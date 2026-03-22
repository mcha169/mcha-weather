import streamlit as st
import requests

# ڕێکخستنی لاپەڕە
st.set_page_config# لادانی نیشانەی Fork و مێنیووی سەرەوە
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QS1n {display: none !important;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)(page_title="M C H A Weather", page_icon="🌤️")

# فانکشنی دۆزینەوەی وێنەی جوڵاو (GIF) بەپێی کەشوهەوا
def get_weather_gif(weather_desc):
    weather_desc = weather_desc.lower()
    
    # ئەگەر شەو بوو
    if "night" in weather_desc or "clear" in weather_desc and "night" in weather_desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif" # شەوی ئەستێرەاوی
    
    # ئەگەر هەتاو بوو (بە ڕۆژ)
    elif "sunny" in weather_desc or "clear" in weather_desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/0hNftA9q66y3Xq8BfH/giphy.gif" # ڕۆژی گەش
    
    # ئەگەر باران بوو
    elif "rain" in weather_desc or "drizzle" in weather_desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/t7Qb8655Z1VfBGr5XB/giphy.gif" # باران
    
    # ئەگەر هەور بوو
    elif "cloud" in weather_desc or "overcast" in weather_desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/cnXvL06uK9Tf8U54fD/giphy.gif" # هەور
    
    # ئەگەر بەفر بوو
    elif "snow" in weather_desc:
        return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKQuYm7908t3I9W/giphy.gif" # بەفر
        
    return "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7btXv9m7G2pPzWxy/giphy.gif"

# دروستکردنی باکگراوند و ستایل
def set_bg(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        .mcha-title {{
            font-size: 90px !important;
            font-weight: 900;
            text-align: center;
            color: #FFD700;
            text-shadow: 5px 5px 20px black;
        }}
        .designer-text {{
            text-align: center;
            color: white;
            font-size: 25px;
            font-weight: bold;
            text-shadow: 2px 2px 10px black;
        }}
        h1, label, .stMetric {{ color: white !important; text-align: center; text-shadow: 2px 2px 10px black; }}
        .stButton>button {{
            width: 100%;
            background-color: #FFD700 !important;
            color: black !important;
            font-weight: bold;
            border-radius: 12px;
        }}
        </style>
        """, unsafe_allow_html=True)

# ناونیشانی سەرەکی
st.markdown('<p class="mcha-title">M C H A</p>', unsafe_allow_html=True)
st.markdown('<p class="designer-text">دیزاینەری کەشوهەوا</p>', unsafe_allow_html=True)

city = st.text_input("ناوی شار بنووسە:", "Erbil")

if st.button("🔍 پشکنین"):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url).json()
        
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        
        # دیاریکردنی وێنە جوڵاوەکە
        gif_url = get_weather_gif(desc)
        set_bg(gif_url)
        
        st.metric(label=f"پلەی گەرمی لە {city}", value=f"{temp} °C")
        st.write(f"### دۆخی ئاسمان: {desc}")
        
    except:
        st.error("کێشەیەک هەیە، ناوی شارەکە بپشکنە!")
else:
    # باکگراوندی سەرەکی پێش گەڕان
    set_bg("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/u01ioCe6G8URG/giphy.gif")
