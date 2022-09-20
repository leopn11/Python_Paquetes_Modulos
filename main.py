import operaciones.restador.resta as r
import operaciones.sumador.suma as s
import operaciones.divicion.divide as d
import operaciones.multiplicador.multiplica as m



def main():
    resta = r.resta(70, 65)
    suma = s.suma(60, 60)
    divide = d.divicion(80, 4)
    multiplica = m.multiplicacion(50, 10)

    print(r.resta(70, 65))
    print(s.suma(60, 60))
    print(d.divicion(80, 4))
    print(m.multiplicacion(50, 10))



if __name__ == '__main__':
    main()