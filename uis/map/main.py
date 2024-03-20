import streamlit as st
import pydeck as pdk
import os
from spai.storage import Storage

st.set_page_config(page_title="SPAI Demo", page_icon="🌍")

storage = Storage()

@st.cache_data(ttl=10)
def get_dates():  # in cloud fails because localhost is inside docker, need public url
    images = storage["data"].list(f"*.tif")
    dates = [image.split("_")[-1].split(".")[0] for image in images]
    return dates


dates = get_dates()

# AWS Open Data Terrain Tiles
TERRAIN_IMAGE = (
    "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
)

# Define how to parse elevation tiles
ELEVATION_DECODER = {"rScaler": 256, "gScaler": 1, "bScaler": 1 / 256, "offset": -32768}

st.sidebar.markdown("### Dates")

selected_layers = [
    pdk.Layer(
        "TerrainLayer",
        texture=f"{os.getenv('XYZ_URL')}/S2L2A_{date}.tif/{{z}}/{{x}}/{{y}}.png",
        # texture=f"http://{os.getenv('XYZ_URL')}/S2L2A_{date}.tif/{{z}}/{{x}}/{{y}}.png",
        elevation_decoder=ELEVATION_DECODER,
        elevation_data=TERRAIN_IMAGE,
    )
    for date in dates
    if st.sidebar.checkbox(date, True)
]

if selected_layers:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": 41.4,
                "longitude": 2.17,
                "zoom": 9,
                "pitch": 60,
            },
            layers=selected_layers,
        )
    )
else:
    st.error("Please choose at least one layer above.")

