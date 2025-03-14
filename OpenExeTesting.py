import os
import shutil

path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Substance 3D Painter 2024\\Adobe Substance 3D Painter.exe"
"C:\Program Files (x86)\Steam\steamapps\common\Substance 3D Painter 2024\Adobe Substance 3D Painter.exe"

# finds if the file is executable
def is_exe_on_drive(name):
    print(shutil.which(name))

# doesn't find for some reason
filetestpath = "Adobe Substance 3D Painter.exe"

#is_exe_on_drive(filetestpath)
is_exe_on_drive(path)

# will open application
#os.startfile(path)
