# 1. Definimos los datos reales (Simulamos vacantes encontradas en Bucaramanga)
empresa_1 = "Fábrica de Software Bucaramanga"
cargo_1 = "Aprendiz de Desarrollo Python"
link_1 = "https://elempleo.com"

empresa_2 = "Tech Solutions Girón"
cargo_2 = "Desarrollador Junior HTML/CSS"
link_2 = "https://computrabajo.com"

# 2. Le decimos a Python que cree (o abra) un archivo llamado 'index.html'
# La 'w' significa "Write" (Escribir). Si el archivo no existe, Python lo crea.
archivo_html = open("index.html", "w", encoding="utf-8")

# 3. Guardamos la estructura del HTML dentro de una variable de Python
# Usamos comillas triples (''' ) para poder escribir en múltiples líneas
codigo_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Santander Tech Jobs</title>
</head>
<body>
    <h1>📍 Vacantes Disponibles en Santander</h1>
    <p>Este portafolio web fue generado automáticamente mediante un script de Python.</p>

    <!-- Caja de Oferta 1 -->
    <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;">
        <h2>{cargo_1}</h2>
        <p><strong>Empresa:</strong> {empresa_1}</p>
        <a href="{link_1}" target="_blank">Ver oferta de empleo</a>
    </div>

    <!-- Caja de Oferta 2 -->
    <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;">
        <h2>{cargo_2}</h2>
        <p><strong>Empresa:</strong> {empresa_2}</p>
        <a href="{link_2}" target="_blank">Ver oferta de empleo</a>
    </div>

    <hr>
    
    <!-- Tu Formulario de Contacto para los Reclutadores locales -->
    <h3>¿Eres una empresa local? Contáctame</h3>
    <form>
        <label for="nombre">Nombre de la Empresa:</label>
        <input type="text" id="nombre" placeholder="Ej. Tech Santander" required>
        <br><br>
        <button type="submit">Enviar Mensaje</button>
    </form>
</body>
</html>
'''

# 4. Le ordenamos a Python que escriba todo el bloque de texto dentro del archivo
archivo_html.write(codigo_html)

# 5. Cerramos el archivo para liberar la memoria de la computadora
archivo_html.close()

print("¡Éxito! Python ha creado tu archivo 'index.html' de forma automática.")
