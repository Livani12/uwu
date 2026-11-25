"""SlideStudio: punto de entrada para Streamlit Community Cloud."""
from pathlib import Path
import re
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent

def build_editor():
    """Incluye los recursos locales: el iframe no necesita CDN ni rutas externas."""
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    css = (ROOT / 'styles.css').read_text(encoding='utf-8')
    html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + css + '</style>')
    for name in ('vendor/pptxgen.bundle.js', 'app.js'):
        script = (ROOT / name).read_text(encoding='utf-8')
        script = re.sub(r'</script', lambda m: r'<\/script', script, flags=re.I)
        # Ejecutar en orden al final de body; defer no tiene efecto en scripts inline.
        html = html.replace(f'<script defer src="{name}"></script>', '')
        html = html.replace('</body>', '<script>' + script + '</script></body>', 1)
    return html


def main():
    st.set_page_config(page_title='SlideStudio', page_icon='🖼️', layout='wide', initial_sidebar_state='collapsed')
    st.markdown('<style>.block-container{max-width:100%;padding:1rem 0.65rem 0.5rem;}[data-testid="stHeader"]{height:0;background:transparent;}iframe{border:0;}</style>', unsafe_allow_html=True)
    components.html(build_editor(), height=1060, scrolling=True)


if __name__ == '__main__':
    main()
