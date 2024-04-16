import streamlit as st
import os
from spai.storage import Storage
import geopandas as gpd
from spai.config import SPAIVars
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="SPAI Demo", page_icon="🌍")

storage = Storage()["data"]
vars = SPAIVars()


@st.cache_data(ttl=10)
def get_dates():  # in cloud fails because localhost is inside docker, need public url
    images = storage.list(f"*.tif")
    dates = [image.split("_")[-1].split(".")[0] for image in images]
    return dates

@st.cache_data(ttl=10)
def get_aoi_centroid():
    aoi = vars["AOI"]
    gdf = gpd.GeoDataFrame.from_features(aoi)
    centroid = gdf.geometry.centroid[0].y, gdf.geometry.centroid[0].x
    return centroid

def choose_date(dates):
    with st.sidebar:
        st.sidebar.markdown("### Dates")
        date = st.selectbox("Date", dates)
    return date

dates = get_dates()
date = choose_date(dates)
centroid = get_aoi_centroid()  # Get centroid from the AOI

url = f"http://{os.getenv('XYZ_URL')}/sentinel-2-l2a_{date}.tif/{{z}}/{{x}}/{{y}}.png"

# Create map with Folium
m = folium.Map(
    location=centroid,
    zoom_start=12,
    tiles="CartoDB Positron",
)

# Add the image layer to the map
raster = folium.raster_layers.TileLayer(
    tiles=url,
    attr="Satellite Imagery",
    name="Image",
    overlay=True,
    control=True,
    show=True,
)
raster.add_to(m)
folium_static(m)