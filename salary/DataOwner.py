import tenseal as ts
import utils

### Encryption Example (Then we can use these keys to encrypt)
context = ts.context_from(utils.read_data("./keys/secret.txt"))
### Lets encrypt $10,000 salary
salary = [10000]
salary_encrypted = ts.ckks_vector(context, salary)
salary_encrypted_proto = salary_encrypted.serialize()
utils.write_data("./outputs/salary_encrypted.txt", salary_encrypted_proto)


### Decryption Example (Lets decrypt a salary from our example)
m_proto = utils.read_data("./outputs/salary_encrypted.txt")
m = ts.lazy_ckks_vector_from(m_proto)
m.link_context(context)
### Before performing operation on encrypted data, we expect our salary to be $10,000
print(round(m.decrypt()[0], 2))

### Decrypting the modified salary (should be $12,600)
m_proto = utils.read_data("./outputs/salary_encrypted_new_with_plain_calculations.txt")
m = ts.lazy_ckks_vector_from(m_proto)
m.link_context(context)
print(round(m.decrypt()[0], 2))
