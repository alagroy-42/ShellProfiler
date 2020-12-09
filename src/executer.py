import os
import sys
import subprocess

class Executer:

    def __init__(self, execList, name, shell):
        self.path = os.path.realpath('./profiles')
        self.name = name
        self.shell = shell
        file = open(self.getPath('pre'), 'w')
        for elem in execList:
            if elem['id'] == 'dir':
                if shell == True:
                    break
                else:
                    file.write('chdir ' + elem['dir'] + '\n')
            else:
                self.writeCmd(file, elem)
        file.close()
        if elem['id'] == 'dir':
            self.writeDir(elem)
        index = execList.index(elem)
        if index != len(execList):
            file = open(self.getPath('post'), 'w')
            for elem in range(index, len(execList)):
                if execList[elem]['id'] == 'dir':
                    continue
                self.writeCmd(file, execList[elem])
            file.close()
    
    def writeDir(self, dirElem):
        if dirElem['id'] != 'dir':
            return
        file = open(self.getPath('dir'), 'w')
        file.write(dirElem['dir'] + '\n')
        file.close()

    def writeCmd(self, file, elem):
        if elem['silent'] == True:
            elem['cmd'] += ' >&- 2>&-'
        file.write(elem['cmd'] + '\n')

    def getPath(self, arg):
        return self.path + '/' + self.name + '.' + arg + '.pfl'
    
    def exec(self):
        file = open(self.getPath('pre'), 'r')
        for cmd in file:
            subprocess.call(cmd, shell=True)
        file.close()
        if os.path.isfile(self.getPath('dir')):
            file = open(self.getPath('dir'), 'r')
            dir = file.readline().rstrip().replace('~', os.getenv('HOME'))
            os.chdir(dir)
        file = open(self.getPath('post'), 'r')
        for cmd in file:
            subprocess.call(cmd, shell=True)
        file.close()
        if self.shell:
            subprocess.call(os.getenv('SHELL'))
            os.kill(os.getppid(), 9)
            
