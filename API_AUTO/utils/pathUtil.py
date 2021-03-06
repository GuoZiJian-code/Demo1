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
        return os.path.join(project_path, file_path)

    @staticmethod
    def create_file(filename):
        """
        创建日志文件夹和日志文件
        :param filename:
        :return:
        """
        path = filename[0:filename.rfind("/")]
        if not os.path.isdir(path):  # 无文件夹时创建
            os.makedirs(path)
        if not os.path.isfile(filename):  # 无文件时创建
            fd = open(filename, mode="w", encoding="utf-8")
            fd.close()
        else:
            pass


if __name__ == '__main__':
    print(pathUtils.pathApi(file_paths=["test_data", "getData.py"]))
