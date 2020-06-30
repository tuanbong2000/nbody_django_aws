import os, shutil
import sys
#from create_data_oneSystem import createData

# Stars interacting gravitationally

# Anh Tuan Vu

# Run C++ to create the file sh nbody_sh1
def create_data_out(path_data_input,path_data_out):
        # Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
        text1 = "./nbody_sh1 -d 0.03 -e 1 -o 0.1 -t 50 < "
        text2 =path_data_input
        text3 =" | awk '{print $2, $3, $4}'> "
        text4 =path_data_out
        os.system(text1+text2+text3+text4)
#create_data_out('datas/data_in.txt', 'datas/data_out.txt')
