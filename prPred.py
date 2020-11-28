# !/usr/bin/env python
# _*_coding:utf-8_*_
# File created on 2020/10
__author__ = "Wang,Yansu"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Wang,yansu"
__email__ = "Wangys_c@hotmail.com"

from optparse import OptionParser
from codes import *
import os
import shutil
# import sys
# sys.path.append('./codes')
#
# import feature
# import domain



def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=]-o[--output]",
                          version="%prog 1.2")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="the result file with fasta format",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="the output folder",
                      default=False)
    (options, args) = parser.parse_args()

    # extract option from command line
    input = options.input
    output = options.output
    return (input,output)

def write_file(filename):
    """
    写入文件，先判断文件路径是否存在，如果存在，先删除文件，然后进行插入操作
    """
    file_path = os.getcwd() + '/' + filename
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
        #os.removedirs(file_path)
        os.mkdir(file_path)
    else:
        os.mkdir(file_path)
    return (file_path)

def main():
    input,output = MakeOption()
    feature.extract_feature(input,output)
    df1 = feature.bind_feature(output)
    df3 = feature.feature_selection(df1,output)
    df5_scaler= feature.model_training_scale(df3)
    seq_dict2 = feature.svc_model(df5_scaler,input,output)
    str1_dict = domain.tmhmm_number(input,output)
    str_dict = domain.pfam_domain(input,output)
    domain.merge(seq_dict2,str1_dict, str_dict,output)
    # os.remove('./'+output +'/domain')
    # os.remove('./'+output +'/features')
if __name__ == "__main__":
    main()
