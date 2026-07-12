from dataclasses import dataclass

from bs4 import BeautifulSoup
@dataclass
class ImageResult:
    total_images:int
    images_with_alt:int
    missing_alt: int
    empty_alt: int

def analyze_images(html:str)-> ImageResult:
    soup = BeautifulSoup(html, "lxml")
    images = soup.find_all("img")
    total_images = len(images)
    images_with_alt =0 
    missing_alt = 0
    empty_alt = 0

    for img in images:
        alt = img.get("alt")

        if alt is None:
            missing_alt +=1
        elif alt.strip() == "":
            empty_alt +=1
        else:
            images_with_alt +=1
    
    return ImageResult(
        tota_images = total_images,
        images_with_alt = images_with_alt,
        missing_alt = missing_alt,
        empty_alt = empty_alt,
    )