# author:ChriPaul
# file:pathUtil.py
# time:2021/02/23

import os

class pathUtils:
    @staticmethod
    def pathApi(file_paths):
        project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
        file_path = ""
        for item in file_paths:
            file_path = os.path.join(file_path, item)
        return os.path.join(project_path,file_path)
if __name__ == '__main__':
    print(pathUtils.pathApi(file_paths=["test_data","getData.py"]))














