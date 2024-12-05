import tenseal as ts
import utils
context = ts.context_from(utils.read_data("./keys/secret.txt"))

### Decrypt tally
tally = utils.read_data("./outputs/tally")
encrypted_tally = ts.lazy_ckks_vector_from(tally)
encrypted_tally.link_context(context)
decrypted_democrat_tally = encrypted_tally.decrypt()[0]
decrypted_republican_tally = encrypted_tally.decrypt()[1]

print("Democratic Votes:", (int(abs(round(decrypted_democrat_tally, 0)))))
print("Republican Votes:", (int(abs(round(decrypted_republican_tally, 0)))))