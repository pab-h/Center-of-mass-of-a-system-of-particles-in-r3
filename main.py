from src.ParticleSystem import ParticleSystem
from src.Point import MassPoint

system = ParticleSystem([
    MassPoint(10, 1, 1, 1)
])

system.addParticles([
    MassPoint(10, 2, 2, 2)
])

print(system.massCenter)



