# 🎵 Youtube & SoundCloud Downloader 🎥

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Repo Size](https://img.shields.io/github/repo-size/MusashiShI/YoutubeSoundcloud_Downloade)  

🚀 Um aplicativo simples e moderno para baixar vídeos do **YouTube** e áudios do **SoundCloud**. Desenvolvido em **Python** com uma interface gráfica amigável.

---

## ✨ Funcionalidades

✅ **Download de Vídeos do YouTube**
- Suporta resoluções de **144p até 4K60fps**.
- Opção para baixar **somente o áudio**.

✅ **Download de Áudios do SoundCloud**
- Baixa músicas diretamente no formato **MP3**.

✅ **Interface Moderna**
- Tema escuro e design intuitivo usando `ttkbootstrap`.

✅ **Organização Automática**
- Os downloads são salvos em pastas separadas (`Youtube/` e `Soundcloud/`).

---

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- 🐍 **Python 3.8 ou superior** → [Baixe o Python](https://www.python.org/downloads/).
- 🌍 **Git** (opcional, para clonar o repositório) → [Baixe o Git](https://git-scm.com/).

---

## 🚀 Como Usar

### 1️⃣ Clonar o Repositório
Abra o terminal e execute:
```bash
git clone git@github.com:MusashiShI/YoutubeSoundcloud_Downloade.git
cd YoutubeSoundcloud_Downloade
```

### 2️⃣ Criar e Ativar o Ambiente Virtual (Recomendado)
Crie um ambiente virtual para evitar conflitos de dependências:
```bash
python -m venv venv  # Criar o ambiente virtual
source venv/bin/activate  # Ativar no Linux/macOS
venv\Scripts\activate  # Ativar no Windows
```

### 3️⃣ Instalar as Dependências
Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Programa
```bash
python main.py
```

---

## 🎨 Como Usar o Aplicativo

1️⃣ **Insira a URL** → Cole o link do **YouTube** ou **SoundCloud**.
2️⃣ **Processar URL** → Clique em "Process URL" para verificar e exibir opções.
3️⃣ **Selecionar Qualidade** → Escolha a resolução desejada para vídeos.
4️⃣ **Baixar** → Clique em "Download" e aguarde! 🎶📥

Os arquivos serão salvos automaticamente em suas respectivas pastas!

---

## 🤝 Como Contribuir

💡 **Contribuições são bem-vindas!** Siga os passos abaixo:

1️⃣ **Faça um Fork** do repositório.
2️⃣ **Crie um Branch** para sua feature ou correção:
```bash
git checkout -b minha-feature
```
3️⃣ **Faça Commit das suas alterações**:
```bash
git commit -m "Adicionando nova funcionalidade"
```
4️⃣ **Envie para o Repositório**:
```bash
git push origin minha-feature
```
5️⃣ **Abra um Pull Request no GitHub**.

---

## 📁 Estrutura do Projeto

```
YoutubeSoundcloud_Downloade/
├── main.py              # Código principal do aplicativo
├── requirements.txt     # Lista de dependências
├── README.md            # Este arquivo
├── venv/                # Ambiente virtual (se criado)
├── Youtube/             # Pasta para downloads do YouTube
└── Soundcloud/          # Pasta para downloads do SoundCloud
```

---

## 📜 Licença

📝 Este projeto está licenciado sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 📬 Contato

📌 **GitHub**: [MusashiShI](https://github.com/MusashiShI)  
📧 **Email**: beselgamain@gmail.com  

---

## 🎉 Agradecimentos

💙 **Agradecimentos especiais às bibliotecas incríveis usadas neste projeto**:
- 🎨 [`ttkbootstrap`](https://ttkbootstrap.readthedocs.io/en/latest/) → Interface moderna.
- 📥 [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) → Download eficiente de vídeos e músicas.

🚀 **Divirta-se baixando seus vídeos e músicas favoritas!** 🎶🔥
