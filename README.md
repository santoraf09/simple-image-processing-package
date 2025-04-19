# Simple Image Processing

Pacote Python simples para processamento de imagens, desenvolvido como exercício prático do curso da DIO: *"Descomplicando a criação de pacotes de processamento de imagens com Python"*.

## 📦 Funcionalidades

- Leitura de imagens
- Visualização com Matplotlib
- Plotagem de múltiplas imagens lado a lado
- Transferência de histograma (simulada)

## 🚀 Instalação

Você pode instalar diretamente do Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ simple-image-processing

🧪 Exemplo de uso
python
Copiar
Editar
from image_processing.utils import io, plot
from image_processing.processing import combination

img1 = io.read_image("imagem1.jpg")
img2 = io.read_image("imagem2.jpg")

result = combination.transfer_histogram(img1, img2)
plot.plot_result(img1, img2, result)

📁 Estrutura do pacote
markdown
Copiar
Editar
image_processing/
├── processing.py
├── utils.py
└── __init__.py
📌 Requisitos
Python >= 3.8

numpy

matplotlib

imageio

👨‍💻 Autor
Rafael Santiago

yaml
Copiar
Editar

---

Agora é só:
1. Subir esse `README.md` no GitHub.
2. Rodar `python setup.py sdist bdist_wheel`
3. Publicar com:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*