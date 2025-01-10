print("start mammals")

# primates = ["Monkeys", "Apes", "Humans"]
# carnivores = ["Lions", "Tigers", "Bears", "Wolves"]
# rodents = ["Rats", "Mice", "Squirrels"]
# cetaceans = ["Whales", "Dolphins", "Porpoises"]
# even_toed_ungulates = ["Cows", "Deer", "Giraffes"]
# odd_toed_ungulates = ["Horses", "Zebras", "Rhinoceroses"]
# bats = ["Bats"]
# lagomorphs = ["Rabbits", "Hares"]
# insectivores = ["Hedgehogs", "Moles", "Shrews"]
# elephants = ["Elephants"]
# marsupials = ["Kangaroos", "Koalas", "Wombats", "Opossums", "Tasmanian Devils"]
# monotremes = ["Platypus", "Echidnas (Spiny Anteaters)"]

mammals = {
    "Placental Mammals": {
        "Primates": ["Monkeys", "Apes", "Humans"],
        "Carnivores": ["Lions", "Tigers", "Bears", "Wolves"],
        "Rodents": ["Rats", "Mice", "Squirrels"],
        "Cetaceans": ["Whales", "Dolphins", "Porpoises"],
        "Ungulates": {
            "Even-toed": ["Cows", "Deer", "Giraffes"],
            "Odd-toed": ["Horses", "Zebras", "Rhinoceroses"],
        },
        "Bats": ["Bats"],
        "Lagomorphs": ["Rabbits", "Hares"],
        "Insectivores": ["Hedgehogs", "Moles", "Shrews"],
        "Elephants": ["Elephants"],
    },
    "Marsupials": ["Kangaroos", "Koalas", "Wombats", "Opossums", "Tasmanian Devils"],
    "Monotremes": ["Platypus", "Echidnas (Spiny Anteaters)"],
}

# 출력 예시
# print(mammals["Placental Mammals"]["Primates"])  # ["Monkeys", "Apes", "Humans"]
# print(mammals["Marsupials"])  # ["Kangaroos", "Koalas", "Wombats", "Opossums", "Tasmanian Devils"]
# print(mammals["Monotremes"])  # ["Platypus", "Echidnas (Spiny Anteaters)"]