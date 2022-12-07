import json

def set_value(object, path, filename, value):
    path_parts = path.split(".")
    for part in path_parts:
        if part not in object:
            object[part] = {}
        object = object[part]
    object[filename] = value

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

    def addFilename(self, filename, value, path):
        set_value(self.arbo, path, filename, value)
        self.addSize(path, value)

    def part1(self):
        total = 0
        all_find = {}

        for repo in self.repo_size:
            value = self.repo_size[repo]
            if value <= 100000:
                total += value
                all_find[repo] = value

        return total, json.dumps(all_find, indent = 2)

    def __str__(self):
        return json.dumps(self.arbo, indent = 2)
