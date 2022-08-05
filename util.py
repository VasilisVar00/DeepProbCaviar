import os
import re

# find out how many frames are in the video

def get_total_frames(dir_path):
    return len([entry for entry in os.listdir(dir_path) 
    if os.path.isfile(os.path.join(dir_path, entry))])


def transform_files(input_file,output_file):
    frames = get_total_frames(input_file.split("-")[1].split("/")[0]) # take only Walk1
    Tmax = frames*40
    with open(input_file, "r") as fin, open(output_file,'w') as fout:
        lines = fin.readlines()
        for line in lines:
            l = (line.split(":")) # l[0] is the simple event l[1] is a list of intervals
            nums = re.findall(r'\d+',l[1]) # find all numbers
            new_l = [int(i) for i in nums] 
            new_l.sort()   

            # in the sorted list take two consecutive numbers i.e start and finish of interval
            # each jump is a jump of two (to take the next interval)

            k = 0 
            j = k+1
            down = new_l[k]
            up = new_l[j]
            flag = 'false'
            for i in range(0,Tmax+40,40):
                if(i > up):
                    flag = "false"
                    if(j < len(new_l) - 1):
                        down = new_l[k+2] #jump of two
                        up = new_l[j+2]
                if(i >= down and i <= up):
                    flag = "true"
                fout.write("holdsAt({0} = {1},{2})\n".format(l[0],flag,i))
    
    fin.close()
    fout.close()
    

transform_files('caviar/original/01-Walk1/ground_truth/01-Walk1_annotation.txt','caviar/original/01-Walk1/ground_truth/01-Walk1_annotation_new.txt')






