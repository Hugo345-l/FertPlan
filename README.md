# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FertiPlan

## BMH

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bruno-castro-dias/">Bruno Castro - RM558359</a>
- <a href="https://www.linkedin.com/in/hugomariano191628150/">Hugo Mariano - rm560688</a>
- <a href="https://www.linkedin.com/in/matheus-castro-63644b224/">Matheus Castro - RM559293</a> 


## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomesr</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">Andre Godoi</a>


## 📜 Descrição

📜 Descrição

O FertiPlan é um sistema desenvolvido para auxiliar grandes agroindústrias e agricultores no planejamento e na gestão eficiente de fertilizantes. O projeto visa enfrentar um dos maiores desafios do agronegócio brasileiro: a dependência significativa de fertilizantes importados, que representa aproximadamente 85% do total utilizado no país. Essa dependência gera vulnerabilidade a flutuações de preços e problemas logísticos, impactando diretamente os custos de produção e a sustentabilidade da agricultura.

O FertiPlan propõe um sistema integrado que oferece recomendações personalizadas de fertilizantes, com foco na otimização do uso dos insumos, redução de custos e promoção de práticas agrícolas mais sustentáveis. A aplicação utiliza dados fornecidos pelo agricultor, como tipo de solo, cultura plantada e disponibilidade de insumos locais, para gerar recomendações inteligentes que ajudam a aumentar a eficiência e a resiliência das operações agrícolas.

- <a href="[https://www.linkedin.com/in/profandregodoi/](https://www.ers.usda.gov/amber-waves/2022/september/brazil-s-momentum-as-a-global-agricultural-supplier-faces-headwinds/)">Artigo de inspiração</a>

Como o Sistema Funciona

Entrada de Dados do Usuário:

O agricultor insere os dados necessários: tipo de solo (arenoso, argiloso, etc.), cultura plantada (milho, soja, etc.), área de cultivo (em hectares), região do país (para definir a logística e fornecedores), data de plantio, e expectativa de produtividade.

Consulta de Dados Estáticos:

Acessando o banco de dados, o sistema consulta a tabela de fertilizantes necessários para cada tipo de solo e cultura, e então calcula a quantidade exata de fertilizante necessário.

Essas tabelas contêm informações sobre as melhores práticas para cada tipo de solo e cultura, fornecendo dados objetivos que facilitam a recomendação.

Consulta de Preços e Disponibilidade:

O sistema então consulta uma base estática com informações sobre preços dos fertilizantes disponíveis no mercado internacional e local. Esta base incluirá informações sobre os fornecedores, se o fertilizante é importado ou local, preço por tonelada, qualidade do fertilizante, e a disponibilidade atual.

As informações são comparadas para recomendar a melhor opção de custo-benefício, levando em consideração a logística de distribuição e a qualidade dos insumos.

Geração de Recomendação:

A partir dos dados inseridos pelo agricultor e as consultas realizadas, o sistema gera uma recomendação que inclui:

O tipo de fertilizante (importado ou local).

A quantidade necessária para atingir a expectativa de produtividade.

Comparação dos custos entre diferentes fornecedores.

Sugestão do melhor fornecedor com base em custo, qualidade e disponibilidade.

Relatórios:

Um relatório detalhado em formato PDF é gerado, contendo:

A recomendação de fertilizantes e quantidade.

Comparação de fornecedores (preço, qualidade).

Informações sobre disponibilidade e previsão de entrega.

Esses relatórios podem ser consultados a qualquer momento e servem como base para o agricultor tomar decisões estratégicas durante o processo produtivo.

O FertiPlan permite que o agricultor insira feedback sobre os resultados obtidos após a aplicação das recomendações. Esse feedback é utilizado pelo sistema para ajustar os parâmetros de análise, tornando as recomendações futuras ainda mais precisas e personalizadas, criando um ciclo de aprendizado contínuo.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

--


## 🗃 Histórico de lançamentos

*1.0 - 13/10/2024

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
