import webbrowser
from datetime import datetime


def execute_command(command):

    if "que horas" in command or "horas são" in command:
        hora = datetime.now().strftime("%H:%M")
        return f"São {hora}."

    if "abre o google" in command or "abre google" in command:
        webbrowser.open("https://www.google.com")
        return "A abrir o Google."

    if "abre o youtube" in command or "abre youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "A abrir o YouTube."

    if "pesquisa" in command:
        pesquisa = command.replace("pesquisa", "").strip()

        if pesquisa:
            url = (
                "https://www.google.com/search?q="
                + pesquisa.replace(" ", "+")
            )

            webbrowser.open(url)
            return f"A pesquisar por {pesquisa}."

        return "O que queres que eu pesquise?"

    return None