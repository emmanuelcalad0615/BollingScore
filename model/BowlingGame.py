class BowlingGame:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        if len(self.frames) < 10:
            self.frames.append(frame)
        else:
            print("Ya se han jugado los 10 frames, no se pueden agregar más.")

    def calculate_score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            score += frame.score(self.frames[i+1:])
        return score