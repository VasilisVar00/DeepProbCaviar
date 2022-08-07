# code to transform all video annotation
# video_names.txt contains the names of all videos
# we use the transform_files function

from get_coordinates import get_coordinates
from util import transform_files


base1 = 'caviar/original/'
base2 = 'caviar/enhanced/'

with open('video_names.txt','r') as f:
    files = f.readlines()
    files = map(lambda s: s[:-1],files) # remove endline
    for fl in files:
        fin1 = base1 + fl + '/ground_truth/' + fl + '_annotation.txt'
        fin2 = base2 + fl  + '/ground_truth/' + fl + '_annotation.txt'
        fout1 = base1 + fl + '/ground_truth/' + fl + '_annotation_new.txt'
        fout2 = base2 + fl + '/ground_truth/' + fl + '_annotation_new.txt'
        transform_files(fin1,fout1)
        transform_files(fin2,fout2)
