from config import WAKE_WORD
from core.listener import Listener
from core.speaker import Speaker
from core.commands import execute_command


def main():
    speaker = Speaker()
    listener = Listener()

    speaker.speak("Sistema JARVIS iniciado.")

    while True:
        text = listener.listen()

        if not text:
            continue

        if WAKE_WORD not in text:
            continue

        command = text.replace(WAKE_WORD, "").strip()

        if not command:
            speaker.speak("Sim?")
            continue

        if command in ["parar", "sair", "desligar", "terminar"]:
            speaker.speak("A encerrar o sistema JARVIS.")
            break

        response = execute_command(command)

        if response:
            speaker.speak(response)
        else:
            speaker.speak(
                "Ainda não tenho um comando para isso."
            )


if __name__ == "__main__":
    main()