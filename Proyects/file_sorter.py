from PIL import Image
import os

downloads_folder = ""
picture_folder = ""

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extesion = os.path.splitext(downloads_folder + filename)

        if extesion in ['.jpg', '.jpeg', '.png']:
            picture = Image.open(downloads_folder + filename)
            picture.save(picture_folder + 'compressed_'+filename, optimize= True, quality = 60)
            os.remove(downloads_folder + filename)
            print(name + ": " + extesion)

        if extesion in ['.mp3']:
            music_folder = "" #Insertar ruta a la que mover los archivos
            os.rename(downloads_folder + filename, music_folder + filename)
