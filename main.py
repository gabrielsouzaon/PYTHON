import os
import yt_dlp

output_folder = "AudiosBaixados"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Função para baixar o áudio
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixa a melhor qualidade de áudio disponível
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Salva com o título do áudio
        'postprocessors': [{  # Processa o arquivo após o download
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Converte para o formato mp3
            'preferredquality': '192',  # Qualidade do áudio
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído! O áudio está salvo na pasta:", output_folder)
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)

video_url = input("Cole aqui a sua URL: ")
download_audio(video_url)
