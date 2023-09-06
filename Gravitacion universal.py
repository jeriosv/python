G : float = 6.67384e-11 # Constante de Cavendish [Nm^2/kg^2]
m1 : float = 5.972e+24 # Masa de la Tierra [kg]
m2 : float = 1 # Masa de alguna victima
r : float = 6400e3 # Radio de la Tierra [m]

# Solución
F = G * m1 * m2 / r**2
print(F)

