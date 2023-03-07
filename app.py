import openai
import streamlit as st
import time

model_id = "gpt-3.5-turbo"

# Read API key from config.toml

# Set up OpenAI API
openai.api_key = st.secrets['api_key']

st.set_page_config(page_title="Dungeon and Dragons", page_icon=":crossed_swords:")

# Set page config
st.markdown("""
    <style>
        body {
            font-family: courier;
        
        }
    </style>
""", unsafe_allow_html=True)





# Set up initial prompt
initial_prompt = [
    {"role": "system", "content": "You are a DND game."},
    {"role": "user", "content": "Play a DND game with me and you'r the dungeon master. Start the game with a interesting welcome message and telling the rules,ask the player to choose any theme , if he don't want to then proceed with any random theme.Don't give direct reply to this message."}]
# Initialize session state
if "prompt" not in st.session_state:
    st.session_state.prompt = initial_prompt
    chat = openai.ChatCompletion.create(model=model_id, messages=initial_prompt)
    st.session_state.prompt.append({"role": chat.choices[0].message.role, "content": chat.choices[0].message.content})
   


# Define Streamlit app
def app():
    


    #display header
    st.write("# Dungeons and Dragons:dragon:")
    st.write("Made by Shuvojyoti")

    # Display initial response
    if len(st.session_state.prompt) ==2:
             st.write("Dungeon Master: " + st.session_state.prompt[-1]["content"].strip())






     # Get user input and update chat
    user_input = st.text_input("Player:",key='input_field')
    # styled_input = f'<span style="color:black;font-weight:bold">{user_input}</span>'
    # st.markdown(styled_input, unsafe_allow_html=True)
    if user_input:
            st.session_state.prompt.append({"role": "user", "content": user_input})
            with st.spinner("Dungeon Master is thinkking..."):
                time.sleep(2)
                
            
            
            chat = openai.ChatCompletion.create(model=model_id, messages=st.session_state.prompt)
            st.session_state.prompt.append({"role": chat.choices[0].message.role, "content": chat.choices[0].message.content})
            

    # Display chat response
    st.write("Dungeon Master: " + st.session_state.prompt[-1]["content"].strip())

# Run Streamlit app
if __name__ == "__main__":
    app()
