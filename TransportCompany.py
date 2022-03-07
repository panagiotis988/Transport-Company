# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υποεργασία 4

class Package():
    def __init__(self, description, destination):
        self.description = description
        self.destination = destination

    def cost(self):
        if self.destination == 'Αθήνα':
            return 1
        elif self.destination == 'Θεσσαλονίκη':
            return 2
        else:
            return 0

    def __str__(self):
        return f"{self.description}: Προορισμός: {self.destination}, "


class Parcel(Package):
    # Εδώ συμπληρώνετε τον κώδικά σας

    def __init__(self, description, destination, weight):
        Package.__init__(self, description, destination)
        self.weight = float(weight[:-2])

    def cost(self):
        price = Package.cost(self) + self.weight * 0.5
        return price

    def __str__(self, invoice=None):
        if Parcel.cost == 1:
            return f"{self.description} :Προορισμός: {self.destination}" \
                   f",Βάρος: {self.weight}kg"
        else:
            return f"{self.description} :Προορισμός: {self.destination}" \
                   f",Βάρος: {self.weight}kg,Κόστος:{Parcel.cost(self)}"


class Envelope(Package):
    # Εδώ συμπληρώνετε τον κώδικά σας

    def __init__(self, description, destination, priority):
        Package.__init__(self, description, destination)
        self.priority = int(priority[-2:])

    def cost(self):
        return Package.cost(self) + self.priority * 0.20

    def __str__(self, invoice=None):
        if invoice == None:
            return f"{self.description} :Προορισμός:{self.destination}," \
                   f"Προτεραιότητα {self.priority}"
        else:
            return f"{self.description} :Προορισμός:{self.destination}," \
                   f"Προτεραιότητα {self.priority},Κόστος: {Envelope.cost(self)}€"


class Bulky_Item(Package):
    # Εδώ συμπληρώνετε τον κώδικά σας

    def __init__(self, description, destination, length, width, height):
        Package.__init__(self, description, destination)
        self.length = float(length[6:-1])
        self.width = float(width[7:-1])
        self.height = float(height[5:-1])

    def cost(self):
        return Package.cost(self) + (self.length * self.width * self.height) * 20

    def __str__(self, invoice=None):
        if invoice == None:
            return f"{self.description} :Προορισμός:{self.destination},Διαστάσεις " \
                   f"{self.length} * {self.width} * {self.height}m"
        else:
            return f"{self.description} :Προορισμός:{self.destination},Διαστάσεις" \
                   f" {self.length} * {self.width} * {self.height}m,Κόστος:{self.cost():.2f}€"


items = '''Πακέτο1 (Αθήνα, 20kg),
Πακέτο2 (Θεσσαλονίκη, 10kg),
Πακέτο3 (Αθήνα, 30kg),
Πακέτο4 (Αθήνα, 4.5kg),
Φάκελος1 (Θεσσαλονίκη, προτεραιότητα 1),
Φάκελος2 (Θεσσαλονίκη, προτεραιότητα 3),
ΟγκώδεςΑντικείμενο1 (Αθήνα, μήκος 0.7μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο2 (Θεσσαλονίκη, μήκος 1μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο3 (Αθήνα, μήκος 2μ, πλάτος 0.7μ, ύψος 0.7μ),
'''


def filter(txt):
    return txt.replace("(", ",").replace(")", "").split(",")


packages = []
for item in items.split("\n"):
    if 'Πακέτο' in item:
        p = filter(item)
        packages.append(Parcel(*p[:3]))
    elif 'Φάκελος' in item:
        p = filter(item)
        packages.append(Envelope(*p[:3]))
    elif 'ΟγκώδεςΑντικείμενο' in item:
        packages.append(Bulky_Item(*filter(item)[:5]))

## εκτυπώσεις
print('Δελτίο αποστολής')
for p in packages:
    print(p)
print(40 * "_" + "\n\n")

print('Τιμολόγιο')
for p in packages:
    print(p.__str__(invoice=True))
print(f"ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {sum([p.cost() for p in packages]):.2f}€")
print(40 * "_" + "\n\n")
