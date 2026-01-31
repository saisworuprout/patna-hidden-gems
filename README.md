# 📍 Underrated Patna: The Anti-Hype Map

**A data-driven web application to discover the hidden, high-quality spots in Patna that algorithms often overlook.**

http://localhost:8501 https://share.streamlit.io 

## 📖 About The Project
**Underrated Patna** is a geospatial web application designed to solve the "popularity bias" found in modern navigation services. Standard platforms like Google Maps or TripAdvisor heavily weigh their algorithms toward user engagement volume. Consequently, they often direct traffic to the same few famous locations, creating overcrowded "tourist traps" while leaving high-quality but quieter establishments invisible to the public.

This project disrupts that pattern by using data analytics to surface "Hidden Gems." Instead of ranking locations purely by popularity, the application utilizes a custom logic layer that evaluates the ratio between **User Satisfaction (Star Rating)** and **Footfall (Review Count)**. The system ingests curated location data for the city of Patna and categorizes venues into three distinct segments:
* 🔴 **"Hyped/Crowded"** (Red) for high-traffic zones.
* 🔵 **"Standard"** (Blue) for average locations.
* 🟢 **"Hidden Gems"** (Green) for spots with exceptional ratings (4.5+) but low commercial visibility.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **Data Processing:** Pandas
* **Geospatial Visualization:** Folium & Streamlit-Folium
* **Data Storage:** CSV (Curated Dataset)

## 🚀 Key Features
* **Interactive Map:** Visualizes data using Leaflet.js (via Folium).
* **Smart Algorithms:** Automatically categorizes locations based on review/rating ratio.
* **Dynamic Filtering:** Users can filter by category (Cafe, Park, Museum, etc.).
* **Real-time Search:** Instantly locate specific places by name.
* **Visual Popups:** Clickable markers displaying images, ratings, and status.
* # patna-hidden-gems
