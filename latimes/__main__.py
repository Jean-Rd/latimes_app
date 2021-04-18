import click

@click.command()
@click.argument("cadena_tiempo", type=click.STRING)

def main(cadena_tiempo: str):

    '''
    cadena_tiempo --> Tu tiempo en lenguaje natural(palabras)
    '''

    print("Hola mundo mundial", cadena_tiempo + "!!!")

if __name__ == '__main__':
    main()