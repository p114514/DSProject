from os import walk
import pygame


# import surface for sprites
def import_folder(path):
    surface_list = []

    for folder_name, sub_folder, img_files in walk(path):
        for img in img_files:
            full_path = path + '\\' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list
