import streamlit as st

st.set_page_config(layout = "wide")
st.markdown("""<style>[data-testid="stSidebar"] {background: linear-gradient(180deg, #00c6ff, #0072ff);padding: 20px;}.icon-container {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<font face= Helvetica><b><u>Desenvolvedor</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Wesley E. dos Santos  
                - Fiap Postech - 3DTAT''')
    linkedin_url = "https://www.linkedin.com/in/wesleyesantos/"
    youtube_url = "https://www.youtube.com/@Wesley_santos-Excel_PowerBI"
    st.sidebar.markdown(f"""<div class="icon-container"><a href="{linkedin_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/linkedin.png?raw=true" width="30"/></a><a href="{youtube_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/youtube.png?raw=true" width="30"/></a></div>""", unsafe_allow_html=True)
    st.sidebar.image('https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/eu.jpg?raw=true', use_column_width=True)
    
st.subheader(':blue[Conclusão]',divider='blue')
st.markdown('''Com o trabalho realizado cheguei as seguintes conclusões abaixo:''')
st.markdown('''- <b><font color='blue'>Pedras:</b></font> Ao analisar as pedras já vemos de cara que maior volume dos alunos estão na penultima pedra que é a <b>Ametista</b>, ou seja uma ótima classificação estão a um passo da <b>Topázio</b> que é a maior pedra, porém quando abrimos a análise a nível fase conseguimos ver que a última fase carrega um volume maior de alunos na pedra mais baixa e o percentil de alunos nos níveis intermediários (<b>Ágata </b>e <b>Ametista</b>) estão com percentual abaixo da média, o que podemos considerar um ponto de atenção mesmo contendo um volume de alunos menor, a atuação preventiva no Gap irá tratar o problema evitando que o mesmo ocorrá quando tiver uma quantidade grande de alunos na fase em questão.''', unsafe_allow_html=True)
st.markdown('''- <b><font color='blue'>Ponto de Virada (PV):</b></font> Quanto ao ponto de virada por ser um passo mágico e estar mais atrelado a conquista de skills fundamentais, o maior volume de conquistas ocorre nas primeiras fases, ocorre menos nas últimas fases pois os alunos já estão mais experientes com muito mais habilidades para resolução de desafios complexos (o que não os exclui de adquirirem novas habilidades), porém na fase 8 não teve alunos que chegaram a conquista em questão o que levanta um ponto de análise para ir mais afundos nos eventos que impactaram tal resultado; ao olhar por ano pude observar que 2020 se sobresai mais nas fases intermediárias, fases 3 e 4 se aparecem com um pico, é interessante puxar os eventos que ocorreram em 2020 nas outras fases primarias que impactaram tanto os alunos de atingir o PV, os outros anos teve uma estabilidade boa acompanhando o raciocínio de maior conquista nas primeiras fases e caindo esse volume de acordo com que a fase aumenta.''', unsafe_allow_html=True)
st.markdown('''- <b><font color='blue'>Ponto de Virada (PV):</b></font>

