# Reconhecimento-IA-TensorFlow-
Este projeto demonstra como classificar imagens utilizando o modelo pré-treinado ResNet50 da biblioteca TensorFlow/Keras. O código carrega uma imagem a partir de uma URL, realiza o pré-processamento necessário e exibe as três classes mais prováveis com suas respectivas probabilidades.

Funcionalidades

Carrega imagens diretamente de URLs.

Pré-processa a imagem para ser compatível com o modelo ResNet50.

Realiza previsões usando o modelo pré-treinado do ImageNet.

Exibe a imagem com a previsão mais provável no título.

Lista as 3 previsões mais prováveis no console.

Tecnologias utilizadas

Python 3.10+

TensorFlow 2.x

Keras

NumPy

Matplotlib

Pillow (PIL)

Requests

Estrutura do código
.
├── main.py          # Código principal para carregar a imagem, processar e exibir previsões
└── README.md        # Este arquivo

Requisitos

Para rodar o código, você precisa ter Python instalado e as seguintes bibliotecas:

pip install tensorflow matplotlib pillow requests numpy


Observação: O código utiliza o modelo ResNet50 pré-treinado, que será baixado automaticamente pelo Keras na primeira execução.

Como usar

Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>


Execute o script:

python main.py


O script carregará a imagem definida na variável url, exibirá a imagem com a previsão mais provável e imprimirá as três principais previsões no console.

Personalização

Para testar com outra imagem, basta alterar a variável url no código:

url = "URL_DA_SUA_IMAGEM"

Exemplo de saída

A imagem é exibida com a classe mais provável no título.

No console, você verá algo como:

Top 3 previsões:
pug: 98.75%
bull_mastiff: 0.65%
boxer: 0.45%
