import tenseal as ts
import utils

context = ts.context_from(utils.read_data("./keys/public.txt"))

### Initialize the tally vector
tally = ts.ckks_vector(context, [0])
current = "0"

while True:
    # Try to load current encrypted voter
    encrypted_voter_proto = utils.read_data(f"./outputs/encryptedVotes/voter" + current)
    if encrypted_voter_proto == -1:
        break
    encrypted_voter = ts.lazy_ckks_vector_from(encrypted_voter_proto)
    encrypted_voter.link_context(context)  # Link context to the encrypted data
    # Aggregate votes without decrypting
    tally += encrypted_voter
    current = str(int(current) + 1)

### Write the votes
utils.write_data("./outputs/tally", tally.serialize())
