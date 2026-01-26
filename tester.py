def count_bad_inputs(filename):
    bad_inputs_count = 0
    total_lines = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                total_lines += 1
                try:
                    # Attempt to convert the line to a float (or int, depending on your data)
                    float(line.strip())
                except ValueError:
                    # If conversion fails, it's a "bad input"
                    bad_inputs_count += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

    print(f"Total lines processed: {total_lines}")
    print(f"Number of bad inputs: {bad_inputs_count}")
    return bad_inputs_count

# Example usage with a file named 'data.txt'
# Assume 'data.txt' contains:
# 10.5
# 20
# invalid
# 30.2
# error
# 45

filename = 'data.txt'
count_bad_inputs(filename)