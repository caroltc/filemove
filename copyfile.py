#!usr/bin/python
#-*-coding:utf-8-*-

import sys,os
import shutil


class FileMove:
    def __init__(self, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path
        if not os.path.exists(self.file_path) :
            raise RuntimeError(" dir not exists")
    def run(self):
        self.read_path(self.file_path, '++++')

    def read_path(self, read_folder, prev):
        if os.path.isdir(read_folder):
            for (root,dirs,files) in os.walk(read_folder) :
                for file_name in files:
                    print prev,read_folder+"/"+file_name
                    self.move_file(read_folder,file_name)
                    if read_folder != self.file_path:
                        self.rm_empty_dir(read_folder)
                for dirname in dirs:
                    if not os.listdir(str(read_folder)+'/'+str(dirname)):
                        self.rm_empty_dir(str(read_folder)+'/'+str(dirname))
                    else:
                        print prev+'#'+str(dirname)
                        self.read_path(str(read_folder)+'/'+str(dirname), prev+' ++++')

    def move_file(self,path,file):
        print path+"/"+file, '  moved'
        shutil.move(path+"/"+file, self.output_path+"/"+file)

    def copy_file(self,path,file):
        print path+"/"+file, '  copyed'
        shutil.copyfile(path+"/"+file, self.output_path+"/"+file)

    def rm_empty_dir(self, path):
        print path, '  removed'
        if not os.listdir(path):
            os.removedirs(path)

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print "command error!\neg: python copyfile.py --read_path --output_path"
        sys.exit(0) 
    read_folder = sys.argv[1]
    output_folder = sys.argv[2]
    fileMove = FileMove(read_folder, output_folder)
    fileMove.run()
