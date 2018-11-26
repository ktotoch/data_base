def add_value(key: str, value: str) -> None:  # добавит нововую пары ключ:значение
    with open("example.db") as file:
        for line in file:
            if key + ":" in line:
                raise KeyError("Key already exists")  # вызываем исключение, если ключ уже существует
    with open("example.db", "a") as file:  # записываем новую пару в "черновик"
        file.write(f"{key}:{value}\n")  # (в этом файле не будут отражаться измененные впоследствии значения)
    with open("modified_example.db", "a") as file:  # и в "чистовик"
        file.write(f"{key}:{value}\n")  # (в этом файле будут отражаться измененные значения)


def modify_value(key: str, value: str) -> None:  # изменит значение, связанное с ключом
    with open("example.db", "r") as file:
        with open("modified_example.db", "w") as new_file:  # создаем новый файл, в котором будут измененные данные
            for line in file:
                if key + ":" in line:
                    new_file.write(line.replace(line.split(":")[1], value + "\n"))
                else:
                    new_file.write(line)


# def remove_value(key: str) -> None:  # удалит пару ключ:значение
#     with open("example.db", "r") as file:
#         with open("modified_example.db", "w") as new_file:
#             for line in file:
#                 if key + ":" in line:
#                     new_file.write(line.replace(line, ""))
#                 else:
#                     new_file.write(line)


def get_value(key: str) -> str:  # выведет на экран значение, ассоциированное с ключом
    with open("modified_example.db") as file:
        for line in file:
            if key + ":" in line:
                return line.split(":")[1].replace("\n", "")


add_value("planet1", "Mercury")
add_value("planet2", "Venus")
add_value("planet3", "Earth")
add_value("planet4", "Mars")
add_value("planet5", "Jupiter")
add_value("planet6", "???")
modify_value("planet6", "Saturn")
add_value("planet7", "Uranus")
add_value("planet8", "Neptune")
add_value("planet9", "Pluto")
# remove_value("planet9")
