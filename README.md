# API

## Endpoints

- `/register`:
	- **POST**: registra un **usuario** con **password**. 
	- **Ejemplo**: `http POST /register username="user1" password="passwd1"`
- `/login`:
	- **POST**: Devuelve el JWT de un usuario si introduce las credenciales correctas.
	- **Ejemplo**: `http POST /login username="user1" password="passwd1"`
	- **Devuelve**: JWT del usuario.
