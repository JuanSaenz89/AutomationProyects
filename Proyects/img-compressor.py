from PIL import Image
import os

downloads_folder = input("Ingrese ruta a la carpeta de imagenes: ")

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extesion = os.path.splitext(downloads_folder + filename)

        if extesion in ['.jpg', '.jpeg', '.png']:
            picture = Image.open(downloads_folder + filename)
            picture.save(downloads_folder + 'compressed_'+filename, optimize= True, quality = 60)
            os.remove(downloads_folder + filename)