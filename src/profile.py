class Profile:

    def __init__(self, yaml, name):
        default = {
            'dir': '~',
            'shell': True,
            'process': None,
            }

        self.name = name
        for key in default:
            exists = False
            if key in list(yaml.keys()):
                setattr(self, key, yaml[key])
                exists = True
            if exists == False:
                setattr(self, key, default[key])
    
    def loadProcesses(self):
        self.shellExec = []
        keys = ['cmd', 'args', 'depends_on', 'silent']
        for process in self.process:
            id = process
            for key in keys:
                if not key in self.process[id].keys():
                    if key == 'cmd':
                        print('SyntaxError: process[' + id + '] does not have a cmd argument')
                        exit(1)
                    self.process[id][key] = ''
            self.shellExec.append({
                'cmd': self.process[id]['cmd'] + ' ' + ' '.join(self.process[id]['args']),
                'id': id,
                'depends_on': self.process[id]['depends_on'],
                'silent': self.process[id]['silent']
            })
    
    def loadDir(self):
        self.shellExec.append({
            'id': 'dir',
            'dir': self.dir,
            'depends_on': ''
        })
    
    def orderInstructions(self):
        ordered = []
        treated = []
        while len(self.shellExec) != 0:
            elem = self.shellExec[0]
            idBeg = elem['id']
            depends_pass = False
            for dep in elem['depends_on']:
                if not dep in treated:
                    depends_pass = True
            while elem['depends_on'] != '' and depends_pass:
                for tmp in self.shellExec:
                    if tmp['id'] in elem['depends_on']:
                        elem = tmp
                        if tmp['id'] == idBeg:
                            print('Error: Infinite "depends_on" loop.')
                            exit(1)
                        break
                if elem['id'] == idBeg:
                    print('Error: undefined "depends_on" for elem ' + idBeg)
                    exit(1)
            ordered.append(elem)
            treated.append(elem['id'])
            self.shellExec.pop(self.shellExec.index(elem))
        return ordered
    
    def loadProfile(self):
        self.loadProcesses()
        self.loadDir()
        return self.orderInstructions()        
