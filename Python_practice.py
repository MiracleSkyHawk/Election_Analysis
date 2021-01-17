# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for counti, voter in counties_dict.items():
#     message = (f"{counti} county has {voter:,}")
#     print(message)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for counti in range(len(voting_data)):
    message = (
        f'{voting_data[counti].get("county")} county has'
        f'{voting_data[counti].get("registered_voters"):,}')
    print(message)