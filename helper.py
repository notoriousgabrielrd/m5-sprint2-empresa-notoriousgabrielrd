class Helpers:
    @staticmethod
    def helper_func(nome: str):
        new_name = nome.lower().split()
        return "_".join(new_name)

    @staticmethod
    def helper_title(nome: str):
        new_name = nome.title().split()
        return "".join(new_name)

    @staticmethod
    def helper_name_title(nome: str):
        new_name = nome.title().split()
        return " ".join(new_name)
