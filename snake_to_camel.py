def snake_to_camel(palabra):
        return ''.join(x.capitalize() or '_' for x in palabra.split('_'))

print(snake_to_camel('diplomado_phyton_hoy'))