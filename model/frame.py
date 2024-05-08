


class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self):
        return len(self.rolls) == 1 and sum(self.rolls) == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self, next_frames):
        frame_score = sum(self.rolls)
        if self.is_strike():
            if len(next_frames) >= 2 and next_frames[0].is_strike():
                frame_score += next_frames[0].rolls[0] + next_frames[1].rolls[0]
            elif len(next_frames) >= 1:
                frame_score += sum(next_frames[0].rolls[:2])
        elif self.is_spare():
            if next_frames:
                frame_score += next_frames[0].rolls[0]
        return frame_score


