import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Underrated Patna", layout="wide")
st.title("📍 Underrated Patna: The Anti-Hype Map")

# 2. LOAD DATA
try:
    df = pd.read_csv("places.csv")
except FileNotFoundError:
    st.error("Error: Could not find places.csv")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Find Your Spot")
unique_types = ["All"] + list(df['type'].unique())
selected_type = st.sidebar.selectbox("Select Category", unique_types)
search_query = st.sidebar.text_input("Search by Name")

# --- FILTER DATA ---
filtered_df = df
if selected_type != "All":
    filtered_df = filtered_df[filtered_df['type'] == selected_type]
if search_query:
    filtered_df = filtered_df[filtered_df['name'].str.contains(search_query, case=False)]

st.sidebar.write(f"Found {len(filtered_df)} places")

# 3. CREATE MAP
m = folium.Map(location=[25.61, 85.12], zoom_start=13)

# 4. ADD PINS WITH IMAGES
for index, row in filtered_df.iterrows():
    
    # Logic: Pin Color
    reviews = int(row['reviews'])
    rating = float(row['rating'])

    if reviews > 1000:
        color = "red"
        status = "Hyped / Crowded 🚨"
    elif reviews < 100 and rating >= 4.5:
        color = "green"
        status = "Hidden Gem 💎"
    else:
        color = "blue"
        status = "Standard Spot"

    # --- NEW: HTML POPUP ---
    # We write HTML to show the image and bold text
    # width='200px' keeps the image small and neat
    html_popup = f"""
    <div style="width: 200px;">
        <img src="{row['image_url']}" style="width: 100%; border-radius: 5px; margin-bottom: 5px;">
        <h4 style="margin: 0;">{row['name']}</h4>
        <p style="margin: 0; color: gray;">{status}</p>
        <p>⭐ <b>{rating}</b> ({reviews} reviews)</p>
    </div>
    """
    
    # Add the Marker
    folium.Marker(
        [row['latitude'], row['longitude']],
        popup=folium.Popup(html_popup, max_width=250), # Max width prevents scrolling
        icon=folium.Icon(color=color)
    ).add_to(m)

# 5. DISPLAY
col1, col2 = st.columns([3, 1])
with col1:
    st_folium(m, width=800, height=500)
with col2:
    st.subheader("Results List")
    st.dataframe(filtered_df[['name', 'rating', 'reviews']])