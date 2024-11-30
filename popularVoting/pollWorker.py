import tenseal as ts
import utils

context = ts.context_from(utils.read_data("./keys/public.txt"))

### Initialize the tally vectors
democrat_tally = ts.ckks_vector(context, [0])
republican_tally = ts.ckks_vector(context, [0])

current = "0"

while True:
    # Try to load Democrat vote
    encrypted_voter_proto = utils.read_data(f"./outputs/encryptedVotes/demo{current}")
    if encrypted_voter_proto != -1:
        encrypted_voter = ts.lazy_ckks_vector_from(encrypted_voter_proto)
        encrypted_voter.link_context(context)  # Link context to the encrypted data
        democrat_tally += encrypted_voter
    else:
        # If no more Democrat votes, try Republican vote
        encrypted_voter_proto = utils.read_data(f"./outputs/encryptedVotes/rep{current}")
        if encrypted_voter_proto == -1:
            break  # If no more votes, exit loop
        republican_tally += ts.plain_tensor([1])

    current = str(int(current) + 1)

### Write the votes
utils.write_data("./outputs/democratic_tally", democrat_tally.serialize())
utils.write_data("./outputs/republican_tally", republican_tally.serialize())
