import model
from model import frame
from model.frame import Frame
from model.BowlingGame import BowlingGame



def solicitar_pines_tumbados(frame_num, roll_num):
    while True:
        try:
            pins = int(input(f"Ingrese el número de pines tumbados en el lanzamiento {roll_num} del frame {frame_num}: "))
            if pins < 0 or pins > 10:
                print("Por favor, ingrese un número entre 0 y 10.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return pins

def main():
    game = model.BowlingGame.BowlingGame()

    for frame_num in range(1, 11):
        frame = Frame()
        game.add_frame(frame)

        if frame_num < 10:
            print(f"Frame {frame_num}:")
            pins1 = solicitar_pines_tumbados(frame_num, 1)
            frame.add_roll(pins1)
            if pins1 < 10:
                pins2 = solicitar_pines_tumbados(frame_num, 2)
                frame.add_roll(pins2)
        else:
            print("Frame 10:")
            pins1 = solicitar_pines_tumbados(10, 1)
            frame.add_roll(pins1)
            if pins1 == 10 or sum(frame.rolls) == 10:
                print("Lanzamiento extra:")
                pins2 = solicitar_pines_tumbados(10, 2)
                frame.add_roll(pins2)
                if pins2 == 10 and (pins1 == 10 or sum(frame.rolls) == 10):
                    print("Segundo lanzamiento extra:")
                    pins3 = solicitar_pines_tumbados(10, 3)
                    frame.add_roll(pins3)

    score = game.calculate_score()
    print("Puntaje total:", score)

if __name__ == "__main__":
    main()