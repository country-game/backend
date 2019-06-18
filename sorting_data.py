def get_GPD_per_capitla_data():
    """
    Organizes the data that was copy and pasted from the site.
    :return: none
    """
    with open("raw_data.txt") as text_file:
        contents = text_file.read()
    lines_weird = contents.split("\\n")
    lines = []
    for line in lines_weird:
        lines.append(line)
    for line in lines:
        print("")
        print(line)
        print("")


get_GPD_per_capitla_data()
