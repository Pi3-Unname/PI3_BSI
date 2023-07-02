import streamlit as st
from build_hearder import build_header

build_header(
    title='Home',
    header='HOME',
)

st.write('''<p style='text-indent: 20px; text-align: justify;'>Neste trabalho de pesquisa, exploramos a fundo os dados de serviços de saúde para desvendar padrões e tendências relevantes. Analisamos os custos dos serviços, desenvolvemos modelos de previsão de demanda e investigamos o perfil dos pacientes com tempo de internação prolongado. Também abordamos questões de equidade na saúde. Nossas descobertas fornecem insights valiosos para aprimorar a gestão hospitalar, planejamento estratégico e tomada de decisão no setor da saúde.</p>

<p style='text-indent: 20px; text-align: justify;'>Nossos resultados têm o potencial de impactar positivamente o setor de saúde, fornecendo às organizações informações valiosas para melhorar a eficiência operacional, alocar recursos de forma mais eficaz e desenvolver estratégias de atendimento mais personalizadas. Além disso, essas descobertas podem contribuir para aprimorar políticas públicas de saúde, visando a equidade no acesso aos serviços.</p>

<p style='text-indent: 20px; text-align: justify;'>Em resumo, nossa pesquisa busca desvendar os segredos escondidos nos dados de serviços de saúde, revelando informações cruciais para aprimorar a gestão, previsão e compreensão das demandas desses serviços. Ao utilizar abordagens inovadoras e considerar variáveis-chave, estamos contribuindo para um sistema de saúde mais eficiente, equitativo e voltado para as necessidades da população.</p>''', unsafe_allow_html=True)