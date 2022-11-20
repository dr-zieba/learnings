import cv2, glob, os
from pathlib import Path

available_images = glob.glob(r'open_cv\batch\*')

for file in available_images:
    ext = os.path.splitext(file)[-1].lower()
    if '.jpg' in ext:
        img = cv2.imread(file,1)
        resized_image = cv2.resize(img,(100,100))
        file_name = fr'open_cv\batch\{Path(file).stem}_resized{ext}'
        cv2.imwrite(file_name, resized_image)

