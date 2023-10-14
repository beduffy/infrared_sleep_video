import os
import glob

import cv2
import numpy as np

def create_night_video_from_folder(folder_path):
    all_filepaths = sorted(glob.glob(folder_path + '*'))

    print('num images:', len(all_filepaths))

    if len(all_filepaths) > 0:
        img_array = []
        print(all_filepaths[:5])

        img = cv2.imread(all_filepaths[0])
        height, width, layers = img.shape
        size = (width, height)

        fn = 'night_video.mp4'
        _fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(fn, _fourcc, 15, size)

        for fp in all_filepaths:
            img = cv2.imread(fp)
            height, width, layers = img.shape
            size = (width, height)
            
            filename = fp.split('/')[-1]
            print(filename)
            filename_date_plus = filename.split('img_dt_')[-1]
            filename_date_plus = filename_date_plus.split('_frame')[0]
            text_to_show = filename_date_plus

            cv2.putText(img, text_to_show, (10, 23), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            out.write(img)
        out.release()
        
        msg = 'Created night report video at: {}'.format(fn)
        print(msg)
        print('Finished')
    else:
        print('No images recorded, not creating video')


if __name__ == '__main__':
    folder_path = 'data/test/'
    create_night_video_from_folder(folder_path)