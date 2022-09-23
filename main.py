from src.ParticleSystem import ParticleSystem
from src.Point import MassPoint
from random import randrange

def getRandomMassPoint() -> MassPoint:
    return MassPoint(
        randrange(1, 100),
        randrange(1, 100),
        randrange(1, 100),
        randrange(1, 100),
    )

system = ParticleSystem([ getRandomMassPoint() for _ in range(10)])

system.plot()
