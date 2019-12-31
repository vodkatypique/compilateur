def parse():
    with open(input("entrez path du fichier de code : ")) as file:
        pcode = ""
        pcode = "".join(file.readlines()).replace("\t", "").replace("\n", "  ").replace("; ", ";")
        return pcode