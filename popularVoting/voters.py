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

