
import aiohttp


class AsyncFileUploader:
    def __init__(self, base_url="https://envs.sh"):
        self.base_url = base_url

    async def upload_file(self, file_path, secret=False, expires=None):
        data = aiohttp.FormData()
        data.add_field("file", open(file_path, "rb"), filename=file_path)

        if secret:
            data.add_field("secret", "")
        if expires:
            data.add_field("expires", str(expires))

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, data=data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(
                        "Yükleme başarısız oldu!\n"
                        f"Durum kodu: {response.status}"
                    )

    async def shorten_url(self, url):
        data = {"shorten": url}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, data=data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(
                        "URL kısaltma başarısız oldu!"
                        f"Durum kodu: {response.status}"
                    )

    async def upload_url(self, url, secret=False, expires=None):
        data = {"url": url}
        if secret:
            data["secret"] = ""
        if expires:
            data["expires"] = str(expires)

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, data=data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(
                        "URL yükleme başarısız oldu!"
                        f"Durum kodu: {response.status}"
                    )


"""
# Örnek kullanım
async def main():
    uploader = AsyncFileUploader()

    # Dosya yükleme örneği
    try:
        file_url = await uploader.upload_file(
        "dosya.png", secret=True, expires=86400
    )
        print("Yüklenen dosya URL'si:", file_url)
    except Exception as e:
        print(e)

    # URL kısaltma örneği
    try:
        short_url = await uploader.shorten_url(
        "https://example.com/long/url"
    )
        print("Kısa URL:", short_url)
    except Exception as e:
        print(e)

    # Uzaktan URL yükleme örneği
    try:
        uploaded_url = await uploader.upload_url(
        "https://example.com/image.jpg",
        secret=True, expires=3600
    )
        print(
        "Yüklenen uzaktan dosya URL'si:", uploaded_url
    )
    except Exception as e:
        print(e)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
"""
