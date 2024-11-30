import tenseal as ts
import pandas as pd
import utils

context = ts.context_from(utils.read_data("./keys/secret.txt"))
'''
### !!! CAREFUL RUNNING THIS. IT CREATES 1000 VOTER ENCRYPTED FILES !!!
### Read in voting data
df = pd.read_csv('../voting_data.csv')
current = "0"

### Encrypt each vote
for index, row in df.iterrows():
    ### Use index 0 for Democrats and index 1 for Republicans
    vote = (0, 0)
    vote = (1, 0) if row['Vote'] == 'Democrat' else (0, 1)
    state = utils.state_name_to_id(row['State'])  # Get state from voter

    voter_uuid = row['UUID']  # Get UUID from voter
    # Convert UUID to ASCII values
    uuid_ascii = utils.string_to_ascii(voter_uuid)

    voter_encrypted = ts.ckks_vector(context, [vote[0], vote[1]] + [state] + uuid_ascii)  # store as vector [vote, state, uuid]
    voter_encrypted_proto = voter_encrypted.serialize()
    utils.write_data("./outputs/encryptedVotes/voter" + current, voter_encrypted_proto)
    current = str(int(current) + 1)


current = "0"
decrypted_voters = []
### Decrypt the votes (voters should be able to see their votes)
while True:
    encrypted_voter_proto = utils.read_data("./outputs/encryptedVotes/voter" + current)
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
'''
### Decrypt tally
tally = utils.read_data("./outputs/tally")
encrypted_tally = ts.lazy_ckks_vector_from(tally)
encrypted_tally.link_context(context)
decrypted_democrat_tally = encrypted_tally.decrypt()[0]
decrypted_republican_tally = encrypted_tally.decrypt()[1]

print("Democratic Votes:", (int(abs(round(decrypted_democrat_tally, 0)))))
print("Republican Votes:", (int(abs(round(decrypted_republican_tally, 0)))))
