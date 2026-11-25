# SlideStudio — edición Streamlit

Editor visual de presentaciones en español. Analiza localmente los colores y la composición de una imagen de referencia, crea una estructura de diapositivas para un tema y exporta PowerPoint editable. No requiere API ni claves. El editor original HTML/JavaScript se integra en Streamlit; los recursos están incluidos.

## Publicación en Streamlit Community Cloud

1. Descomprime el ZIP. Sube **los archivos y la carpeta vendor**, no el ZIP, a la raíz de tu repositorio en GitHub. Verifica que `streamlit_app.py` y `requirements.txt` estén directamente en la rama `main`, no dentro de otra carpeta.
2. En https://share.streamlit.io/ crea una app. Repository: `Livani12/el-mejor` (o tu repositorio). Branch: `main`. Main file path: `streamlit_app.py`. App URL: el nombre disponible que prefieras.
3. Pulsa Deploy. Streamlit instalará la dependencia de `requirements.txt`. En Advanced settings puedes elegir Python 3.12 si está disponible.

## Uso local

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

También puedes abrir `index.html` directamente en un navegador, manteniendo los otros archivos en sus rutas originales.

## Funciones

- Imagen de referencia y detección aproximada de paleta/composición.
- Tema, número de diapositivas, cinco estilos y seis distribuciones.
- Fuente, tamaños, colores, edición de contenido e imágenes.
- Agregar, duplicar, ordenar, eliminar, previsualizar y presentar.
- Guardar y reabrir proyecto JSON; exportar PPTX con objetos independientes.

La identificación de la tipografía exacta y la reconstrucción píxel por píxel no son automáticas. La generación de contenido inicial crea una estructura y textos guía, no investigación mediante IA. Los proyectos se procesan en el navegador: descarga un JSON antes de recargar o cerrar la página para no perder el trabajo. Las fuentes deben estar instaladas en el equipo donde se abre PowerPoint para mantener la apariencia.

## Archivos necesarios

- `streamlit_app.py`: entrada de Streamlit.
- `requirements.txt`: dependencia de Python.
- `index.html`, `app.js`, `styles.css`: editor.
- `vendor/pptxgen.bundle.js`: biblioteca local de exportación; licencia adjunta.
- `.streamlit/config.toml`: configuración opcional.
