# proyecto_final_python
Acá subo lo referido al proyecto final de python de CoderHouse

Entrada del dia 01/12/2022:
                        importante acordar de cambiar el directorio a 'myproject' cuando queremos correr el servidor, tuve que crear esa carpeta por motivos que no conozco porque sino no me dejaba instalar django

Entrada de preentrega, 13/12/2022:
                        Mi idea en esta web es que el usuario pueda cargar POR SEPARADO (todavía no se me ocurrió cómo enlazar las entradas) distintas instancias de Familiar, Mascota y Empleo.

                        Importante importar "seed_data.py" antes de usarla si se quiere tener entradas ya establecidas
                        
                        La web de por sí tiene botones para navegarla, no es necesario usar la barra de navegación en todos los casos.

                        PARA VER LAS LISTAS: mi-familia/
                                             mis-mascotas/
                                             mis-empleos/ 
                        
                        PARA DAR DE ALTA UNA ENTRADA NUEVA: mi-familia/alta
                                                            mis-mascotas/alta
                                                            mis-empleos/alta

                        PARA ACTUALIZAR UNA ENTRADA EXISTENTE: mi-familia/actualizar/<PK>
                                                               mis-mascotas/actualizar/<PK>
                                                               mis-empleos/actualizar/<PK>    (se debe ingresar una PK existente en la BD)

                        PARA BUSCAR ENTRADAS: mi-familia/buscar
                                              mis-mascotas/buscar
                                              mis-empleos/buscar 

                        PARA BORRAR UNA ENTRADA EXISTENTE: mi-familia/borrar/<PK>
                                                           mis-mascotas/borrar/<PK>
                                                           mis-empleos/borrar/<PK>    (se debe ingresar una PK existente en la BD)
                                                           ADVERTENCIA! comando experimental: funciona una sola vez si se usa el botón de "borrar", el problema está en que luego de usarlo la barra de navegación queda fijada con el "borrar" de la primera vez y eso interfiere en su correcto funcionamiento