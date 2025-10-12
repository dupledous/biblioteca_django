# biblioteca_django
Instrucciones Generales

•	Debe generar un sitio Web con las características que se indican en el enunciado.
•	El trabajo puede ser desarrollado por máximo 2 personas.
•	Debe ser desarrollado utilizando exclusivamente el framework Django.

Situación

Desarrollaremos un sitio web simulando la Metodología de Desarrollo Ágil, la que plantea la necesidad de presentar avances periódicos, lo cual implica que, en intervalos de tiempo (Sprint) se deben generar "Entregables".

El desarrollo consistirá en 3 Sprint, los cuales se describen a continuación:

•	Para el primer Sprint se requiere la presentación de una maqueta del sitio a desarrollar, implementado en Django bajo la utilización de vistas y templates HTML, apoyando el diseño con hojas de estilo y/o Frameworks de CSS.
Especificaciones para el primer Sprint

El sitio debe ser desarrollado completamente utilizando framework Django.

Características del sitio
1.	El sitio web a presentar debe contener, al menos, 3 páginas (templates).  La primera de ellas debe corresponder al index o home y debe entregar información relativa al contenido del sitio.
Desde esta se debe llegar las otras páginas del sitio, a través de la implementación de un menú o barra de navegación.

2.	Tanto el index, como la página secundaria, deben presentar contenido que incluya al menos lo siguiente (Con uso de recursos estáticos):

•	Imágenes.
•	Párrafos con textos.
•	Hipervínculos.

3.	Incluye un archivo CSS o utiliza un framework de CSS, que permita mostrar un diseño homogéneo en todas las páginas.  Uso de recursos estáticos.

4.	Incluye como tercera página un formulario de contacto, que como mínimo solicite, nombre completo, correo electrónico, teléfono, comentario. No es necesario que tenga funcionalidad por ahora.

5.	Recuerda implementar todas las vistas y configurar las urls respectivas.  Lo más importante es realizar el envío de la información a ser desplegada en el template, a través de diccionarios de contexto construidos en las vistas.




•	En el segundo Sprint, se debe incorporar como elemento adicional los modelos de Django y accesos a la Base de Datos
Especificaciones para el segundo Sprint

El sitio debe ser desarrollado completamente utilizando framework Django.

Características del sitio
1.	Trabajando con el sitio web anterior, debe ahora mejorar aspectos de los contenidos, obteniendo la información desde la base de datos generada en base a modelos en Django.

2.	El index, se mantiene como página de contenidos fijos, pero la página secundaria debe obtener información del modelo para presentar su información adicional.  Todo el sitio debe utilizar plantillas genéricas.

3.	Se debe registrar en el modelo la información obtenida desde el formulario de contacto existente.

4.	Adicionalmente generar una nueva página donde se entregue información de los clientes/usuarios/personajes registrados en el formulario de contacto, utilizando para el despliegue de la información, listas o tablas html.  Importante mantener el diseño del sitio generado, en la presentación de la información.






•	En el tercer Sprint y final, entregar una aplicativo integral, utilizando API Restful y seguridad.
Especificaciones para el tercer Sprint

El sitio debe ser desarrollado completamente utilizando framework Django.

Características del sitio
1.	Trabajando con el sitio web anterior, debe ahora mejorar aspectos de seguridad y obtención de información utilizando API’s en Django.

2.	Utilizando API de autenticación de Django, debe proveer de un servicio de autenticación (login) que restrinja el acceso a los usuarios no registrados a alguna o algunas de las opciones del menú principal. El registro del usuario se puede realizar en la misma aplicación o a través del módulo de administración.

3.	Adicionalmente generar una nueva página desde donde se consuma un servicio o API y despliegue la información recuperada.  Esta API puede ser generada con DRF o se puede utilizar alguna disponible en la Web.

