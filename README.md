
# Telegram File Uploader Bot
Bu proje, medya dosyalarını yüklemek, URL'leri kısaltmak, URL'den dosya yüklemek ve **envs.sh URL'leriyle etkileşimde bulunmak** için bir Telegram botudur. Bot, kullanıcıların dosya yükleme, URL kısaltma ve paylaşma işlemlerini kolaylaştırmak için çeşitli komutlar sunar.

## Özellikler
- Medya dosyalarını yükleyebilme (gizli yükleme seçeneği ile).
- Uzun URL'leri kısa URL'lere dönüştürme.
- URL'den medya dosyası yükleme.
- Yüklenen dosyaları paylaşma, önizleme ve kopyalama için butonlar oluşturma.
- **envs.sh** URL'lerini inline query olarak paylaşabilme.

## Gereksinimler
Bu projeyi çalıştırmadan önce aşağıdaki gereksinimlerin karşılandığından emin olun:
- Python 3.10 veya üstü
- [Telegram bot token](https://core.telegram.org/bots#6-botfather) (BotFather aracılığıyla alınabilir)
- [Telegram api anahtarları](https://my.telegram.org)

## Kurulum
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/suphiozturk8/envs_sh_bot.git
   cd envs_sh_bot
   ```
2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. `config.ini` dosyasını düzenleyin ve kendi **Telegram bot token**, **API ID**, ve **API Hash** bilgilerinizi girin:
   ```ini
   [telegram]
   name = uploader_bot
   api_id = YOUR_API_ID
   api_hash = YOUR_API_HASH
   bot_token = YOUR_BOT_TOKEN
   ```
4. Botu başlatın:
   ```bash
   python -m bot
   ```

## Kullanım
Bot, aşağıdaki komutları destekler:
### Genel Komutlar
- `/start`: Botu başlatır ve kullanım talimatlarını gösterir.
- `/help`: Botun işlevleri hakkında bilgi verir.

### Dosya Yükleme
- `/upload`: Yanıtladığınız bir medyayı yükler.
- `/upload -s`: Gizli dosya yükleme.
- `/upload_url <URL>`: Verilen URL'deki bir dosyayı yükler.
- `/upload_url -s <URL>`: URL'den gizli yükleme.

### URL İşlemleri
- `/shorten <URL>`: Verilen bir URL'yi kısaltır.

### Inline Özelliği
Bot, **envs.sh** URL'lerini inline query olarak alabilir. Bu özellik, kullanıcıların bot üzerinden bağlantı paylaşmalarını sağlar. Kullanıcılar, `@envs_sh_bot <URL>` şeklinde bağlantılarını paylaşabilirler.

### Örnekler
1. **Dosya yükleme**  
   Medyaya yanıt olarak şu komutu girin:  
   ```bash
   /upload
   ```
2. **URL'den yükleme**  
   ```bash
   /upload_url https://example.com/image.jpg
   ```
3. **URL kısaltma**  
   ```bash
   /shorten https://example.com
   ```
4. **Inline URL Paylaşma**  
   `@envs_sh_bot` ile bir **envs.sh** URL'si paylaşın:  
   ```bash
   @envs_sh_bot https://envs.sh/vD3.jpg
   ```

## Proje Yapısı
<details><summary><b>Genişletmek için tıklayın!</b></summary>

```plaintext
.
├── bot/
│   ├── __init__.py          # Bot istemcisi
│   ├── __main__.py          # Bot çalıştırma dosyası
│   ├── config.py            # Bot yapılandırması
│   ├── plugins/
│   │   ├── __init__.py      # Plugin başlatıcısı
│   │   ├── start.py         # /start ve /help komutları
│   │   ├── upload.py        # /upload komutu
│   │   ├── url.py           # /shorten ve /upload_url komutları
│   │   └── inline.py        # Inline query özelliği
│   └── utils/
│       ├── __init__.py      # Yardımcı fonksiyonlar başlatıcısı
│       ├── buttons.py       # Buton oluşturma işlevi
│       ├── file_uploader.py # Dosya yükleme ve URL kısaltma sınıfı
│       ├── url.py           # envs.sh URL doğrulama işlevi
│       └── logger.py        # Loglama yapılandırması
├── config.ini               # Bot ayarları
├── requirements.txt         # Gereksinim dosyası
├── README.md                # Proje dokümantasyonu
```

</details>

## Teknolojiler
- **[Pyrogram (Kurigram)](https://docs.kurigram.live)**: Telegram API ile etkileşim.
- **[Aiohttp](https://docs.aiohttp.org/)**: Asenkron HTTP istekleri.

## Lisans
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
