import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\n {usuario[1]}, vamos a crear una nota")

        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:

            print(f"\n Perfecto, has guardado la nota: {nota.titulo}" )

        else:    

            print(f"\n No se ha guardado la nota, lo sentimos {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nUsuario {usuario[1]}, tus notas son: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:

            print("**************************************************")
            print(nota[2])
            print(nota[3])
    def borrar(self, usuario):
        print(f" OK, {usuario[1]} vamos a Borrar notas") 

        titulo = input("Ingrese el titulo de la nota a borrar: ") 

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f" Se ha borrado la nota {nota.titulo}") 
        else:
            print("No se ha borrado la nota, prueba luego...")