import streamlit as st
import random

def main():
    st.title("Hand Cricket Game")
    
    # Initialize session state variables
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'your_runs' not in st.session_state:
        st.session_state.your_runs = 0
    if 'comp_runs' not in st.session_state:
        st.session_state.comp_runs = 0
    if 'is_out' not in st.session_state:
        st.session_state.is_out = False
    if 'batting' not in st.session_state:
        st.session_state.batting = True  # True if the player is batting, False if bowling
    if 'result' not in st.session_state:
        st.session_state.result = ""

    lst = [1, 2, 3, 4, 6]

    if st.session_state.batting:
        st.subheader("Your Batting")
        runs = st.number_input("Enter Runs for Your Batting Turn (1, 2, 3, 4, 6):", min_value=1, max_value=6, step=1, key='bat')
        
        if st.button("Play Batting Move"):
            comp_bowl = random.choice(lst)
            st.write(f"Your Guess: {runs}, Computer Guess: {comp_bowl}")

            if runs == comp_bowl:
                st.session_state.is_out = True
                st.write(f"You are Out. Your Total Runs = {st.session_state.your_runs}\n")
                st.session_state.batting = False  # Switch to bowling
            else:
                if runs == 5:
                    st.write("Sorry !! 5 not possible")
                else:
                    st.session_state.your_runs += runs
                    st.write(f"Your runs now are: {st.session_state.your_runs}\n")

    if not st.session_state.batting and not st.session_state.result:
        st.subheader("Computer Batting")
        bowl = st.number_input("Enter Runs for Your Bowling Turn (1, 2, 3, 4, 6):", min_value=1, max_value=6, step=1, key='bowl')
        
        if st.button("Play Bowling Move"):
            comp_bat = random.choice(lst)
            st.write(f"Computer Guess: {comp_bat}, Your Guess: {bowl}")

            if comp_bat == bowl:
                st.write(f"The Computer is Out. Computer Runs = {st.session_state.comp_runs}\n")
                st.session_state.result = determine_result(st.session_state.your_runs, st.session_state.comp_runs)
            else:
                st.session_state.comp_runs += comp_bat
                st.write(f"Computer Runs: {st.session_state.comp_runs}\n")

                if st.session_state.comp_runs > st.session_state.your_runs:
                    st.session_state.result = determine_result(st.session_state.your_runs, st.session_state.comp_runs)

    if st.session_state.result:
        st.subheader("RESULTS:")
        st.write(st.session_state.result)
        if st.button('Play Again'):
            reset_game_state()

def determine_result(your_runs, comp_runs):
    if comp_runs < your_runs:
        diff_runs = your_runs - comp_runs
        return f"\nYou won the Game.\n\nYour Total Runs = {your_runs}\nComputer Total Runs = {comp_runs}\n\nCongratulations!!! You Won the game by {diff_runs} runs"
    elif comp_runs == your_runs:
        return "The Game is a Tie"
    else:
        return f"\nComputer won the Game.\n\nComputer Total Runs = {comp_runs}\nYour Total Runs = {your_runs}\n\nWell tried your best, comeback Strong for next match"

def reset_game_state():
    st.session_state.step = 1
    st.session_state.your_runs = 0
    st.session_state.comp_runs = 0
    st.session_state.is_out = False
    st.session_state.batting = True
    st.session_state.result = ""

if __name__ == "__main__":
    main()
