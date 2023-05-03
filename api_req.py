# import requests
# url = "https://example.com/api/temperate_phages/"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
# else:
#     print("Error: Unable to retrieve data")

# print(response)


# # for phage in data:
# #     photo_url = phage['plaque_photo']
# #     # Use another request to retrieve the photo data and save it to a file or display it
import requests
import pandas as pd
import os


# url = "https://phagesdb.org/api/lytic_phages/"
url = "https://phagesdb.org/api/temperate_phages/"


headers = {
    "accept": "application/json",
    "X-CSRFToken": "E5dLR9i3zTObbD9Sfkyok6Ja9ykZBiqCXgQBVLXUwOdUSCCyqrhbfYKHSUxLKXRx"
}

response = requests.get(url, headers=headers)
data = response.json()

# print(response.status_code)
# print(response.json())

df = pd.DataFrame(data["results"])
df = df.dropna(subset=['plaque_thumb_file'])
print(df.shape[0])
print(df.columns)

# Create a folder to store the images
os.makedirs('temperate', exist_ok=True)

# Iterate through the dataframe and download the images
for url in df['plaque_thumb_file']:
    response = requests.get(url)
    filename = url.split('/')[-1]
    filepath = os.path.join('temperate', filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)

        
