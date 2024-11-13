import tenseal as ts
import utils

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coef_mod_bit_sizes = [60, 40, 40, 60]
)

### Key Generation 
context.generate_galois_keys()
context.global_scale = 2**40
secret_context = context.serialize(save_secret_key = True)

utils.write_data("keys/secret.txt", secret_context)
context.make_context_public()

public_context = context.serialize()
utils.write_data("keys/public.txt", public_context)


### Encryption Example
context = ts.context_from(utils.read_data("keys/secret.txt"))
salary = [10000]
salary_encrypted = ts.ckks_vector(context, salary)
utils.write_data("outputs/salary_encrypted.txt", salary_encrypted.serialize())


### Decryption Example
m_proto = utils.read_data("outpus/salary_encrupted_new_with plan_calculations")
m = ts.lazy_ckks_vector_from(m_proto)
round(m.decrypt()[0], 2) 

# Should be around $12,600