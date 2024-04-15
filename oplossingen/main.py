import pygame, sys
import random
from pygame.locals import QUIT

breedte = 600
hoogte = 400
dikte = 5
penseelkleur = (0, 0, 0)
achtergrondkleur = (240, 230, 190)
penseelvorm = "cirkel"

pygame.init()
DISPLAYSURF = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Codefever Paint')
DISPLAYSURF.fill(achtergrondkleur)


def random_kleur():
    rood = random.randint(0, 255)
    groen = random.randint(0, 255)
    blauw = random.randint(0, 255)
    return (rood, groen, blauw)


while True:
    muispos = pygame.mouse.get_pos()  # Positie van muis

    for event in pygame.event.get():
        # Linkermuisknop ingedrukt:
        if pygame.mouse.get_pressed() == (True, False, False):
            # penseelkleur = random_kleur()
            if penseelvorm == "cirkel":
                pygame.draw.circle(DISPLAYSURF, penseelkleur, muispos, dikte)
            elif penseelvorm == "vierkant":
                pygame.draw.rect(DISPLAYSURF, penseelkleur, (muispos, (2 * dikte, 2 * dikte)))
        # Rechtermuisknop: gom
        if pygame.mouse.get_pressed() == (False, False, True):
            pygame.draw.circle(DISPLAYSURF, achtergrondkleur, muispos, dikte + 3)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                penseelkleur = (255, 0, 0)
            if event.key == pygame.K_g:
                penseelkleur = (0, 255, 0)
            if event.key == pygame.K_b:
                penseelkleur = (0, 0, 255)
            if event.key == pygame.K_z:
                penseelkleur = (0, 0, 0)
            if event.key == pygame.K_UP:
                dikte += 1
            if event.key == pygame.K_DOWN:
                dikte -= 1
            if event.key == pygame.K_k:
                print("Stel zelf je kleur samen!")
                rood = int(input("Rood (0-255): "))
                groen = int(input("Groen (0-255): "))
                blauw = int(input("Blauw (0-255): "))
                penseelkleur = (rood, groen, blauw)
            if event.key == pygame.K_s:
                bestandsnaam = input("Opslaan als: ")
                pygame.image.save(DISPLAYSURF, "kunstwerken/" + bestandsnaam + ".jpg")
            if event.key == pygame.K_m:
                penseelkleur = random_kleur()
            if event.key == pygame.K_w:
                DISPLAYSURF.fill(achtergrondkleur)
            if event.key == pygame.K_i:
                bestandsnaam = input("Geef bestandsnaam: ")
                afbeelding = pygame.image.load(bestandsnaam)
                DISPLAYSURF.blit(afbeelding, (0, 0))
            if event.key == pygame.K_v:
                penseelvorm = "vierkant"
            if event.key == pygame.K_c:
                penseelvorm = "cirkel"
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()