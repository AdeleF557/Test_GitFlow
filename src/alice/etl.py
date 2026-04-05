def extract():
    """Extrait les données depuis la source."""
    data = {"records": [1, 2, 3]}
    print("Extraction des données...")
    return data

def transform(data):
    """Applique les transformations métier sur les données brutes."""
    transformed = {k: [x * 2 for x in v] for k, v in data.items()}
    print("Transformation des données...")
    return transformed

def load(data):
    """Charge les données transformées en destination."""
    print(f"Chargement de {len(data)} enregistrements...")
    return True
