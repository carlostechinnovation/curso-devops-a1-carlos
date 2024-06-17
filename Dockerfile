# Usa la imagen base de Python 3.10
FROM python:3.10

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia el script Python desde GitHub al contenedor
ADD https://raw.githubusercontent.com/carlostechinnovation/curso-devops-a1-carlos/main/main.py /app/main.py

# Ejecuta el script al iniciar el contenedor
CMD ["python", "main.py"]
