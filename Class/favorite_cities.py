class city:
    def __init__(self, name, country, population, landmark):
        self.name = name
        self.country = country
        self.population = int((population + 500) / 1000) * 1000
        self.landmark = landmark if landmark else []
    
Pontianak = city('Kalimantan Barat', 'Indonesia', 690277, ['Sungai Ambawang', 'Sungai Kapuas', 'Singkawang'])
print(vars(Pontianak))