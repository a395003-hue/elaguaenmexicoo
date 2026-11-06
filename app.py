import pandas as pd
import streamlit as st
import altair as alt
        "respuesta": "El porcentaje de hogares conectados a la red pública",
        "explicacion": "La cobertura describe el acceso a la red de agua entubada."
    },
    {
        "pregunta": "Si una regadera tiene un caudal de 8 litros por minuto y permanece abierta 3 minutos, ¿cuánta agua utiliza?",
        "opciones": ["8 litros", "11 litros", "24 litros"],
        "respuesta": "24 litros",
        "explicacion": "Se multiplica el caudal por el tiempo: 8 × 3 = 24 litros."
    },
    {
        "pregunta": "¿Qué puedes hacer con el agua fría que sale mientras esperas la caliente?",
        "opciones": [
            "Dejarla correr por el drenaje",
            "Recolectarla y reutilizarla en otras tareas",
            "Añadirle jabón y desecharla"
        ],
        "respuesta": "Recolectarla y reutilizarla en otras tareas",
        "explicacion": "Puede aprovecharse para actividades como limpiar patios o descargar el sanitario, según su calidad y uso."
    },
    {
        "pregunta": "¿Cuál de estas acciones ayuda a reducir el desperdicio?",
        "opciones": [
            "Reparar las fugas",
            "Dejar la llave abierta al cepillarse",
            "Aumentar el tiempo de ducha"
        ],
        "respuesta": "Reparar las fugas",
        "explicacion": "Reparar fugas evita que el agua se pierda continuamente."
    }
]

respuestas_usuario = []
for i, pregunta in enumerate(preguntas):
    seleccion = st.radio(
        f"**{i + 1}. {pregunta['pregunta']}**",
        pregunta["opciones"],
        key=f"quiz_agua_{i}"
    )
    respuestas_usuario.append(seleccion)

if st.button("Revisar mis respuestas", type="primary"):
    aciertos = 0
    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[i] == pregunta["respuesta"]:
            aciertos += 1

    st.session_state["resultado_quiz_agua"] = aciertos

    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[i] == pregunta["respuesta"]:
            st.success(f"Pregunta {i + 1}: ¡Correcto! {pregunta['explicacion']}")
        else:
            st.error(
                f"Pregunta {i + 1}: La respuesta correcta es "
                f"**{pregunta['respuesta']}**. {pregunta['explicacion']}"
            )

if "resultado_quiz_agua" in st.session_state:
    puntos = st.session_state["resultado_quiz_agua"]
    st.metric("Tu puntuación", f"{puntos} de {len(preguntas)}")
    if puntos == len(preguntas):
        st.balloons()
        st.success("¡Excelente! Tienes muy claros los conceptos.")
    elif puntos >= 3:
        st.info("¡Buen trabajo! Repasa las explicaciones para mejorar.")
    else:
        st.info("Sigue aprendiendo: revisa los indicadores y las recomendaciones de la aplicación.")

# ==========================================================
# 7. COMPROMISO PERSONAL
# ==========================================================
st.markdown("---")
st.subheader("7. ✍️ Mi compromiso con el agua")
st.write("Marca las acciones que te comprometes a intentar durante esta semana.")

compromisos = [
    "Cerrar la llave mientras me cepillo los dientes.",
    "Reducir el tiempo que paso en la ducha.",
    "Reutilizar agua cuando sea posible y seguro.",
    "Avisar si encuentro una fuga.",
    "Usar la lavadora con cargas completas."
]

acciones_realizadas = []
for i, compromiso in enumerate(compromisos):
    if st.checkbox(compromiso, key=f"compromiso_agua_{i}"):
        acciones_realizadas.append(compromiso)

st.write(f"**Avance de tu compromiso: {len(acciones_realizadas)} de {len(compromisos)} acciones**")
st.progress(len(acciones_realizadas) / len(compromisos))

if len(acciones_realizadas) == len(compromisos):
    st.success("¡Excelente compromiso! Cada hábito responsable ayuda a cuidar el agua.")
elif acciones_realizadas:
    st.info("¡Vas avanzando! Mantén estas acciones durante la semana.")
else:
    st.caption("Selecciona al menos una acción para comenzar tu compromiso.")


# Las fuentes originales pasan a ser la sección 8.
st.subheader("8. Fuentes de información oficiales")
st.write("Para garantizar la veracidad del proyecto, los datos e indicadores provienen de instituciones oficiales:")

fuentes_texto = "- **CONAGUA (Comisión Nacional del Agua)**\n  - *Documento:* Estadísticas del Agua en México / Atlas del Agua.\n  - *Institución:* Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT).\n  - *Enlace:* [https://www.gob.mx/conagua](https://www.gob.mx/conagua)\n\n- **Sistema de Información del Agua (CONAGUA)**\n  - *Documento:* Monitoreo de disponibilidad y calidad del agua por regiones hidrológicas.\n  - *Enlace:* [https://app.conagua.gob.mx/sistemasdeagua/](https://app.conagua.gob.mx/sistemasdeagua/)\n\n- **INEGI (Instituto Nacional de Estadística y Geografía)**\n  - *Documento:* Censos de población y estadísticas sobre servicios de agua potable y saneamiento.\n  - *Enlace:* [https://www.inegi.org.mx/](https://www.inegi.org.mx/)\n\n- **FAO (Organización de las Naciones Unidas para la Alimentación y la Agricultura)**\n  - *Documento:* Base de datos global de recursos hídricos (AQUASTAT).\n  - *Enlace:* [https://www.fao.org/](https://www.fao.org/)"

st.markdown(fuentes_texto)
