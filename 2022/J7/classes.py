import json

def set_value(obj, path, value):
    path_parts = path.split(".")
    for part in path_parts[:-1]:
        if part not in obj:
            obj[part] = {}
        obj = obj[part]
    obj[path_parts[-1]] = value

class Path:
    def __init__(self):
         self.path = []

    def getCurrentPath(self):
        return '.'.join(self.path)

    def doChangeDirectory(self, directoryName):
        if directoryName == '..':
            del self.path[-1]
        else:
            self.path.append(directoryName)

    def __str__(self):
        return '/'.join(self.path)

class Arborescence:
    def __init__(self):
        self.arbo = {}
        self.repo_size = {}

    def addSize(self, path, value):
        for repo in path.split('.'):
            if repo not in self.repo_size:
                self.repo_size[repo] = value
            else:
                self.repo_size[repo] += value

    def addItem(self, name, value, path=''):
        print("ADD")
        if path == '':
            print("root")
            self.arbo[name] = value

        else:
            print("Path : "+ path+'.'+name)
            update_path = path + '.' + name
            set_value(self.arbo, update_path, value)

            self.addSize(path, value)

    def part1(self):
        total = 0

        for repo in self.repo_size:
            value = self.repo_size[repo]
            print("{} : {}".format(repo, value))
            if value <= 100000:
                print("YES")
                total += value

        return total

    def __str__(self):
        return json.dumps(self.repo_size, indent = 2)
