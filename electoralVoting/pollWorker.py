import tenseal as ts
import utils

context = ts.context_from(utils.read_data("./keys/public.txt"))

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
    'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina',
    'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin', 'Wyoming']

current = "0"
for state in states: 
    ### Initialize the tally vector
    tally = ts.ckks_vector(context, [0])

    while True:
        # Try to load current encrypted voter
        encrypted_voter_proto = utils.read_data(f"./outputs/encryptedVotes/" + state + "/voter" + current)
        if (encrypted_voter_proto == -1):
            break
        encrypted_voter = ts.lazy_ckks_vector_from(encrypted_voter_proto)
        encrypted_voter.link_context(context)  # Link context to the encrypted data
        # Aggregate votes without decrypting
        tally += encrypted_voter
        current = str(int(current) + 1)

    ### Write the votes
    utils.write_data("./outputs/" + state + "_tally", tally.serialize())
