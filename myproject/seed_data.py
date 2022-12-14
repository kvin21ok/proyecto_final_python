from ejemplo.models import (Familiar, Mascota, Empleo)

Familiar(nombre= 'Kevin', direccion= 'Ayacucho 1892', numero_pasaporte= 123456789).save()
Familiar(nombre= 'Carlitos', direccion= 'Azcuenaga 1882', numero_pasaporte= 987654321).save()
Familiar(nombre= 'Maria', direccion= 'Pringles 2121', numero_pasaporte= 21222324).save()
Familiar(nombre= 'Juana', direccion= 'Rivadavia 882', numero_pasaporte= 192837645).save()
print('Los familiares DE PRUEBA fueron cargados con exito')

Mascota(nombre = 'Firulais' , tipo = 'Perro', edad = 5).save()
Mascota(nombre = 'Morrongo', tipo = 'Gato', edad = 8).save()
Mascota(nombre = 'Filomena', tipo = 'Pez', edad = 2).save()
Mascota(nombre = 'Jacinto', tipo = 'Loro', edad = 4).save()
print('Las mascotas DE PRUEBA fueron cargadas con exito')

Empleo(ocupacion = 'albañil', antiguedad = 15, cargo = 'ayudante', breve_descripcion = 'mantener mojados los ladrillos').save()
Empleo(ocupacion = 'maestranza', antiguedad = 5, cargo = 'preceptor', breve_descripcion = 'controlar quien entra a tiempo al aula').save()
Empleo(ocupacion = 'cientifico', antiguedad = 8, cargo = 'encargado del laboratorio', breve_descripcion = 'mantener el orden y la disciplina del personal a cargo').save()
Empleo(ocupacion = 'presidente', antiguedad = 4, cargo = 'presidente electo', breve_descripcion = 'dirigir la republica').save()
print('Los empleos DE PRUEBA fueron cargados con exito')