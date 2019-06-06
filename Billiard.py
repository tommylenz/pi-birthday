def mod(Zahl, Teiler):
	if Zahl/Teiler >= 0:
		Teiler = -Teiler
	while Zahl >= -Teiler:
		Zahl += Teiler
	return Zahl==0

class Vektor:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

def billiard(Richtungsvektor, Startvektor, Tisch):
	n_horizontal = 0.5
	n_vertikal = 0
	if Richtungsvektor.y >= 0:
		while not mod(n_horizontal, 1):
			n_vertikal += 1
			n_horizontal = (Richtungsvektor.x*(n_vertikal*Tisch.y-Startvektor.y)/Richtungsvektor.y+Startvektor.x)/Tisch.x

	elif Richtungsvektor.y < 0:
		while not mod(n_horizontal, 1):
			n_vertikal -=1
			n_horizontal = (Richtungsvektor.x*(n_vertikal*Tisch.y-Startvektor.y)/Richtungsvektor.y+Startvektor.x)/Tisch.x

	print(int(n_horizontal), n_vertikal)

def main():
	xR, yR = input("Richtungsvektor (x,y): ").split(",")
	Richtungsvektor = Vektor(xR, yR)
	xS, yS = input("Startvektor (x,y): ").split(",")
	Startvektor = Vektor(xS, yS)
	Tischbreite, Tischlänge = input("Tischmaße (Breite, Länge): ").split(",")
	Tisch = Vektor(Tischbreite, Tischlänge)
	billiard(Richtungsvektor,  Startvektor, Tisch)

main()
