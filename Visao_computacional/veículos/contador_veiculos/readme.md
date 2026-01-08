<h1 align="center">🚗 Contador de Veículos com OpenCV</h1>

<p align="center">
  Sistema de contagem automática de veículos em vídeo utilizando
  visão computacional e processamento de imagens.
</p>

<hr>

<h2>📌 Descrição</h2>
<p>
  Este projeto realiza a <strong>detecção e contagem de veículos</strong>
  em um vídeo utilizando técnicas clássicas de visão computacional
  com a biblioteca <strong>OpenCV</strong>.
</p>

<p>
  A contagem é feita quando o centro do veículo cruza uma linha virtual
  definida na imagem, simulando um sistema de monitoramento de tráfego.
</p>

<hr>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li>Leitura de vídeo a partir de arquivo (.mp4)</li>
  <li>Subtração de fundo para detecção de objetos em movimento</li>
  <li>Aplicação de filtros e operações morfológicas</li>
  <li>Detecção de contornos representando veículos</li>
  <li>Contagem automática ao cruzar linha virtual</li>
  <li>Exibição do contador em tempo real</li>
</ul>

<hr>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>NumPy</li>
</ul>

<hr>

<h2>📂 Estrutura do projeto</h2>
<pre>
VehicleCounter/
│
├── video.mp4
├── vehicle_counter.py
└── README.md
</pre>

<hr>

<h2>⚙️ Instalação</h2>

<ol>
  <li>Clone o repositório</li>
</ol>

<pre>
git clone https://github.com/seu-usuario/vehicle-counter-opencv.git
</pre>

<ol start="2">
  <li>Instale as dependências</li>
</ol>

<pre>
pip install opencv-python opencv-contrib-python numpy
</pre>

<p>
  <em>Obs:</em> O módulo <code>bgsegm</code> requer o pacote
  <strong>opencv-contrib-python</strong>.
</p>

<hr>

<h2>▶️ Como usar</h2>

<ol>
  <li>Adicione o arquivo <code>video.mp4</code> ao diretório do projeto</li>
  <li>Execute o script</li>
</ol>

<pre>
python vehicle_counter.py
</pre>

<p>
  Pressione a tecla <strong>ESC</strong> para encerrar a aplicação.
</p>

<hr>

<h2>📸 Demonstração</h2>

<p align="center">
  <img src="images/demo.gif" alt="Contagem de veículos em vídeo" width="600">
</p>

<p>
  A aplicação exibe:
</p>
<ul>
  <li>Vídeo original com bounding boxes</li>
  <li>Linha virtual de contagem</li>
  <li>Número total de veículos detectados</li>
</ul>

<hr>

<h2>🧠 Como funciona</h2>
<ul>
  <li>O vídeo é convertido para escala de cinza</li>
  <li>É aplicada subtração de fundo (MOG)</li>
  <li>Filtros e operações morfológicas removem ruídos</li>
  <li>Contornos são detectados e filtrados por tamanho</li>
  <li>O centro do objeto é monitorado ao cruzar a linha</li>
</ul>

<hr>

<h2>🔮 Melhorias futuras</h2>
<ul>
  <li>Classificação de tipos de veículos</li>
  <li>Contagem bidirecional</li>
  <li>Uso de Deep Learning (YOLO, SSD)</li>
  <li>Exportação de dados para CSV</li>
  <li>Interface gráfica dedicada</li>
</ul>

<hr>

<h2>👤 Autor</h2>
<p>
  <strong>Fellipe da Silva Marçal</strong><br>
  Desenvolvedor Python & Visão Computacional<br>
  GitHub: <a href="https://github.com/seu-usuario">seu-usuario</a>
</p>

