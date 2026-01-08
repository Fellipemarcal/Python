<h1 align="center">🎚️ Controle de Volume por Gestos da Mão</h1>

<p align="center">
  Controle o volume do sistema em tempo real utilizando gestos da mão
  capturados pela webcam, com visão computacional.
</p>

<hr>

<h2>📌 Descrição</h2>
<p>
  Este projeto permite controlar o volume do sistema operacional Windows
  por meio da distância entre o polegar e o dedo indicador da mão.
  A detecção é feita em tempo real utilizando <strong>MediaPipe</strong>
  para rastreamento dos pontos da mão e <strong>OpenCV</strong> para
  processamento de imagem.
</p>

<p>
  Quanto maior a distância entre os dedos, maior será o volume do sistema.
</p>

<hr>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li>Detecção de mão em tempo real</li>
  <li>Rastreamento preciso dos landmarks da mão</li>
  <li>Controle suave do volume do sistema</li>
  <li>Barra visual de volume integrada</li>
  <li>Uso de módulo personalizado para hand tracking</li>
</ul>

<hr>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
  <li>NumPy</li>
  <li>PyCaw (controle de áudio do Windows)</li>
</ul>

<hr>

<h2>📂 Estrutura do projeto</h2>
<pre>
HandGestureVolumeController/
│
├── HandGestureVolumeController.py
├── HandTrackingModule.py
└── README.md
</pre>

<hr>

<h2>⚙️ Instalação</h2>

<ol>
  <li>Clone o repositório</li>
</ol>

<pre>
git clone https://github.com/seu-usuario/hand-gesture-volume-controller.git
</pre>

<ol start="2">
  <li>Instale as dependências</li>
</ol>

<pre>
pip install opencv-python mediapipe numpy pycaw comtypes
</pre>

<hr>

<h2>▶️ Como usar</h2>
<ol>
  <li>Conecte uma webcam ao computador</li>
  <li>Execute o script principal</li>
</ol>

<pre>
python HandGestureVolumeController.py
</pre>

<p>
  Utilize a distância entre o polegar e o indicador para ajustar o volume.
  Pressione <strong>ESC</strong> ou <strong>Enter</strong> para encerrar o programa.
</p>

<hr>

<h2>📸 Demonstração</h2>
<p>
  A interface exibe:
</p>
<ul>
  <li>Landmarks da mão detectada</li>
  <li>Barra de volume dinâmica</li>
  <li>Porcentagem do volume atual do sistema</li>
</ul>

<hr>

<h2>🔮 Melhorias futuras</h2>
<ul>
  <li>Suporte a múltiplas mãos</li>
  <li>Novos gestos para controle de mídia</li>
  <li>Compatibilidade com outros sistemas operacionais</li>
  <li>Interface gráfica dedicada</li>
</ul>

<hr>

<h2>👤 Autor</h2>
<p>
  <strong>Fellipe da Silva Marçal</strong><br>
  Desenvolvedor Python & Visão Computacional<br>
  GitHub: <a href="https://github.com/Fellipemarcal">seu-usuario</a>
</p>

