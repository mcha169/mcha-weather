import streamlit as st
import requests

# شاردنەوەی لۆگۆ و نیشانەکان
st.set_page_config(page_title="Weather", layout="centered")
st.markdown("""
    <style>
    #MainMenu, footer, header, .viewerBadge_container__1QS1n, #stDecoration {visibility: hidden; display:none !important;}
    </style>
    """, unsafe_allow_html=True)

def apply_bg(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        .info {{ text-align: center; color: white; text-shadow: 2px 2px 10px black; }}
        </style>
        """, unsafe_allow_html=True)

city = st.text_input("", placeholder="Erbil...")

if city:
    try:
        data = requests.get(f"https://wttr.in/{city}?format=j1").json()
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        
        # وێنەی شەو و هەور (وەک ئەوەی ویستت)
        bg_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif"
        apply_bg(bg_url)
        
        st.markdown(f"""
            <div class="info">
                <h1 style="font-size: 80px;">{temp}°C</h1>
                <p style="font-size: 30px;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.error("Error!")
else:
    apply_bg("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6bmZueXp6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyXG9eU/giphy.gif")
