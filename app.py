
import streamlit as st

# --- App Title ---
st.title("🛒 Mini E-commerce Store")

# --- Sample Products ---
products = [
    {"name": "Wireless Earbuds", "price": 15000, "image": "https://via.placeholder.com/150"},
    {"name": "Smart Watch", "price": 25000, "image": "https://via.placeholder.com/150"},
    {"name": "Phone Case", "price": 5000, "image": "https://via.placeholder.com/150"},
]

# --- Shopping Cart Simulation ---
cart = []

st.header("📦 Products Available")
for product in products:
    st.image(product["image"], width=150)
    st.write(f"**{product['name']}**")
    st.write(f"Price: ₦{product['price']}")
    if st.button(f"Add to Cart - {product['name']}"):
        cart.append(product)
        st.success(f"{product['name']} added to cart!")

# --- Checkout Form ---
st.header("📝 Checkout")
with st.form("checkout_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    address = st.text_area("Delivery Address")
    submit = st.form_submit_button("Place Order")

    if submit:
        if name and email and address:
            st.success("Order placed successfully!")
            st.write("🔔 You will be contacted soon.")
        else:
            st.error("Please fill in all fields.")

st.caption("Powered by Streamlit")
