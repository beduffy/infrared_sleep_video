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
        out = cv2.VideoWriter(fn, _fourcc, 3, size)

        for fp in all_filepaths:
            img = cv2.imread(fp)
            height, width, layers = img.shape
            size = (width, height)
            
            filename = fp.split('/')[-1]
            print(filename)
            # filename_date_alone = filename.split('-')
            filename_date_plus = filename.split('img_dt_')[-1]
            filename_date_plus = filename_date_plus.split('_frame')[0]
            # text_to_show = '-'.join(filename_date_plus.split('-'))
            text_to_show = filename_date_plus

            cv2.putText(img, text_to_show, (10, 23), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # img_array.append((filename, img))
            out.write(img)
        out.release()
        
        # print('Num images: {}'.format(len(img_array)))

        # img_array = sorted(img_array, key=lambda x: x[0])
        
        # print('Changing directory')
        # os.chdir(snapshots_folder)
        # print('os.getcwd(): ', os.getcwd())
        # fn = '{}_{}_night_video.mp4'.format()
        
        
        msg = 'Created night report video at: {}'.format(fn)
        print(msg)
        # for i in range(len(img_array)):
        #     out.write(img_array[i][1])
        # out.release()
        print('Finished')
    else:
        print('No images recorded, not creating video')


if __name__ == '__main__':
    folder_path = 'data/test/'
    create_night_video_from_folder(folder_path)
