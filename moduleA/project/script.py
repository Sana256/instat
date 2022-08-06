import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

print(sys.path)
import moduleA.for_import


def script():
    moduleA.for_import.ForImportFromTopLevel()
    print("done")


if __name__ == '__main__':
    script()