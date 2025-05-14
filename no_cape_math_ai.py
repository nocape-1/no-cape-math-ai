
import streamlit as st
import sympy as sp

# App Title and Description
st.set_page_config(page_title="No Cape Math AI", page_icon="🧠")
st.title("🧠 No Cape Math AI")
st.markdown("**AI isubiza ibibazo by'imibare y’ishuri: Algebra, Calculus, na Geometry.**")
st.markdown("---")

# Main Functionality
choice = st.selectbox("👉 Hitamo icyiciro cy'imibare ushaka:", ["Algebra", "Calculus", "Geometry"])

# Algebra Solver
if choice == "Algebra":
    st.subheader("📘 Algebra")
    eq_input = st.text_input("Injiza equation (urugero: 2*x + 3 = 11):")
    if eq_input:
        try:
            x = sp.Symbol('x')
            left, right = eq_input.split('=')
            eq = sp.Eq(sp.sympify(left), sp.sympify(right))
            sol = sp.solve(eq, x)
            st.success(f"Ibisubizo bya {eq_input}: {sol}")
        except Exception as e:
            st.error(f"Ibibazo mu gusoma equation: {e}")

# Calculus Solver
elif choice == "Calculus":
    st.subheader("📗 Calculus")
    expr_input = st.text_input("Injiza expression (urugero: x**2 + 3*x + 1):")
    if expr_input:
        try:
            x = sp.Symbol('x')
            expr = sp.sympify(expr_input)
            derivative = sp.diff(expr, x)
            integral = sp.integrate(expr, x)
            st.success(f"🔹 Derivative: {derivative}")
            st.info(f"🔸 Integral: {integral} + C")
        except Exception as e:
            st.error(f"Hari ikibazo: {e}")

# Geometry Calculator
elif choice == "Geometry":
    st.subheader("📕 Geometry")
    shape = st.selectbox("Hitamo shape:", ["Circle", "Rectangle", "Triangle"])
    
    if shape == "Circle":
        radius = st.number_input("Injiza radius ya circle:", min_value=0.0)
        if radius > 0:
            area = sp.pi * radius**2
            circumference = 2 * sp.pi * radius
            st.success(f"📏 Area: {area.evalf()}")
            st.info(f"🌀 Circumference: {circumference.evalf()}")

    elif shape == "Rectangle":
        length = st.number_input("Injiza uburebure (length):", min_value=0.0)
        width = st.number_input("Injiza ubugari (width):", min_value=0.0)
        if length > 0 and width > 0:
            area = length * width
            perimeter = 2 * (length + width)
            st.success(f"📐 Area: {area}")
            st.info(f"📏 Perimeter: {perimeter}")

    elif shape == "Triangle":
        base = st.number_input("Injiza base ya triangle:", min_value=0.0)
        height = st.number_input("Injiza height ya triangle:", min_value=0.0)
        if base > 0 and height > 0:
            area = 0.5 * base * height
            st.success(f"📐 Area: {area}")
