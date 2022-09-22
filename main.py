from src.ParticleSystem import ParticleSystem
from src.Point import MassPoint

system = ParticleSystem([
    MassPoint(10, 0, 0, 0),
    MassPoint(10, 1, 0, 0)
])

print(system.massCenter)
