import streamlit as st

def main():
    st.title("Aplicación de tarjetas de texto")

    # Campo para que el usuario escriba el texto
    user_input = st.text_area("Escribe tu texto aquí:")

    if st.button("Crear Tarjeta"):
        # Mostrar el texto en forma de tarjeta
        st.markdown(f"""
            <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; border: 1px solid #e1e4e8;">
                <h4>Tu Texto:</h4>
                <p>{user_input}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
