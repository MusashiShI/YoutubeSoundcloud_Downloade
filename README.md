# Youtube & SoundCloud Downloader

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo Size](https://img.shields.io/github/repo-size/MusashiShI/YoutubeSoundcloud_Downloade)

Um aplicativo simples e moderno para baixar vídeos do YouTube e áudios do SoundCloud. Desenvolvido em Python com uma interface gráfica amigável.

---

## Funcionalidades

- **Download de Vídeos do YouTube**:
  - Suporta resoluções de 144p até 4K60fps.
  - Opção para baixar apenas o áudio.
- **Download de Áudios do SoundCloud**:
  - Baixa músicas diretamente no formato MP3.
- **Interface Moderna**:
  - Tema escuro e design intuitivo.
- **Organização Automática**:
  - Os downloads são salvos em pastas separadas (`Youtube` e `Soundcloud`).

---

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- **Python 3.8 ou superior**:
  - [Baixe o Python](https://www.python.org/downloads/).
- **Git** (opcional, para clonar o repositório):
  - [Baixe o Git](https://git-scm.com/).

---

## Como Usar

### 1. Clonar o Repositório
Abra o terminal e execute o seguinte comando para clonar o repositório:
```bash
git clone git@github.com:MusashiShI/YoutubeSoundcloud_Downloade.git
cd YoutubeSoundcloud_Downloade
```

2. Instalar as Dependências
Instale as bibliotecas necessárias usando o pip:
```bash
pip install -r requirements.txt
```

3. Executar o Programa
```bash
python main.py
```
4. Usar o Aplicativo
Insira a URL:
Cole o link do YouTube ou SoundCloud no campo de texto.

Processe a URL:
Clique em "Process URL" para verificar o link e exibir as opções de qualidade (se for um vídeo do YouTube).

Selecione a Qualidade:
Para vídeos do YouTube, escolha a qualidade desejada no menu suspenso.

Baixe:
Clique em "Download" para iniciar o download.

O arquivo será salvo na pasta correspondente (Youtube ou Soundcloud).


Como Contribuir
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um Fork do repositório.

Crie um Branch para sua feature ou correção:
```bash
git checkout -b minha-feature
```
Faça Commit das suas alterações:
```bash
git commit -m "Adicionando nova funcionalidade"
```
Envie para o Repositório:
```bash
git push origin minha-feature
```
Abra um Pull Request no GitHub.

Estrutura do Projeto
YoutubeSoundcloud_Downloade/
├── main.py              # Código principal do aplicativo
├── requirements.txt     # Lista de dependências
├── README.md            # Este arquivo
├── Youtube/             # Pasta para downloads do YouTube
└── Soundcloud/          # Pasta para downloads do SoundCloud
Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

GitHub: MusashiShI

Email: beselgamain@gmail.com

Agradecimentos
ttkbootstrap pela interface moderna.
yt-dlp pela biblioteca de download.
