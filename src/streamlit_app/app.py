import streamlit as st


def main() -> None:
    st.set_page_config(page_title="Supersimple App", page_icon="✨", layout="centered")

    st.title("Supersimple Streamlit App")
    st.write(
        "This is a minimal, professional Streamlit app packaged as a Python project."
    )

    name = st.text_input("Your name", placeholder="Type your name...")
    if name:
        st.success(f"Hello, {name}!")


if __name__ == "__main__":
    main()
