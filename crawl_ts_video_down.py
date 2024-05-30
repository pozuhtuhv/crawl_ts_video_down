import os
import requests
import time
import subprocess

# headers area
headers = {
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Referer': 'https://test.com', # ex
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'sec-ch-ua-platform': '"Windows"',
}

# download_folder name
save_folder = 'image_download'

# create folder confirm
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# download function
def download_image(image_url, save_path):
    response = requests.get(image_url, headers=headers)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {save_path}")
    else:
        print(f"Failed to download {image_url}")

# download loop
for i in range(1, 916): # start number, end number
    time.sleep(1.5)
    image_number = f"{i:04}"  # 4 number value for cmd copy load 
    image_url = f'https://test.com/video{i}.jpeg'
    save_path = os.path.join(save_folder, f'{image_number}.jpeg')
    download_image(image_url, save_path)

# mp4 file combine
cmd_command = f'copy /b * a.mp4'

# CMD command run
subprocess.run(cmd_command, shell=True, cwd=save_folder)
print("All images have been merged into a.mp4")
