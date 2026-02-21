import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Snowball 4K", page_icon="❄️", layout="centered")

# --- Lógica de Dados ---
META_EURO = 4000.0
COTACAO_EURO = 6.00
YIELD_MEDIO = 0.009

ativos_carteira = [
    {"t": "HGLG11", "p": 168.0, "cat": "Logística"},
    {"t": "BTLG11", "p": 106.0, "cat": "Logística"},
    {"t": "XPML11", "p": 118.0, "cat": "Shoppings"},
    {"t": "KNCR11", "p": 105.0, "cat": "Papel"},
    {"t": "CPTS11", "p": 8.6, "cat": "Papel"},
    {"t": "TAEE11", "p": 35.0, "cat": "Ações"},
    {"t": "BBAS3", "p": 29.0, "cat": "Ações"},
    {"t": "TRXF11", "p": 112.0, "cat": "Renda Urbana"}
]

pesos = {
    "Papel": 0.30,
    "Logística": 0.20,
    "Shoppings": 0.15,
    "Ações": 0.15,
    "Renda Urbana": 0.20
}

# --- Interface ---
st.title("❄️ Snowball 4K")
st.markdown("### O seu caminho para os **€ 4.000,00/mês**")

with st.sidebar:
    st.header("Gestão de Carteira")
    patrimonio = st.number_input("Património Atual (R$)", value=2000.0, step=500.0)
    aporte = st.number_input("Aporte de Hoje (R$)", value=2000.0, step=100.0)

# Cálculos de Renda
renda_real = patrimonio * YIELD_MEDIO
renda_euro = renda_real / COTACAO_EURO
progresso = (renda_euro / META_EURO) * 100

col1, col2 = st.columns(2)
col1.metric("Renda Mensal (R$)", f"R$ {renda_real:.2f}")
col2.metric("Renda Mensal (€)", f"€ {renda_euro:.2f}")

st.write(f"**Progresso da Meta:** {progresso:.2f}%")
st.progress(min(progresso/100, 1.0))

st.divider()
st.subheader("🛒 Sugestão de Compra Rebalanceada")

for cat, peso in pesos.items():
    valor_setor = aporte * peso
    # Seleciona o primeiro ativo da categoria para simplificar o aporte
    lista_cat = [a for a in ativos_carteira if a['cat'] == cat]
    if lista_cat:
        ativo = lista_cat[0]
        qtd = int(valor_setor // ativo['p'])
        if qtd > 0:
            st.success(f"**{cat}**: Comprar {qtd}x **{ativo['t']}** (Subtotal: R$ {qtd*ativo['p']:.2f})")

if st.button("🚀 REGISTRAR APORTE"):
    st.balloons()
    st.write("Aporte guardado! A sua bola de neve está a crescer.")
