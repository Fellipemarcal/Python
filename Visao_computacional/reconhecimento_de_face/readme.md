<h1 align="center">👤 Detecção Facial com OpenCV</h1>

<p align="center">
  Sistema simples de detecção de rostos em tempo real utilizando
  visão computacional e webcam.
</p>

<hr>

<h2>📌 Descrição</h2>
<p>
  Este projeto utiliza a biblioteca <strong>OpenCV</strong> para realizar
  a detecção de rostos em tempo real a partir da webcam.
  O algoritmo é baseado em <strong>Haar Cascades</strong>, um método clássico
  de visão computacional para reconhecimento de padrões faciais.
</p>

<p>
  Cada rosto detectado é destacado com um retângulo e uma identificação
  visual exibindo nome e status.
</p>

<hr>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li>Captura de vídeo em tempo real via webcam</li>
  <li>Conversão da imagem para escala de cinza</li>
  <li>Detecção facial utilizando Haar Cascade</li>
  <li>Desenho de bounding box ao redor do rosto</li>
  <li>Exibição de nome e status na tela</li>
</ul>

<hr>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>NumPy</li>
  <li>Haar Cascade Classifier</li>
</ul>

<hr>

<h2>📂 Estrutura do projeto</h2>
<pre>
FaceDetection/
│
├── face_detection.py
├── README.md
└── haarcascade_frontalface_default.xml
</pre>

<p>
  <em>Obs:</em> O arquivo Haar Cascade pode ser carregado diretamente
  da instalação do OpenCV.
</p>

<hr>

<h2>⚙️ Instalação</h2>

<ol>
  <li>Clone o repositório</li>
</ol>

<pre>
git clone https://github.com/seu-usuario/face-detection-opencv.git
</pre>

<ol start="2">
  <li>Instale as dependências</li>
</ol>

<pre>
pip install opencv-python numpy
</pre>

<hr>

<h2>▶️ Como usar</h2>

<ol>
  <li>Conecte uma webcam ao computador</li>
  <li>Execute o script</li>
</ol>

<pre>
python face_detection.py
</pre>

<p>
  Pressione a tecla <strong>Q</strong> para encerrar a aplicação.
</p>

<hr>

<h2>📸 Demonstração</h2>

<p align="center">
  <img src="images/demo.png" alt="Detecção facial em tempo real" width="600">
</p>

<p>
  A aplicação exibe:
</p>
<ul>
  <li>Rostos detectados em tempo real</li>
  <li>Retângulo delimitador</li>
  <li>Identificação com nome e status</li>
</ul>

<hr>

<h2>🔮 Melhorias futuras</h2>
<ul>
  <li>Reconhecimento facial com treinamento de modelos</li>
  <li>Identificação automática de múltiplas pessoas</li>
  <li>Integração com banco de dados</li>
  <li>Uso de modelos baseados em Deep Learning</li>
</ul>

<hr>

<h2>👤 Autor</h2>
<p>
  <strong>Fellipe da Silva Marçal</strong><br>
  Desenvolvedor Python & Visão Computacional<br>
  GitHub: <a href="https://github.com/seu-usuario">seu-usuario</a>
</p>

