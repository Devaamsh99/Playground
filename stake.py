import streamlit as st

def calculate_investment(odds):
    if odds > 0:
        return 2000 / odds
    return 0

st.title("Betting Investment Calculator")

st.header("Enter the odds for each team")
odds_a = st.number_input("Odds for Team A", min_value=0.01, format="%.2f")
odds_b = st.number_input("Odds for Team B", min_value=0.01, format="%.2f")

st.header("Which team will lose?")
losing_team = st.radio("Select the losing team", ("Team A", "Team B"))

hit_six = st.radio("Did the losing team hit a 6 in 2 overs?", ("Yes", "No"))

if st.button("Calculate Investment"):
    investment_a = calculate_investment(odds_a)
    investment_b = calculate_investment(odds_b)
    total_investment = investment_a + investment_b
    max_profit = 4000 - total_investment
    loss_amount = total_investment - 2000
    
    st.subheader("Investment Amounts:")
    st.write(f"Investment for Team A: ${investment_a:.2f}")
    st.write(f"Investment for Team B: ${investment_b:.2f}")
    st.write(f"Total Investment: ${total_investment:.2f}")
    
    st.subheader("Results:")
    if hit_six == "Yes":
        st.write(f"Maximum Profit: ${max_profit:.2f}")
    else:
        st.write(f"Loss Amount: ${loss_amount:.2f}")