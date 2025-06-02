def decipher(line: list[str]) -> str:
    """Функция дешифровки посланий для марсохода"""
    result = ''
    index = 0
    while index < len(line):
        symb: str = line[index]
        if symb.isdigit():
            result = result + (int(symb) * decipher(line[index + 2:]))
            index += 1
            continue
        elif symb == "[":
            bracket_counter = 1
            while bracket_counter > 0:
                index += 1
                if line[index] == "[":
                    bracket_counter += 1
                if line[index] == "]":
                    bracket_counter -= 1
        elif symb == "]":
            return result
        else:
            result += symb
        index += 1
        return result 
    
    
if __name__ == '__main__':
    line = list(input())
    print(decipher(line))
