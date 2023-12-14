from pytube import YouTube
from pydub import AudioSegment
import os

videos = [] #Array com links de vídeos para fazer o download

def baixar_mp3(url, destino):
    try:
        yt = YouTube(url)     

        stream = yt.streams.filter(only_audio=True).last()  # Coletar o último arquivo da lista que é o de melhor qualidade disponível      
        arquivo = stream.download(output_path=destino)

        # Converter para MP3 usando pydub
        audio = AudioSegment.from_file(arquivo)
        audio.export(f"{destino}/{yt.title.replace('/','-')}.mp3", format="mp3")

        os.remove(arquivo) # Excluir o arquivo .webm

        print(yt.title + " - Download finalizado com sucesso!")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

pasta_destino = "/home/csaecmdskxxx/glayson"
for i in videos:
    baixar_mp3(i, pasta_destino)
