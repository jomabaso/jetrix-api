import subprocess

# Ejecuta el comando para iniciar el servidor Django
subprocess.run(["python", "manage.py", "runserver", "0.0.0.0:8000"])