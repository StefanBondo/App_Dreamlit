import streamlit as st


def quiz_streamlit():
    st.title("Mini quiz")

    # Spørgsmål 1
    st.subheader("1) Tal-spørgsmål")

    if "forsøg_spg1" not in st.session_state:
        st.session_state.forsøg_spg1 = 0

    korrekt_svar = 5
    er_låst = st.session_state.forsøg_spg1 >= 3

    user_tal = st.number_input(
        "Skriv det rigtige tal Hint(1-5):",
        step=1,
        format="%d",
        disabled=er_låst
    )
    if st.button("Tjek tal", disabled=er_låst):
        if user_tal == korrekt_svar:
            st.success("Du har gættet korrekt")
        else:
            st.session_state.forsøg_spg1 = st.session_state.forsøg_spg1 + 1
            st.error(f"Du har gættet forkert. Forsøg: {st.session_state.forsøg_spg1}/3")

    if st.session_state.forsøg_spg1 >= 3:
        st.error("Du har ikke flere forsøg")

    st.divider()

    # Spørgsmål 2
    st.subheader("2) Land/by-spørgsmål")
    korrekt_land = "københavn"
    user_by = st.text_input("Hvad hedder hovedstaden i Danmark:")
    if st.button("Tjek by"):
        if user_by.strip().lower() == korrekt_land:
            st.success("Du har ret")
        else:
            st.error("Du er forkert")

    st.divider()

    # Spørgsmål 3
    st.subheader("3) Regnestykke")
    regnestyk_korrekt = 5.6
    user_regne = st.number_input("Hvad er 4.4 + 1.2:", step=0.1, format="%.1f")
    if st.button("Tjek regnestykke"):
        if user_regne == regnestyk_korrekt:
            st.success("Du har regnet korrekt")
        else:
            st.error("Du har regnet forkert")
            
    st.divider()
    
    # Spørgsmål 4 - loop
    
    # Spørgsmål 4 - loop
    st.subheader("4) Skriv 1, 2, 3")

    korrekt_liste = [1, 2, 3]

    tal_1 = st.number_input("Første tal", min_value=0, step=1, format="%d", key="tal1")
    tal_2 = st.number_input("Andet tal", min_value=0, step=1, format="%d", key="tal2")
    tal_3 = st.number_input("Tredje tal", min_value=0, step=1, format="%d", key="tal3")

    user_liste = [tal_1, tal_2, tal_3]

    if st.button("Tjek rækkefølge"):
        alle_rigtige = True

        for index in range(3):
            if user_liste[index] != korrekt_liste[index]:
                alle_rigtige = False

        if alle_rigtige:
            st.success("Korrekt! Du skrev 1, 2, 3.")
        else:
            st.error(f"Ikke helt rigtigt. Du skrev {user_liste}")
            
    st.divider()
    
    # Spørgsmål 5
    
    st.subheader("5) Byer i DK")
    
    væreste_by = "Køge"
    
    muligheder = ["Køge", "Allerød", "Frederiksund"]
    
    svar = st.radio("Hvad er den værste by i DK", muligheder)
    
    if st.button ("Tjek svar"):
        if svar == væreste_by:
            st.success("Du har gættet korrekt")
        else:
            st.error(f"Du har gættet forkert, det korrekte er {væreste_by}")

quiz_streamlit()
