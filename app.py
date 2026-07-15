import streamlit as st

st.set_page_config(page_title="ResellProfit - L'outil des Revendeurs", page_icon="💰", layout="centered")

# Design épuré
st.title("💰 ResellProfit")
st.subheader("Calculez vos bénéfices nets en un clic")
st.write("---")

# Formulaire du revendeur
prix_achat = st.number_input("Prix d'achat de l'objet (€)", min_value=0.0, value=10.0, step=1.0)
prix_vente = st.number_input("Prix de vente estimé (€)", min_value=0.0, value=30.0, step=1.0)

# Choix de la plateforme de revente
plateforme = st.selectbox(
    "Plateforme de vente :",
    ("Remise en main propre (Sans frais)", "eBay (Frais ~12%)", "Autre site (Frais fixes 10%)")
)

# Frais d'envoi cachés
frais_envoi = st.number_input("Frais de livraison à votre charge (€)", min_value=0.0, value=0.0, step=0.5)

st.write("---")

# Algorithme de calcul des frais
frais_plateforme = 0.0
if plateforme == "eBay (Frais ~12%)":
    frais_plateforme = prix_vente * 0.12
elif plateforme == "Autre site (Frais fixes 10%)":
    frais_plateforme = prix_vente * 0.10

total_frais = frais_plateforme + frais_envoi
benefice_net = prix_vente - prix_achat - total_frais

# Affichage du résultat business
if benefice_net > 0:
    st.success(f"### 🎉 Bénéfice Net : {benefice_net:.2f} €")
    roi = (benefice_net / prix_achat) * 100 if prix_achat > 0 else 0
    st.info(f"📈 **Retour sur investissement (ROI) :** {roi:.1f} %")
else:
    st.error(f"### ⚠️ Perte : {benefice_net:.2f} €")

st.caption(f"Détail des frais déduits : {total_frais:.2f} €")
st.write("---")
st.subheader("📱 Rejoignez la communauté !")

# Création de colonnes pour aligner les boutons des réseaux
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.link_button("✈️ Telegram", "https://t.me/Baptiste202420")
with col2:
        st.link_button("🐦 Twitter", "https://x.com/bbacri2")  # Mis à jour avec ton compte !
with col3:
    st.link_button("📸 Instagram", "https://www.instagram.com/baptistebacri?igsh=MTFvY2F2NnF0eW11dA==")
with col4:
        st.link_button("🎵 TikTok", "https://www.tiktok.com/@bbenallou0?_r=1&_t=ZN-983TROLjC34")
with col5:
    st.link_button("💬 Discord", "https://discord.gg/TON_INVITATION")
