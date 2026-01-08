<h1 align="center">✋ Detecção de Mãos com MediaPipe</h1>

<p align="center">
  Aplicação de visão computacional para detecção e rastreamento de mãos
  em tempo real utilizando webcam.
</p>

<hr>

<h2>📌 Descrição</h2>
<p>
  Este projeto utiliza a biblioteca <strong>MediaPipe</strong> em conjunto
  com <strong>OpenCV</strong> para detectar e rastrear mãos em tempo real
  a partir da webcam.
</p>

<p>
  O sistema identifica os principais <em>landmarks</em> da mão e desenha
  as conexões entre eles, permitindo o desenvolvimento de aplicações
  interativas baseadas em gestos.
</p>

<hr>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li>Captura de vídeo em tempo real via webcam</li>
  <li>Detecção de até duas mãos simultaneamente</li>
  <li>Rastreamento dos landmarks da mão</li>
  <li>Desenho das conexões entre os pontos da mão</li>
  <li>Base para projetos de controle por gestos</li>
</ul>

<hr>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
</ul>

<hr>

<h2>📂 Estrutura do projeto</h2>
<pre>
HandTracking/
│
├── hand_tracking.py
└── README.md
</pre>

<hr>

<h2>⚙️ Instalação</h2>

<ol>
  <li>Clone o repositório</li>
</ol>

<pre>
git clone https://github.com/seu-usuario/hand-tracking-mediapipe.git
</pre>

<ol start="2">
  <li>Instale as dependências</li>
</ol>

<pre>
pip install opencv-python mediapipe
</pre>

<hr>

<h2>▶️ Como usar</h2>

<ol>
  <li>Conecte uma webcam ao computador</li>
  <li>Execute o script</li>
</ol>

<pre>
python hand_tracking.py
</pre>

<p>
  Pressione a tecla <strong>Q</strong> para encerrar a aplicação.
</p>

<hr>

<h2>📸 Demonstração</h2>

<p align="center">
  <img src="images/demo.gif" alt="Detecção de mãos com MediaPipe" width="600">
</p>

<p>
  A aplicação exibe:
</p>
<ul>
  <li>Pontos (landmarks) da mão</li>
  <li>Conexões anatômicas entre os dedos</li>
  <li>Rastreamento em tempo real</li>
</ul>

<hr>

<h2>🧠 Como funciona</h2>
<ul>
  <li>O frame da webcam é convertido de BGR para RGB</li>
  <li>O MediaPipe Hands detecta as mãos no frame</li>
  <li>Os landmarks são extraídos e desenhados na imagem</li>
</ul>

<hr>

<h2>🔮 Melhorias futuras</h2>
<ul>
  <li>Reconhecimento de gestos específicos</li>
  <li>Integração com controle de volume ou mídia</li>
  <li>Aplicações interativas (jogos, interfaces touchless)</li>
  <li>Suporte a mais dispositivos de entrada</li>
</ul>

<hr>

<h2>👤 Autor</h2>
<p>
  <strong>Fellipe da Silva Marçal</strong><br>
  Desenvolvedor Python & Visão Computacional<br>
  GitHub: <a href="https://github.com/seu-usuario">seu-usuario</a>
</p>

