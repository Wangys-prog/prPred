from optparse import OptionParser
from Bio import SeqIO
import os
import shutil
import subprocess
import datetime
import re
import os


def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=]-o[--output]",
                          version="%prog 1.2")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="the result file with fasta format",
                      default=False)
    (options, args) = parser.parse_args()

    # extract option from command line
    input = options.input
    return (input)
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

def run_command(cmd):
    # print("INFO: Running command: {0}".format(cmd), flush=True)
    print(cmd)
    return_code = subprocess.call(cmd, shell=True)
    if return_code != 0:
        print("ERROR: [{2}] Return code {0} when running the following command: {1}".format(return_code, cmd, datetime.datetime.now()))

def main():
    input = MakeOption()
    file_path = input
    write_file("split_fasta_result")
    for file in os.listdir(file_path):
        (name, suffix) = os.path.splitext(file)
        cmd1 = "prPred" + ' -i ' + \
               input + "/"+ file + \
               " -o " +name +"_result"
        run_command(cmd1)
        shutil.move(name+"_result", "split_fasta_result")
    # file_path = input
    # txt_list1 = []
    # for file in os.listdir(file_path):
    #     txt_list1.append(file_path + '/' + file)
    # for i in range(len(txt_list1)):
    #     cmd1 = "prPred" + ' -i ' + \
    #            txt_list1[i] + \
    #            " -o split_fasta_result/" + txt_list1[i].split("/")[-1] + "_result"
    #     run_command(cmd1)
if __name__ == "__main__":
    main()