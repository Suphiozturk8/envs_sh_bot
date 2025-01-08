
from pyrogram import Client, filters

HELP_MESSAGE = """
**Yardım Menüsü**  
Dosya Yükleme ve URL Kısaltma Botu'nun komut listesi:

**Genel Komutlar:**  
- `/start` – Botu başlat ve hoş geldin mesajını al.  
- `/help` – Bu yardım menüsünü görüntüle.  

**Dosya Yükleme:**  
- `/upload` – Yanıtladığınız bir medyayı yükler.  
- `/upload -s` – Gizli dosya yükleme.  
- `/upload_url <URL>` – Verilen URL'deki bir dosyayı yükler.  
- `/upload_url -s <URL>` – URL'den gizli yükleme.  

**URL İşlemleri:**  
- `/shorten <URL>` – Verilen URL'yi kısaltır.  

**Örnek Kullanım:**  
1. **Bir dosyayı yüklemek için:**  
   Medyaya yanıt verip şu komutu kullanın:  
   `/upload`  
   
2. **URL kısaltmak için:**  
   `/shorten https://example.com`  

3. **URL'den dosya yüklemek için:**  
   `/upload_url https://example.com/file.jpg`  

**Notlar:**  
- Maksimum dosya boyutu: **100 MB**  
- Gizli yükleme seçeneği ile dosyalarınız daha güvenli bir şekilde paylaşılır.  

Sorularınız veya geri bildirimleriniz varsa bot sahibine ulaşabilirsiniz. (@Syupie)

İyi kullanımlar dilerim!
"""

START_MESSAGE = """
Merhaba!
Ben dosya yükleme ve URL kısaltma botuyum.

**Neler yapabilirim?**  
- Medya dosyalarını yükleyebilirim (gizli yükleme seçeneği ile).  
- Uzun URL'leri kısa hale getirebilirim.  
- Bir URL'den medya dosyası alıp, yükleyebilirim.  

**Başlamak için bir komut yazın veya /help komutu ile detaylı bilgi alın.**

İyi kullanımlar!
"""


@Client.on_message(filters.command(["start", "help"]))
async def start_command(client, message):
    if "start" in message.command:
        text = START_MESSAGE
    elif "help" in message.command:
        text = HELP_MESSAGE
    
    await message.reply_text(text=text)
