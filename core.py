<<<<<<< HEAD
import json
from pathlib import Path
import difflib

# Lokasi file FAQ
BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faq_toko.json"

# Load data FAQ saat aplikasi dijalankan
with FAQ_FILE.open("r", encoding="utf-8") as f:
    FAQS = json.load(f)

def get_bot_reply(user_message: str) -> str:
    """
    Fungsi utama untuk menjawab pertanyaan.
    Dipakai bersama oleh web dan Telegram.
    """
    text = (user_message or "").lower()

    # 1. Cek kecocokan dengan daftar FAQ berdasarkan keyword
    for faq in FAQS:
        for kw in faq["keywords"]:
            if kw in text:
                return faq["answer"]

    # 2. Respon sapaan umum
    sapaan = ["hallo", "hai", "assalamualaikum", "assalamu'alaikum", "pagi", "siang", "sore", "malam"]
    if any(s in text for s in sapaan):
        return (
            "Hallo, selamat datang di cookiesbite 👋\n"
            "Silakan tanya seputar jam operasional, alamat, cara order, atau produk kami."
        )

    # 3. Jawaban default kalau tidak ditemukan
        return (
        "Maaf, saya belum memahami pertanyaan tersebut.\n"
        "Silahkan tanyakan tentang :\n"
         "- Harga kue\n"
         "- Jenis kue\n"
         "- Jam buka toko\n"
         "atau hubungi WhatsApp 081327337031 ya 😊"
        "Mohon gunakan bahasan yang sopan!!!"
        )
    # 4. MUNGKIN MAKSUD ANDA (Suggestion)
    semua_keyword = []
    for faq in FAQS:
        semua_keyword.extend(faq["keywords"])

    rekomendasi = difflib.get_close_matches(
        text,
        semua_keyword,
        n=3,
        cutoff=0.4
    )

    if rekomendasi:
        hasil = "Mungkin maksud anda:\n"
        for r in set(rekomendasi):
            hasil += f"- {r}\n"
        return hasil.strip()    
    
    
    
=======
import json
from pathlib import Path
import difflib

# Lokasi file FAQ
BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faq_toko.json"

# Load data FAQ saat aplikasi dijalankan
with FAQ_FILE.open("r", encoding="utf-8") as f:
    FAQS = json.load(f)

def get_bot_reply(user_message: str) -> str:
    """
    Fungsi utama untuk menjawab pertanyaan.
    Dipakai bersama oleh web dan Telegram.
    """
    text = (user_message or "").lower()

    # 1. Cek kecocokan dengan daftar FAQ berdasarkan keyword
    for faq in FAQS:
        for kw in faq["keywords"]:
            if kw in text:
                return faq["answer"]

    # 2. Respon sapaan umum
    sapaan = ["hallo", "hai", "assalamualaikum", "assalamu'alaikum", "pagi", "siang", "sore", "malam"]
    if any(s in text for s in sapaan):
        return (
            "Hallo, selamat datang di cookiesbite 👋\n"
            "Silakan tanya seputar jam operasional, alamat, cara order, atau produk kami."
        )

    # 3. Jawaban default kalau tidak ditemukan
        return (
        "Maaf, saya belum memahami pertanyaan tersebut.\n"
        "Silahkan tanyakan tentang :\n"
         "- Harga kue\n"
         "- Jenis kue\n"
         "- Jam buka toko\n"
         "atau hubungi WhatsApp 081327337031 ya 😊"
        "Mohon gunakan bahasan yang sopan!!!"
        )
    # 4. MUNGKIN MAKSUD ANDA (Suggestion)
    semua_keyword = []
    for faq in FAQS:
        semua_keyword.extend(faq["keywords"])

    rekomendasi = difflib.get_close_matches(
        text,
        semua_keyword,
        n=3,
        cutoff=0.4
    )

    if rekomendasi:
        hasil = "Mungkin maksud anda:\n"
        for r in set(rekomendasi):
            hasil += f"- {r}\n"
        return hasil.strip()    
    
    
    
>>>>>>> 6c8ca8f925dab4d0b71a2231642f1c52e6b4a255
