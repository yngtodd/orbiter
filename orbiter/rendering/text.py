class GameText:

    def __init__(self):
        self.intro_text = [
          ' The Mars Orbiter experienced an error during Orbit insertion.',
          ' Use thrusters to correct to a circular mapping orbit without',
          ' running out of fuel or burning up in the atmosphere.'
        ]

        self.instruct_text0 = [
          'Orbital altitude must be within 69-120 miles',
          'Orbital Eccentricity must be < 0.05',
          'Avoid top of atmosphere at 68 miles'
        ]

        self.instruct_text1 = [
          'Left Arrow = Decrease Dx',
          'Right Arrow = Increase Dx',
          'Up Arrow = Decrease Dy',
          'Down Arrow = Increase Dy',
          'Space Bar = Clear Path',
          'Escape = Exit Full Screen'
        ]
