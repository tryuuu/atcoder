def convert_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if key in output_dict:
            output_dict[key].append(value)
        else:
            output_dict[key] = [value]
    return output_dict

# Example usage:
test_data = {500: 'x', 500: 'x', 500: 'x', 500: 'x'}
converted_data = convert_dict(test_data)
print(converted_data)  # Output: {500: ['x', 'x', 'x', 'x']}
