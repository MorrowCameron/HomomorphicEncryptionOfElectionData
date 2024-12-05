import base64

def write_data(file_name, data):
    # bytes to base64
    data = base64.b64encode(data)

    with open(file_name, 'wb') as f:
        f.write(data)
        f.close()

def read_data(file_name):
    try:
        with open(file_name, 'rb') as f:
            data = f.read()
            f.close()
        # base64 to bytes
        return base64.b64decode(data)
    except FileNotFoundError as e:
        return -1


# Function to convert string to ASCII values
def string_to_ascii(s):
    return [ord(char) for char in s]


# Mapping state names to integer IDs
state_to_id = {
    'Alabama': 1,
    'Alaska': 2,
    'Arizona': 3,
    'Arkansas': 4,
    'California': 5,
    'Colorado': 6,
    'Connecticut': 7,
    'Delaware': 8,
    'Florida': 9,
    'Georgia': 10,
    'Hawaii': 11,
    'Idaho': 12,
    'Illinois': 13,
    'Indiana': 14,
    'Iowa': 15,
    'Kansas': 16,
    'Kentucky': 17,
    'Louisiana': 18,
    'Maine': 19,
    'Maryland': 20,
    'Massachusetts': 21,
    'Michigan': 22,
    'Minnesota': 23,
    'Mississippi': 24,
    'Missouri': 25,
    'Montana': 26,
    'Nebraska': 27,
    'Nevada': 28,
    'New Hampshire': 29,
    'New Jersey': 30,
    'New Mexico': 31,
    'New York': 32,
    'North Carolina': 33,
    'North Dakota': 34,
    'Ohio': 35,
    'Oklahoma': 36,
    'Oregon': 37,
    'Pennsylvania': 38,
    'Rhode Island': 39,
    'South Carolina': 40,
    'South Dakota': 41,
    'Tennessee': 42,
    'Texas': 43,
    'Utah': 44,
    'Vermont': 45,
    'Virginia': 46,
    'Washington': 47,
    'West Virginia': 48,
    'Wisconsin': 49,
    'Wyoming': 50
}

# Reverse mapping: integer ID to state name
id_to_state = {v: k for k, v in state_to_id.items()}


def state_name_to_id(state_name: str) -> int:
    """Convert state name to its corresponding integer ID."""
    state_name = state_name.strip()
    return state_to_id.get(state_name, -1)  # Return -1 if state name not found


def state_id_to_name(state_id: int) -> str:
    """Convert integer ID to the corresponding state name."""
    return id_to_state.get(state_id, "Unknown")  # Return "Unknown" if ID not found
