from functools import reduce
from src.Point import MassPoint
from src.Point import Point
import matplotlib.pyplot as pyplot

class ParticleSystem:
    def __init__(self, particles: list[MassPoint] = []) -> None:
        self.__particles = particles
        self.__massCenter: Point = Point(0, 0, 0)
        self.__systemMass: float = 0
        self.__update()

    def __update(self) -> None:
        self.__systemMass = self.calcSystemMass()
        self.__massCenter = self.calcMassCenter()

    def addParticles(self, particles: list[MassPoint]) -> None:
        self.__particles.extend(particles)
        self.__update()

    def calcMassCenter(self) -> Point:
        def reduceX(accumulated: float, massPoint: MassPoint) -> float:
            return accumulated + massPoint.mass * massPoint.x

        def reduceY(accumulated: float, massPoint: MassPoint) -> float:
            return accumulated + massPoint.mass * massPoint.y

        def reduceZ(accumulated: float, massPoint: MassPoint) -> float:
            return accumulated + massPoint.mass * massPoint.z

        return Point(
            x = reduce(reduceX, self.__particles, 0) / self.__systemMass,
            y = reduce(reduceY, self.__particles, 0) / self.__systemMass,
            z = reduce(reduceZ, self.__particles, 0) / self.__systemMass
        )

    def calcSystemMass(self) -> float:
        def reduceMassParticles(accumulated: float, current: MassPoint) -> float:
            return accumulated + current.mass

        return reduce(reduceMassParticles, self.__particles, 0)

    def plot(self) -> None:
        figure = pyplot.figure(figsize=(4, 4))
        axes = figure.add_subplot(111, projection="3d")
        axes.scatter(2, 3, 4)

        pyplot.show()

    @property
    def massCenter(self) -> Point:
        return self.__massCenter

