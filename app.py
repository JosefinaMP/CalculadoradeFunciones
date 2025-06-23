import streamlit as st
import matplotlib.pyplot as plt

st.title("🧮 Calculadora de funciones")
st.write("""
Ingresá una función en términos de `x`, como por ejemplo:
- `x**2`
- `2*x + 1`
- `x**3 - x`
""")

funcion = st.text_input("Función f(x):", value="x**2")
x_vals = list(range(-4, 5))

def evaluar_funcion(expr, x):
    return eval(expr, {"__builtins__": {}}, {"x": x})

if st.button("Analizar función"):
    try:
        y_vals = [evaluar_funcion(funcion, x) for x in x_vals]
        codominio = list(set(y_vals))

        st.subheader("Pares (x, f(x)):")
        for x, y in zip(x_vals, y_vals):
            st.write(f"f({x}) = {y}")

        inyectiva = len(set(y_vals)) == len(x_vals)
        sobreyectiva = set(codominio).issubset(set(y_vals))
        biyectiva = inyectiva and sobreyectiva

        st.subheader("Resultado:")
        st.write("✔ Es inyectiva" if inyectiva else "✘ No es inyectiva")
        st.write("✔ Es sobreyectiva (en el dominio evaluado)" if sobreyectiva else "✘ No es sobreyectiva")
        st.write("✅ Es biyectiva" if biyectiva else "❌ No es biyectiva")

        st.subheader("Gráfico de la función")
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
        ax.axhline(0, color='gray', linewidth=0.5)
        ax.axvline(0, color='gray', linewidth=0.5)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title(f"f(x) = {funcion}")
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error al evaluar la función:\n{e}")
