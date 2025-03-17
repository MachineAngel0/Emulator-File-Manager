
import patoolib
def FileExtractor(FilePath, ExtractPath):
    patoolib.extract_archive(FilePath, outdir=ExtractPath)






# test files, everything works perfectly

temp_7z_file_path = "C:\\Users\\Adams Humbert\\Downloads\\TF3\\Yu-Gi-Oh! Duel Monsters GX Tag Force 3 (English 07-29-21).7z"
temp_7z_extract_file_path = "C:\\Users\\Adams Humbert\\Downloads\\TF3"
temp_rar_file_path = "C:\\Users\\Adams Humbert\\Downloads\\WC2011\\5720 - Yu-Gi-Oh! 5D's World Championship 2011 - Over the Nexus (U).rar"
temp_rar_extract_file_path = "C:\\Users\\Adams Humbert\\Downloads\\WC2011"



#FileExtractor(temp_rar_file_path, temp_rar_extract_file_path)
#FileExtractor(temp_7z_file_path, temp_7z_extract_file_path)