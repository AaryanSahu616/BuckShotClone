import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class BuckshotClone(QWidget):
    def __init__(self):
        super().__init__()

        self.lives_p1 = 6
        self.lives_p2 = 6

        self.turn = random.choice([1, 2])

        self.initUI()
        self.load_magazine()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label_lives = QLabel(f"Lives of Player 1: {self.lives_p1} | Lives of Player 2: {self.lives_p2}", self)
        self.layout.addWidget(self.label_lives)

        self.label_turn = QLabel(f"Player {self.turn}'s Turn", self)
        self.layout.addWidget(self.label_turn)

        self.button_target_opponent = QPushButton('Shoot Opponent', self)
        self.button_target_opponent.clicked.connect(lambda: self.take_turn(1))
        self.layout.addWidget(self.button_target_opponent)

        self.button_target_self = QPushButton('Shoot Yourself', self)
        self.button_target_self.clicked.connect(lambda: self.take_turn(2))
        self.layout.addWidget(self.button_target_self)

        self.setLayout(self.layout)
        self.setWindowTitle('Buckshot Clone')
        self.show()

    def update_lives_label(self):
        self.label_lives.setText(f"Lives of Player 1: {self.lives_p1} | Lives of Player 2: {self.lives_p2}")

    def update_turn_label(self):
        self.label_turn.setText(f"Player {self.turn}'s Turn")

    def rand_ammo(self):
        ammo_sets = [1, 2, 3, 4, 5]
        Ch = random.choice(ammo_sets)
        if Ch == 1:
            return 1, 1
        elif Ch == 2:
            return 2, 3
        elif Ch == 3:
            return 5, 3
        elif Ch == 4:
            return 4, 4
        elif Ch == 5:
            return 1, 5

    def load_magazine(self):
        self.magazine = []
        L, B = self.rand_ammo()
        while L > 0 or B > 0:
            if L > 0 and B > 0:
                ch = random.choice(['L', 'B'])
                if ch == 'B':
                    B -= 1
                else:
                    L -= 1
                self.magazine.append(ch)
            elif L == 0 and B > 0:
                self.magazine.extend(['B'] * B)
                B = 0
            elif B == 0 and L > 0:
                self.magazine.extend(['L'] * L)
                L = 0
        QMessageBox.information(self, "Magazine Info", f"LIVE AMMOS: {self.magazine.count('L')}\nBLANK AMMOS: {self.magazine.count('B')}")

    def take_turn(self, target):
        if not self.magazine:
            self.load_magazine()

        bullet = self.magazine.pop(0)

        if self.turn == 1:
            if target == 2 and bullet == 'L':
                self.lives_p1 -= 1
                QMessageBox.information(self, "Shot", "Player 1 is shot")
            elif target == 1 and bullet == 'B':
                QMessageBox.information(self, "Shot", "It was a blank bullet")
            elif target == 2 and bullet == 'B':
                QMessageBox.information(self, "Shot", "It was a blank bullet")
            else:
                self.lives_p2 -= 1
                QMessageBox.information(self, "Shot", "Player 2 is shot")
            self.turn = 2
        else:
            if target == 2 and bullet == 'L':
                self.lives_p2 -= 1
                QMessageBox.information(self, "Shot", "Player 2 is shot")
            elif target == 1 and bullet == 'B':
                QMessageBox.information(self, "Shot", "It was a blank bullet")
            elif target == 2 and bullet == 'B':
                QMessageBox.information(self, "Shot", "It was a blank bullet")
            else:
                self.lives_p1 -= 1
                QMessageBox.information(self, "Shot", "Player 1 is shot")
            self.turn = 1

        self.update_lives_label()
        self.update_turn_label()

        if self.lives_p1 == 0:
            QMessageBox.information(self, "Game Over", "Player 2 Won")
            self.close()
        elif self.lives_p2 == 0:
            QMessageBox.information(self, "Game Over", "Player 1 Won")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BuckshotClone()
    sys.exit(app.exec_())
