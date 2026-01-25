class pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = int(entry)
        self.name = str(name)
        self.types = types if types else []
        self.description = str(description)
        self.is_caught = bool(is_caught)
    
    def speak(self):
        print(f'{self.name} '* 2)

    def display_details(self):
        print(f'Entry Number: {self.entry}')
        print(f'Name: {self.name}')
        print(f'Type: {self.types}')
        print(f'Description: {self.description}')
        if self.is_caught == True:
            print(f'{self.name} has already been caught!')
        else:
            print(f'{self.name} has not been caught yet!')

venusaur = pokemon(2, 'Venusaur', ['Grass', 'Poison'], 'While it basks in the sun, it can convert the light into energy. As a result, it is more powerful in the summertime.', True)
venusaur.speak()

Terapagos = pokemon(1024, 'Terapagos', 'Normal', 'Terapagos protects itself using its power to transform energy into hard crystals. This Pokémon is the source of the Terastal phenomenon.', False)
Terapagos.display_details()