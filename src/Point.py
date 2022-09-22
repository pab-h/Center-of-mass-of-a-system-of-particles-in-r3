
positionVector = list[float, float, float]

class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f"P({ self.__x }, { self.__y }, { self.__z })"

    def getPosition(self) -> positionVector:
        return [self.__x, self.__y, self.__z]

class MassPoint(Point):
    def __init__(self, mass: float, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.__mass = mass

        if self.mass <= 0:
            raise Exception("mass can't be negative or zero")

    def __str__(self) -> str:
        return f"Pm({ self.__mass }, { self.__x }, { self.__y }, { self.__z })"