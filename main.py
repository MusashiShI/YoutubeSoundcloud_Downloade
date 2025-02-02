import os
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from yt_dlp import YoutubeDL

# Função para criar pastas se não existirem
def create_folders():
    if not os.path.exists("Youtube"):
        os.makedirs("Youtube")
    if not os.path.exists("Soundcloud"):
        os.makedirs("Soundcloud")

# Função para baixar vídeos do YouTube
def download_youtube_video(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality[:-1]}][fps<=60]+bestaudio/best' if quality != 'audio' else 'bestaudio/best',
            'outtmpl': os.path.join("Youtube", '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: update_status(d)],
        }
        with YoutubeDL(ydl_opts) as ydl:
            status_label.config(text=f"Downloading: {url} in {quality}...")
            root.update()  # Atualiza a interface
            ydl.download([url])
            status_label.config(text="Download completed!")
            Messagebox.show_info("Success", "Download completed successfully!")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")
        Messagebox.show_error("Error", f"An error occurred: {e}")

# Função para baixar áudios do SoundCloud
def download_soundcloud_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join("Soundcloud", '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: update_status(d)],
        }
        with YoutubeDL(ydl_opts) as ydl:
            status_label.config(text=f"Downloading SoundCloud audio: {url}...")
            root.update()  # Atualiza a interface
            ydl.download([url])
            status_label.config(text="Download completed!")
            Messagebox.show_info("Success", "Download completed successfully!")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")
        Messagebox.show_error("Error", f"An error occurred: {e}")

# Função para atualizar o status do download
def update_status(data):
    if data['status'] == 'downloading':
        status_label.config(text=f"Downloading: {data['_percent_str']} complete")
    elif data['status'] == 'finished':
        status_label.config(text="Download completed!")

# Função para processar o link e exibir opções
def process_url():
    url = url_entry.get()
    if not url:
        Messagebox.show_error("Error", "Please enter a URL.")
        return

    if 'youtube.com' in url or 'youtu.be' in url:
        try:
            title_label.config(text="YouTube video detected.")
            qualities = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p (4K)', 'audio']
            quality_combobox['values'] = qualities
            quality_combobox.current(0)
            quality_frame.pack()
            download_button.config(command=lambda: download_youtube_video(url, quality_combobox.get()))
        except Exception as e:
            Messagebox.show_error("Error", f"An error occurred: {e}")
    elif 'soundcloud.com' in url:
        title_label.config(text="SoundCloud audio detected.")
        quality_frame.pack_forget()
        download_button.config(command=lambda: download_soundcloud_audio(url))
    else:
        Messagebox.show_error("Error", "Unsupported URL. Please provide a valid YouTube or SoundCloud link.")

# Configuração da interface gráfica
root = ttk.Window(themename="darkly")  # Tema escuro
root.title("YouTube & SoundCloud Downloader")
root.geometry("500x350")

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=BOTH, expand=True)

# Entrada de URL
url_label = ttk.Label(main_frame, text="Enter URL:", font=("Helvetica", 12))
url_label.pack(pady=5)
url_entry = ttk.Entry(main_frame, width=50, font=("Helvetica", 12))
url_entry.pack(pady=5)

# Botão para processar URL
process_button = ttk.Button(main_frame, text="Process URL", command=process_url, bootstyle=PRIMARY)
process_button.pack(pady=10)

# Título do vídeo/áudio
title_label = ttk.Label(main_frame, text="", wraplength=400, font=("Helvetica", 12))
title_label.pack(pady=5)

# Frame para seleção de qualidade (YouTube)
quality_frame = ttk.Frame(main_frame)
quality_label = ttk.Label(quality_frame, text="Select quality:", font=("Helvetica", 12))
quality_label.pack(side=LEFT, padx=5)
quality_combobox = ttk.Combobox(quality_frame, width=15, font=("Helvetica", 12))
quality_combobox.pack(side=LEFT, padx=5)

# Botão de download
download_button = ttk.Button(main_frame, text="Download", bootstyle=SUCCESS)
download_button.pack(pady=10)

# Status do download
status_label = ttk.Label(main_frame, text="", foreground="white", font=("Helvetica", 12))
status_label.pack(pady=10)

# Criar pastas ao iniciar o programa
create_folders()

# Iniciar a interface
root.mainloop()