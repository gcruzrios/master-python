import clases

persona = clases.Persona()

persona.setNombre("Victor")
persona.setApellidos("Robles")
persona.setAltura("190 cm")
persona.setEdad("166 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()} {persona.getAltura()} {persona.getEdad()}")
print(persona.hablar())
print("----------------------------------------------------------------")
informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Perez")
informatico.setAltura("178 cm")
informatico.setEdad("166 años")

print(f"La persona informatico es: {informatico.getNombre()} {informatico.getApellidos()} {informatico.getAltura()} {informatico.getEdad()}")

print(informatico.getLenguajes())
print(informatico.caminar())
print("----------------------------------------------------------------")

tecnico = clases.TecnicoRedes()

tecnico.setNombre("Manolo")

print(tecnico.auditarRedes, tecnico.getNombre())