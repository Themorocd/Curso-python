palabra = "cabra"

match (palabra):
    case "cabra":
        print("Bicho que salta y come hierba")
    case "vaca":
        print("Otro bicho con cuernos más grande")
    case _:
        print("No sé qué bicho es")
