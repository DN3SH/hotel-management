import cv2
import pytesseract
from aadhaar_details import get_values,get_address,send_to_json
from pathlib import Path
import json

if __name__ == "__main__":
    tesseract_path = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    aadhaar_front_img_path = Path("front1.jpg")
    aadhaar_back_img_path = Path("back1.jpg")
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    img = cv2.imread(str(aadhaar_front_img_path))
    
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
    four_points = []
   
    regex_name,regex_gender,regex_dob,regex_mobile_number,regex_aadhaar_number = get_values(img)
    regex_name = " ".join(regex_name[:3])
    print(regex_name,regex_gender,regex_dob,regex_mobile_number,regex_aadhaar_number)
   
    img = cv2.imread(str(aadhaar_back_img_path))
    
    img = cv2.resize(img,(0,0),fx=0.75,fy=0.75)
    
    regex_address = get_address(img)
    print(regex_address)
    send_to_json(regex_name,regex_gender,regex_dob,regex_mobile_number,regex_aadhaar_number,regex_address)
    
    
 