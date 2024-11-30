import tenseal as ts
import pandas as pd
import utils

context = ts.context_from(utils.read_data("./keys/secret.txt"))

### !!! CAREFUL RUNNING THIS. IT CREATES 1000 VOTER ENCRYPTED FILES !!!
### Read in voting data
df = pd.read_csv('../voting_data.csv')
current = "0"

### Encrypt each vote
for index, row in df.iterrows():
    ### Use 1 for Democrats and 0 for Republicans
    vote = 1 if row['Vote'] == 'Democrat' else 0
    state = utils.state_name_to_id(row['State'])  # Get state from voter

    voter_uuid = row['UUID']  # Get UUID from voter
    # Convert UUID to ASCII values
    uuid_ascii = utils.string_to_ascii(voter_uuid)

    voter_encrypted = ts.ckks_vector(context, [vote, state] + uuid_ascii)  # store as vector [vote, state, uuid]
    voter_encrypted_proto = voter_encrypted.serialize()
    if vote == 1:
        utils.write_data("./outputs/encryptedVotes/demo" + current, voter_encrypted_proto)
    else:
        utils.write_data("./outputs/encryptedVotes/rep" + current, voter_encrypted_proto)
    current = str(int(current) + 1)


current = "0"
decrypted_voters = []
### Decrypt the votes (voters should be able to see their votes)
while True:
    encrypted_voter_proto = utils.read_data("./outputs/encryptedVotes/demo" + current)
    if encrypted_voter_proto == -1:
        encrypted_voter_proto = utils.read_data("./outputs/encryptedVotes/rep" + current)
        if encrypted_voter_proto == -1:
            break
    encrypted_voter = ts.lazy_ckks_vector_from(encrypted_voter_proto)
    encrypted_voter.link_context(context)  # Grab each encrypted voter entry
    decrypted_voter = encrypted_voter.decrypt()  # decrypt the voter entry

    decrypted_vote = abs(round(decrypted_voter[0], 2))  # Extract the vote
    if decrypted_vote == 1.0:
        decrypted_vote = "Democrat"
    else:
        decrypted_vote = "Republican"

    decrypted_state = utils.state_id_to_name(int(abs(round(decrypted_voter[1], 2))))  # Extract the state

    decrypted_uuid_ascii = decrypted_voter[2:]  # Extract UUID ascii
    decrypted_uuid = ''.join([chr(int(abs(round(x, 2)))) for x in decrypted_uuid_ascii])  ## Convert the the UUID to str

    decrypted_voters.append((decrypted_uuid, decrypted_state, decrypted_vote))  ## Rebuild voter information

    current = str(int(current) + 1)

### Print the original voter information
for decrypted_voter in decrypted_voters:
    print(decrypted_voter[0], decrypted_voter[1], decrypted_voter[2])

### Decrypt democratic tally
democrat_tally = utils.read_data("./outputs/democratic_tally")
encrypted_democrat_tally = ts.lazy_ckks_vector_from(democrat_tally)
encrypted_democrat_tally.link_context(context)
decrypted_democrat_tally = encrypted_democrat_tally.decrypt()[0]

### Decrypt republican tally
republican_tally = utils.read_data("./outputs/republican_tally")
encrypted_republican_tally = ts.lazy_ckks_vector_from(republican_tally)
encrypted_republican_tally.link_context(context)
decrypted_republican_tally = encrypted_republican_tally.decrypt()[0]

print("Democratic Votes:", (int(abs(round(decrypted_democrat_tally, 0)))))
print("Republican Votes:", (int(abs(round(decrypted_republican_tally, 0)))))
