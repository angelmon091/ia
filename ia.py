#borrador para el asistente chatbot para la competencia del hackathon
"""

CHAT BOT PARA RECOMENDACIONES PERSONALISADAS SOBRE ALGORITMOS QUE SUGIEREN DESTINOS Y ACTIVIDADES VACACIONALES SEGUN LAS PREFERENCIAS DEL USUARIO

"""
import requests

import streamlit as st

st.title("ASISTENTE TURISTICO DEL ALEXANDER :)")

if "messages" not in st.session_state:
     st.session_state.messages = []
if "first_message" not in st.session_state:
     st.session_state.first_message = True

if st.session_state.first_message:
     with st.chat_message("asssistain"):
          st.markdown("Hola! Soy el asistente turístico de Alexander. ¿Necesitas alguna información sobre destinos y actividades vacacionales?")
          st.markdown("Puedes empezar con preguntas sobre tus intereses o necesidades.")
     
     st.session_state.messages.append({"role": "assistain", "content": "hola, de que maneraq te puedo ayudar?"})        
     st.session_state.first_message = False
     
if pronpt := st.chat_input("como te puedo ayudar?"):
     with st.chat_message("user"):
          st.markdown(pronpt)
     st.session_state.messages.append({"role": "user", "content": pronpt})
     
     with st.chat.message("asssistain"):
          st.markdown(pronpt)
          
     st.session_state.messages.append({"role": "assistain", "content": pronpt})
     

          