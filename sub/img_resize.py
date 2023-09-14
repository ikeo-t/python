import os
import shutil
import cv2

#リサイズの値の領域をTkinterから取得予定
RESIZE_X=600
RESIZE_Y=400

def resize_tra(bf,af):

    def scale_to_resolation(img, resolation):
        h, w = img.shape[:2]
        scale = (resolation / (w * h)) ** 0.5
        return cv2.resize(img, dsize=None, fx=scale, fy=scale)

    #リサイズする対象のフォルダパスを取得
    before_dir= bf
    after_dir=  af
    print(before_dir,after_dir,sep='\n')

    li_before_file_name=os.listdir(before_dir)

    for i_file_name in li_before_file_name:
        join_path= os.path.join(before_dir,i_file_name)
        move_path=os.path.join(after_dir,i_file_name)
        
        if os.path.isfile(join_path):
            shutil.copyfile(join_path,move_path)
            im=cv2.imread(move_path)
            dst= scale_to_resolation(im,RESIZE_X * RESIZE_Y)
            #jpgをpngに変換
            af_move_path=move_path.replace('JPG','png')
            cv2.imwrite(af_move_path,dst,[int(cv2.IMWRITE_PNG_COMPRESSION ), 1])
            os.remove(move_path)


if __name__ =='__main__':
    pass
    # bf= r'C:\git-sample\image\before'
    # af= r'C:\git-sample\image\after'
    # resize_tra(bf,af)
    