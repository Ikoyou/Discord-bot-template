def english_to_uwu_converter(input_data: str):
    length_of_data = len(input_data)
    output_data = ''

    for i in range(length_of_data):
        current_data = input_data[i]
        previous_data = '&# 092;&# 048;'
        if i > 0:
            previous_data = input_data[i - 1]

        if current_data == 'L' or current_data == 'R':
            output_data += 'W'

        elif current_data == 'l' or current_data == 'r':
            output_data += 'w'
        elif current_data == 'o' or current_data == 'O':
            if previous_data == 'n' or previous_data == 'N' or previous_data == 'm' or previous_data == 'M':
                output_data += 'yo'
            else:
                output_data += current_data
        else:
            output_data += current_data

    return output_data


