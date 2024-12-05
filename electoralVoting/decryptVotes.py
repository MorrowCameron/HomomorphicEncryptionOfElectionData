import tenseal as ts
import utils
context = ts.context_from(utils.read_data("./keys/secret.txt"))

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
    'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina',
    'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin', 'Wyoming']

current = "0"
for state in states: 
    decrypted_voters = []
    ### Decrypt the votes (voters should be able to see their votes)
    while True:
        encrypted_voter_proto = utils.read_data("./outputs/encryptedVotes/" + state + "/voter" + current)
        if encrypted_voter_proto == -1:
            break
        encrypted_voter = ts.lazy_ckks_vector_from(encrypted_voter_proto)
        encrypted_voter.link_context(context)  # Grab each encrypted voter entry
        decrypted_voter = encrypted_voter.decrypt()  # decrypt the voter entry

        decrypted_vote = decrypted_voter[:2]  # Extract the votes
        demo = round(decrypted_vote[0], 0)
        rep = round(decrypted_vote[0], 0)
        if demo:
            decrypted_vote = "Democrat"
        else:
            decrypted_vote = "Republican"

        decrypted_state = utils.state_id_to_name(int(abs(round(decrypted_voter[2], 2))))  # Extract the state

        decrypted_uuid_ascii = decrypted_voter[3:]  # Extract UUID ascii
        decrypted_uuid = ''.join([chr(int(abs(round(x, 2)))) for x in decrypted_uuid_ascii])  ## Convert the the UUID to str

        decrypted_voters.append((decrypted_uuid, decrypted_state, decrypted_vote))  ## Rebuild voter information

        current = str(int(current) + 1)
        
    ### Print the original voter information
    for decrypted_voter in decrypted_voters:
        print(decrypted_voter[0], decrypted_voter[1], decrypted_voter[2])