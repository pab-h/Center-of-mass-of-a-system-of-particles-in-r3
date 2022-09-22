from src.Point import MassPoint
from src.Point import Point

class ParticleSystem:
    def __init__(self, particles: list[MassPoint] = []) -> None:
        self.__particles = particles
        self.__massCenter = self.calcMassCenter()

    def addParticles(self, particles: list[MassPoint]) -> None:
        self.__particles.extend(particles)
        self.__massCenter = self.calcMassCenter()

    def calcMassCenter(self) -> Point:
        return Point(10, 10, 10)

    @property
    def massCenter(self) -> Point:
        return self.__massCenter

