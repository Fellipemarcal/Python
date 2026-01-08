<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    
</head>
<body>

<h1>🌦️ Weather App – Python & Tkinter</h1>

<hr>

<h2>📌 Descrição do Projeto</h2>

<p>
Este projeto consiste em uma <strong>aplicação de previsão do tempo</strong>
desenvolvida em <strong>Python</strong>, utilizando a biblioteca
<strong>Tkinter</strong> para a interface gráfica e a
<strong>API OpenWeather</strong> para obter dados meteorológicos em tempo real.
</p>

<p>
O objetivo principal do projeto é aplicar conceitos de:
</p>

<ul>
    <li>Consumo de APIs REST</li>
    <li>Manipulação de dados JSON</li>
    <li>Interfaces gráficas com Tkinter</li>
    <li>Tratamento de erros em aplicações Python</li>
</ul>

---

<h2>⚙️ Funcionalidades</h2>

<ul>
    <li>Pesquisa de cidades em tempo real</li>
    <li>Exibição da temperatura atual (°C)</li>
    <li>Exibição da umidade</li>
    <li>Temperatura mínima e máxima</li>
    <li>Identificação do país da cidade</li>
    <li>Exibição de data e hora atuais</li>
    <li>Ícones dinâmicos (dia / noite)</li>
    <li>Tratamento de erros para cidades inválidas</li>
</ul>

---

<h2>🧰 Tecnologias Utilizadas</h2>

<ul>
    <li><strong>Python 3</strong></li>
    <li><strong>Tkinter</strong> (interface gráfica)</li>
    <li><strong>OpenWeather API</strong></li>
    <li><strong>urllib</strong> (requisições HTTP sem bibliotecas externas)</li>
    <li><strong>Pillow (PIL)</strong> para manipulação de imagens</li>
</ul>

---

<h2>📂 Estrutura do Projeto</h2>

<pre>
weather_app/
│
├── main.py
├── logo.png
├── sun.png
├── moon.png
├── README.html
</pre>

---

<h2>🔑 Configuração da API</h2>

<p>
Este projeto utiliza a <strong>OpenWeather API</strong>.
Para executá-lo corretamente, é necessário obter uma chave de API gratuita.
</p>

<ol>
    <li>Acesse <a href="https://openweathermap.org/" target="_blank">https://openweathermap.org</a></li>
    <li>Crie uma conta gratuita</li>
    <li>Copie sua API Key</li>
    <li>Insira a chave no código</li>
</ol>

<pre>
API_KEY = "SUA_API_KEY_AQUI"
</pre>

<p>
⚠️ <strong>Recomendação:</strong> não publique sua API Key em repositórios públicos.
</p>

---

<h2>▶️ Como Executar o Projeto</h2>

<ol>
    <li>Certifique-se de ter o Python 3 instalado</li>
    <li>Instale a biblioteca Pillow:</li>
</ol>

<pre>
pip install pillow
</pre>

<ol start="3">
    <li>Execute o arquivo principal:</li>
</ol>

<pre>
python main.py
</pre>

---

<h2>🧪 Tratamento de Erros</h2>

<p>
A aplicação verifica possíveis erros retornados pela API, como:
</p>

<ul>
    <li>Cidade não encontrada</li>
    <li>API Key inválida</li>
    <li>Problemas de conexão com a internet</li>
</ul>

<p>
Isso evita erros como <code>KeyError: 'main'</code> durante a execução.
</p>

---

<h2>🎯 Objetivo Educacional</h2>

<p>
Este projeto tem caráter <strong>educacional</strong> e é ideal para estudantes
que desejam aprender:
</p>

<ul>
    <li>Integração com APIs externas</li>
    <li>Criação de interfaces gráficas em Python</li>
    <li>Boas práticas de programação</li>
</ul>

---

<h2>📜 Licença</h2>

<p>
Este projeto é de uso livre para fins educacionais.
Sinta-se à vontade para modificar, melhorar e reutilizar o código.
</p>

---

<h2>👨‍💻 Autor</h2>

<p>
Projeto desenvolvido para fins de aprendizado em Python e Data Science.
</p>

</body>
</html>

