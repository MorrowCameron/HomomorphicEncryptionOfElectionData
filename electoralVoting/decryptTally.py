import tenseal as ts
import utils
context = ts.context_from(utils.read_data("./keys/secret.txt"))

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
    'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina',
    'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin', 'Wyoming']

state_to_winner = {
    'Alabama': "",
    'Alaska': "",
    'Arizona': "",
    'Arkansas': "",
    'California': "",
    'Colorado': "",
    'Connecticut': "",
    'Delaware': "",
    'Florida': "",
    'Georgia': "",
    'Hawaii': "",
    'Idaho': "",
    'Illinois': "",
    'Indiana': "",
    'Iowa': "",
    'Kansas': "",
    'Kentucky': "",
    'Louisiana': "",
    'Maine': "",
    'Maryland': "",
    'Massachusetts': "",
    'Michigan': "",
    'Minnesota': "",
    'Mississippi': "",
    'Missouri': "",
    'Montana': "",
    'Nebraska': "",
    'Nevada': "",
    'NewHampshire': "",
    'NewJersey': "",
    'NewMexico': "",
    'NewYork': "",
    'NorthCarolina': "",
    'NorthDakota': "",
    'Ohio': "",
    'Oklahoma': "",
    'Oregon': "",
    'Pennsylvania': "",
    'RhodeIsland': "",
    'SouthCarolina': "",
    'SouthDakota': "",
    'Tennessee': "",
    'Texas': "",
    'Utah': "",
    'Vermont': "",
    'Virginia': "",
    'Washington': "",
    'WestVirginia': "",
    'Wisconsin': "",
    'Wyoming': ""
}

state_to_electoral_votes = {
    'Alabama': 9,
    'Alaska': 3,
    'Arizona': 11,
    'Arkansas': 6,
    'California': 54,
    'Colorado': 10,
    'Connecticut': 7,
    'Delaware': 3,
    'Florida': 30,
    'Georgia': 16,
    'Hawaii': 4,
    'Idaho': 4,
    'Illinois': 19,
    'Indiana': 11,
    'Iowa': 6,
    'Kansas': 6,
    'Kentucky': 8,
    'Louisiana': 8,
    'Maine': 4,
    'Maryland': 10,
    'Massachusetts': 11,
    'Michigan': 15,
    'Minnesota': 10,
    'Mississippi': 6,
    'Missouri': 10,
    'Montana': 4,
    'Nebraska': 5,
    'Nevada': 6,
    'NewHampshire': 4,
    'NewJersey': 14,
    'NewMexico': 5,
    'NewYork': 28,
    'NorthCarolina': 16,
    'NorthDakota': 3,
    'Ohio': 17,
    'Oklahoma': 7,
    'Oregon': 8,
    'Pennsylvania': 19,
    'RhodeIsland': 4,
    'SouthCarolina': 9,
    'SouthDakota': 3,
    'Tennessee': 11,
    'Texas': 40,
    'Utah': 6,
    'Vermont': 3,
    'Virginia': 13,
    'Washington': 12,
    'WestVirginia': 4,
    'Wisconsin': 10,
    'Wyoming': 3
}
democratVotes = 0
republicanVotes = 0
tieVotes = 0

print("Votes per state for Democrats and Republicans")
print("\n================================================\n")

### Decrypt tally
for state in states: 
    tally = utils.read_data("./outputs/" + state + "_tally")
    encrypted_tally = ts.lazy_ckks_vector_from(tally)
    encrypted_tally.link_context(context)
    decrypted_democrat_tally = encrypted_tally.decrypt()[0]
    decrypted_republican_tally = encrypted_tally.decrypt()[1]

    print(state + " Democratic Votes:", (int(abs(round(decrypted_democrat_tally, 0)))))
    print(state + " Republican Votes:", (int(abs(round(decrypted_republican_tally, 0)))))
    print()

    if((int(abs(round(decrypted_democrat_tally, 0)))) > (int(abs(round(decrypted_republican_tally, 0))))):
        state_to_winner[state] = "Democrat"
        democratVotes += state_to_electoral_votes[state]
    elif ((int(abs(round(decrypted_republican_tally, 0)))) > (int(abs(round(decrypted_democrat_tally, 0))))):
        state_to_winner[state] = "Republican"
        republicanVotes += state_to_electoral_votes[state]
    else:
        state_to_winner[state] = "Tie"
        tieVotes += state_to_electoral_votes[state]


print("Final Vote Tallies")
print("\n================================================\n")

print("Democrat votes: " + str(democratVotes))
print("Republican votes: " + str(republicanVotes))
print("Tied votes: " + str(tieVotes))
    

