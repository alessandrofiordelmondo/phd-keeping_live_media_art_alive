# import requests

# # def download(url):
# url="https://drive.google.com/file/d/12cxA2Na9SzPCGs-dqq8Yl9Y9O_WI2gvH/view?usp=sharing"

import requests

def extract_file_id(url):
    # Split the URL by "/"
    parts = url.split("/")
    # The file ID is the part after "d"
    if "file/d/" in url:
        return parts[parts.index("d") + 1]
    return None


def download(url):
    file_id = extract_file_id(url)
    print(f"Extracted File ID: {file_id}")
    # Replace 'FILE_ID' with the actual file ID
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    filename = "image.jpg"
    response = requests.get(download_url, stream=True)
    
    if response.status_code == 200:
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
                print(f"Image successfully downloaded: {filename}")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
