import os
import logging


# Function to print the binary data of each cache file in a readable format
def print_human_readable_cache_data(cache_file):
    decoded_cache_data = {}
    with open(cache_file, "rb") as file:
        file_data = file.read()
        hex_representation = file_data.hex()
        decoded_hex = " ".join(hex_representation[i:i+2] for i in range(0, len(hex_representation), 2))
        decoded_cache_data['hex'] = decoded_hex

        # Attempt to print readable ASCII or UTF-8 text
        try:
            text_data = file_data.decode('utf-8')
            decoded_cache_data['text'] = text_data
        except UnicodeDecodeError:
            # Extract printable ASCII text in ASCII range
            ascii_text = ''.join(
            chr(b) if 32 <= b <= 126 else '.' for b in file_data
            )
            decoded_cache_data['ascii'] = ascii_text
    return decoded_cache_data

if __name__ == "__main__":
    cache_dir = os.path.expanduser("~/.cache/google-chrome/Default/Cache/Cache_Data/")
    for file_name in os.listdir(cache_dir):
        cache_file = os.path.join(cache_dir, file_name)
        print(cache_file)
        if os.path.isfile(cache_file):
            data = print_human_readable_cache_data(cache_file)
            with open('cache_report.txt', 'a') as report:
                for key in data.keys():
                    logging.info(f"fetching data for: {cache_file}")
                    report.write(f"File name: {cache_file}\n")
                    report.write(key + ": " + data[key] + '\n')
                    report.write(f"-------------------\n")

