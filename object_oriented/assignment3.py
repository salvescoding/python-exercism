import sys
import os.path


class ConfigDict(dict):

    def __init__(self, file_name):
        self._file_name = file_name
        if os.path.isfile(self._file_name):
            with open(self._file_name) as f:
                for line in f:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._file_name, 'a') as f:
            for key, value in self.items():
                f.write("{}={}\n".format(key, value))


cd = ConfigDict('config_dict.txt')
print(cd)
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print("I am writing data: {} = {}".format(key, value))
    cd[key] = value
else:
    print('Printing data in the file')
    for key in cd.keys():
        print("  {} = {}".format(key, cd[key]))

print(cd)
