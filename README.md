# Draw & Drive AI 🏎️🧠

Um projeto interativo desenvolvido em Python onde podes desenhar a tua própria pista de corrida e, em seguida, assistir a uma Inteligência Artificial a aprender a conduzir nela de forma autónoma utilizando Neuroevolução (NEAT).

> **Aviso:** Este projeto encontra-se atualmente em desenvolvimento. 🚧

## 🌟 Funcionalidades Atuais
* **Construtor de Pistas**: Uma interface interativa rápida e fluida desenvolvida com `pyray` (Raylib) que permite aos utilizadores desenharem pistas de corrida de forma livre.
* **Exportação Simples**: Guarda as pistas personalizadas instantaneamente como imagens PNG (`assets/pista.png`) prontas a serem lidas pelo modelo de IA.

## 🚀 Próximos Passos (Em Desenvolvimento)
* **Integração NEAT**: Implementação do algoritmo NEAT (`neat-python`) para gerar e treinar os agentes (carros virtuais).
* **Física e Colisões**: Desenvolvimento do sistema de deteção de colisão dos veículos com as margens da pista desenhada.
* **Simulação Visual**: Visualização em tempo real da evolução da rede neuronal, geração após geração, a tentar completar o circuito.

## ⚙️ Como Executar

**1. Instalar as dependências** Certifica-te de que tens o Python instalado e executa na raiz do projeto:  
`pip install -r requirements.txt`

**2. Desenhar uma pista** Para abrires a interface de criação de pistas:  
`python src/drawer.py`

**Controlos da Interface:**
* **Botão Esquerdo do Rato**: Desenhar a estrada.
* **Tecla 'S'**: Guardar a pista (será exportada para `assets/pista.png`).
* **Tecla 'ESC'**: Sair da aplicação.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **PyRay (Raylib)** - Para renderização gráfica da interface e do simulador.
* **NEAT-Python** - Algoritmo de *NeuroEvolution of Augmenting Topologies* para a Inteligência Artificial.
