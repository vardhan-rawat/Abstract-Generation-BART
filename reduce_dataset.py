import os

input_file = "TRAIN/VALIDATION FILE PATH"
output_file = 'OUTPUT_FILE_NAME.jsonl'
limit_bytes = "DESIRED MEMORY TO REDUCE"

def process_large_jsonl(input_file, output_file, limit_bytes):
    bytes_written = 0
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while bytes_written < limit_bytes:
            line = infile.readline()
            if not line:
                break
            if bytes_written + len(line) > limit_bytes:
                break
            outfile.write(line)
            bytes_written += len(line)

process_large_jsonl(input_file, output_file, limit_bytes)
