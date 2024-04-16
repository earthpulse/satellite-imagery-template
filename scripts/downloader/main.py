from spai.storage import Storage
from spai.config import SPAIVars
from spai.data.satellite import explore_satellite_imagery, download_satellite_imagery

vars = SPAIVars()

# # explore available images
# print(
#     "Looking for images in the range",
#     vars["DATES"],
#     "with cloud cover less than 10%...",
# )
# images = explore_satellite_imagery(vars["AOI"], vars["DATES"], cloud_cover=10)
# if len(images) == 0:
#     raise ValueError("No images found")

# # download images and save locally
# storage = Storage()
# sensor = "sentinel-2-l2a"
# existing_images = storage["data"].list(f"{sensor}*.tif")

# dates = [image.split("_")[1].split(".")[0] for image in existing_images]
# print("Found", len(images), f"image{'s' if len(images) > 1 else ''}")
# new_images = []
# for image in images:
#     # check if image is already downloaded
#     date = image["datetime"].split("T")[0]
#     if date in dates or date in new_images:
#         print("Image already downloaded:", date)
#         continue
#     new_images.append(date)
#     print("Downloading new image:", date)
#     path = download_satellite_imagery(storage["data"], vars["AOI"], date)
#     print("Image saved at", path)

aoi = vars["AOI"]

print(aoi)

dates = vars["DATES"]

print(dates)

# # upload
# {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {}, 'geometry': {'coordinates': [[[2.057826447074177, 41.46536860970346], [2.057826447074177, 41.42620786810252], [2.1236170193665203, 41.42620786810252], [2.1236170193665203, 41.46536860970346], [2.057826447074177, 41.46536860970346]]], 'type': 'Polygon'}}]}
# ['2024-04-02', '2024-04-03']

# # draw
# {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Polygon', 'coordinates': [[[2.097638, 41.431626], [2.034514, 41.388335], [2.129201, 41.372867], [2.097638, 41.431626]]]}}
# ['2024-04-03', '2024-04-12']