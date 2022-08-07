#Laboratorio 4.4.1.8
#Elaborado por: Emmanuel López García
#Fecha: 06 de agosto del 2022

# NOTA: PARA ESTE LABORATORIO SE CREÓ EL DIRECTORIO LLAMADO "tree"

import os
class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            return
        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)

directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")