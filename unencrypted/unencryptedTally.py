import pandas as pd
import time

df = pd.read_csv('../voting_data.csv')

start_time = time.time()

vote_tally = df['Vote'].value_counts().to_dict()

end_time = time.time()

# Print the results
print(f"Democrat votes: {vote_tally.get('Democrat', 0)}")
print(f"Republican votes: {vote_tally.get('Republican', 0)}")
print(f"Time taken: {end_time - start_time:.5f} seconds")
