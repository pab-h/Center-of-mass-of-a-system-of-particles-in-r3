
positionVector = list[float, float, float]

class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f"P({ self.__x }, { self.__y }, { self.__z })"

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def z(self) -> float:
        return self.__z

class MassPoint(Point):
    def __init__(self, mass: float, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z)
        self.__mass = mass

        if self.__mass <= 0:
            raise Exception("mass can't be negative or zero")

    @property
    def mass(self) -> float:
        return self.__mass

    def __str__(self) -> str:
        return f"Pm({ self.__mass }, { self.x }, { self.y }, { self.z })"