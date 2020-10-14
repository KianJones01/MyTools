#!/usr/bin/env python3
import os
import sys

import pyfiglet


class finder():
    def __init__(self):
        self.mode = self.setMode()
        self.path = sys.argv[1]
        self.fileFolder = self.fileOrFolder()
        self.tacdicti = self.getTacs()
        self.header()
        self.main()

    def getTacs(self):
        dicti = {'help':['-h', '--help']
                 }
        return dicti

    def header(self):
        tacl = 70
        print(tacl * '-' + '\n' + pyfiglet.figlet_format("Huffer's Python Requirement Finder") + '\n' + tacl * '-')

    def setMode(self):
        if len(sys.argv) > 1:
            self.mode = sys.argv[1]
        else:
            print('Invalid number of arguements, try adding -h for more information.')
            sys.exit()

    def fileOrFolder(self):
        if os.path.isfile(self.path) == True:
            return 'file'
        else:
            return 'folder'

    def filesearch(self, file):
        imports = []
        with open(file, 'r') as f:
            for line in f.readlines():
                if 'import' in line:
                    curr = line.split(' ')
                    if len(curr) == 2:
                        imports.append(line)
        return imports

    def tacinvestigating(self):
        toreturn = self.tacdicti[self.mode]
        return toreturn

    def getdirstuff(self, path, ext='.py'):
        files = []
        returnfiles = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            files.extend(filenames)
        for file in files:
            if ext in file:
                returnfiles.append(file)
        return returnfiles

    def main(self):
        if self.fileFolder == 'file':
            imports = self.filesearch(self.path)
            for imported in imports:
                importing = imported.split(' ')[1]
                print('Installing ' + imported.replace('import', 'module: '))
                #os.system('pip install ' + importing)
        else:
            # self.fileFolder = 'folder'
            filestosearch = self.getdirstuff(self.path)
            for file in filestosearch:
                imports = self.filesearch(self.path+'\\'+file)
                for imported in imports:
                    importing = imported.split(' ')[1]
                    print('Installing ' + imported.replace('import', 'module: '))
                    #os.system('pip install ' + importing)



a = finder()
