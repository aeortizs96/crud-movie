# Backend

Este es el componente backend del proyecto **CRUD-Movie**, que incluye la lógica de negocio y la gestión de datos. A continuación, encontrarás los pasos necesarios para configurar, instalar y ejecutar este componente.

## Configuración del entorno

Sigue estos pasos para configurar el entorno y preparar el proyecto:

1. **Base de Datos:** 
   - Crear una base de datos llamada **"products"** en el sistema gestor de bases de datos MySql.
2. **Script SQL:** 
   - Importar el script **db/movies.sql** dentro de la base de datos **"products"**.
   - Ejecutar el script para cargar y configurar la estructura y los datos.

3. **Instalar `virtualenv`**:
   Ejecuta el siguiente comando para instalar la herramienta que te permitirá crear entornos virtuales:

4. **Instalar las dependencias**:
Una vez activado el entorno virtual, instala las dependencias necesarias para el proyecto. Estas están listadas en el archivo `requirements.txt`. Usa el siguiente comando:

```
pip install -r requirements.txt
```