import tenseal as ts 
import utils

context = ts.context_from(utils.read_data("keys/public.txt"))

### Calcualtions
salary_proto = utils.read_data("outputs/salary_encrypted.txt")
salary_encrypted = ts.lazy_ckks_vector_from(salary_proto)
salary_encrypted.link_context (context)

# Wage increase 20% 
wage_increase_rate_plain = ts. plain_tensor ([1.2])

# Bonus 600 USD
bonus_increase_rate_plain = ts.plain_tensor([600])

# Do operations
salary_new_encrypted = (salary_encrypted * wage_increase_rate_plain) + bonus_increase_rate_plain
utils.write_data("outputs/salary_encrypted_new_with_plain_calculations.txt", salary_new_encrypted.serialize())