from pathlib import Path
import cv2
import numpy as np
import math

imgs_path = Path("data/imgs")
masks_path = Path("data/masks")
mozaic_path = Path("data/mozaics")
mozaic_path.mkdir(exist_ok=True)

imgs = sorted(list(imgs_path.glob('*')))
masks = sorted(list(masks_path.glob('*')))

def merge(list1, list2): 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list

def get_name(img):
    return img.name[:img.name.find('_')]


for i in range(len(imgs)):
    imgs_data = []
    print("Calculating image: " + str(imgs[i].name[:-4]))
    img = cv2.imread(str(imgs[i]))
    mask = cv2.imread(str(masks[i]), cv2.IMREAD_GRAYSCALE)
    
    x_mask, y_mask = np.nonzero(mask) # this finds indices of an array, where a condition is True
    #print(x_mask, y_mask)
    
    # takes masks pixel coordinates
    mask_pos_x = set(map(lambda x: f'{x[0]}, {x[1]}',  merge(x_mask, y_mask)))
    
    if img.shape[0] < 4000:
        sz = int(img.shape[0] / 32)
    else:
        sz = 100
    
    # takes imgs pixel coordinates and saves them in img_pos
    for r in range(0, img.shape[0], sz):
        for c in range(0, img.shape[1], sz):
            crop = img[r:r+sz, c:c+sz]
            x_img, y_img = (crop[:, :, 0] >= 0).nonzero() #finds the coordinates
            img_pos = merge(x_img, y_img) # convert to list of tuples

            # iterates through img_pos and looks for them in mask_pos
            flag = 0
            for pos in img_pos:
                pos = (pos[0] + r, pos[1] + c)
                pos = f'{pos[0]}, {pos[1]}'
                if (pos in mask_pos_x):
                    flag = 1
                    break

            if flag == 1:
                imgs_data.append(crop)
    
    
    # merge every pair of images into mozaic
    if imgs[i] == imgs[-1]:
        x = math.sqrt(len(imgs_data)) # number of images per row
    elif get_name(imgs[i]) != get_name(imgs[i+1]):    
        x = math.sqrt(len(imgs_data))
    else:
        continue
            
    #if number is not a whole number, make it
    if x % 1 != 0:
        #x = int(x) + 1
        x = math.ceil(x)

    sz_moz = int(x*sz) # mozaic size
    mozaic = np.zeros((sz_moz, sz_moz, 3), dtype=np.uint8)

    j = 0
    for r in range(0, sz_moz, sz):
        for c in range(0, sz_moz, sz):
            try:
                mozaic[r:r+sz, c:c+sz] = imgs_data[j]
                j += 1
            except:
                continue

    cv2.imwrite(f"{str(mozaic_path)}/mozaic_{get_name(imgs[i])}.png", mozaic)
