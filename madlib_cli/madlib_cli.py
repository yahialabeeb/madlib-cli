from io import FileIO
import re


def read_template(filepath: str):
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return "sorry I can't open the game file"
    else:
        file_content = file.read()
        file.close()

    return file_content.strip()


def parse_template(file_content:str):
    words_describtions = re.findall(r'\{.*?\}', file_content)
    file_content = re.sub(r'\{.*?\}', "{}", file_content)
    return words_describtions, file_content


def merge(user_inputs, file_content: str):
    user_inputs = tuple(user_inputs)
    output = file_content.format(*user_inputs)
    print(output)
    return output


def write_new_file(output):
    with open('madlib_cli/assest/small_example_result.txt', 'w') as rewrite:
        rewrite.write(output)


if __name__ == "__main__":
    game_file = read_template('madlib_cli/assest/small_example.txt')
    if game_file == "sorry I can't open the game file":
        print(game_file)
    else:
        plyer_name = input("let us know your name   > ")
        print(f"Welcome {plyer_name} to Madlib Game\n")
        print("I will asking you to add some word.\nAfter you adding them I will expose them in a nice pargragh\n")
        print("="*35)
        words_describtions, game_file_edit = parse_template(game_file)
        user_inputs = []
        for i in words_describtions:
            q = i.strip("{}")
            user_inputs.append(input(f"Please Type a word as {q}  > "))
        output = merge(user_inputs, game_file_edit)
        write_new_file(output)
