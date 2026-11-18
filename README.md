# API Simulador SMS Chile

API REST desarrollada con FastAPI para generar números telefónicos con formato móvil chileno (`+56 9 XXXX XXXX`) y simular la recepción de mensajes de texto (SMS) en entornos de prueba.

## Endpoints principales

* `POST /numeros/generar` - Crea un nuevo número chileno virtual en memoria.
* `POST /numeros/{numero}/simular-sms` - Envía un SMS simulado al número indicado.
* `GET /numeros/{numero}/mensajes` - Consulta la bandeja de entrada del número.

## Documentación interactiva

Una vez desplegada, agrega `/docs` al final de tu URL para acceder a la interfaz de pruebas Swagger.
