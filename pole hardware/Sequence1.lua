-- Attention il faudra remplacer les fonctions par celles correspondantes du FarmBot

-- Coordonnées des piles de plantes
local stacks = {
    {x1, y1, z1},
    {x2, y2, z2},
    {x3, y3, z3},
    {x4, y4, z4},
    {x5, y5, z5},
    {x6, y6, z6},
    {x7, y7, z7}
}

-- Distance entre les plantes
local distance = d

-- Temps d'arrosage
local T = t

-- Fonction waterPlant
function waterPlant(x,y,z)
    goTo(x,y,z)
    water(HIGH)
    sleep(T)
    water(LOW)
end

-- Fonction pour arroser une pile de plantes
function waterStack(stack)
    for i=1, 3 do
        -- Arrose la plante à la position actuelle
        waterPlant(stack[1], stack[2] + i*distance, stack[3])
    end
    for i=1, 3 do
        -- Arrose la plante à la position actuelle
        waterPlant(stack[1] + distance, stack[2] + i*distance, stack[3])
    end
end

-- Fonction qui arrose dans le vide pour faire monter l'eau le long du tuyau pour la première utilisation de la journée
function Initwater(time)
    water(HIGH)
    sleep(time)
    water(LOW)
end

Initwater(15)
-- Arrose toutes les piles de plantes
for _, stack in ipairs(stacks) do
    waterStack(stack)
end

-- retour home
goTo(home)