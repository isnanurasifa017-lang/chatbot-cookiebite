<<<<<<< HEAD
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    ContextTypes, 
    filters
)

TOKEN = "8414704529:AAE_c60w2yQ7fprPQS4fdjjcPwUFkAVgTFE"

async def reply_text(update, context):
    text = update.message.text.lower()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋 Saya chatbot Cookiebite!\n"
        "Silakan tanya seputar jam operasional, alamat, pricelist, cara order, atau produk kami."
    )

async def produk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍪 Produk Cookiebite:\n"
        "- Chocolate Cookies\n"
        "- Butter Cookies\n"
        "- Almond Cookies"
    )
async def pricelist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Pricelist:\n"
        "- Chocolate Cookies : Rp15.000\n"
        "- Butter Cookies     : Rp12.000\n"
        "- Almond Cookies     : Rp18.000"
    )
async def alamat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Alamat Cookiebite: Tegal Selatan, Kota Tegal, Jawa Tengah"
    )
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cara order di Cookiebite:\n"
        "Gofood\n"
        "Shopeefood\n" 
        "WhatsApp: 081327337031\n" 
        "Datang langsung ke alamat kami di Tegal Selatan, Kota Tegal."
    )
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    

    
    if text == "cara order":
        context.user_data.clear()
        context.user_data["step"] = "produk"
        await update.message.reply_text(
            "🛒 Pilih produk:\n"
            "1. Chocolate Cookies\n"
            "2. Cheese Cookies\n\n"
            "Ketik nama produk"
        )

    # PILIH PRODUK
    elif context.user_data.get("step") == "produk":
        context.user_data["produk"] = text
        context.user_data["step"] = "jumlah"
        await update.message.reply_text("📦 Masukkan jumlah pesanan")

    
    elif context.user_data.get("step") == "jumlah":
        if not text.isdigit():
            await update.message.reply_text("⚠️ Jumlah harus angka")
            return
        context.user_data["jumlah"] = int(text)
        context.user_data["step"] = "alamat"
        await update.message.reply_text("📍 Masukkan alamat lengkap")

    # ALAMAT
    elif context.user_data.get("step") == "alamat":
        context.user_data["alamat"] = text

        await update.message.reply_text(
            f"✅ Pesanan diterima!\n\n"
            f"🍪 Produk: {context.user_data['produk']}\n"
            f"📦 Jumlah: {context.user_data['jumlah']}\n"
            f"📍 Alamat: {context.user_data['alamat']}\n\n"
            "Terima kasih sudah order di Cookiebite 🤎",
            parse_mode="Markdown"
        )

        context.user_data.clear()
        
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "produk" in text:
        await update.message.reply_text(
            "🍪 Produk Cookiebite:\n"
            "- Chocolate Cookies\n"
            "- Butter Cookies\n"
            "- Almond Cookies"
        )

    elif "harga" in text or "pricelist" in text:
        await update.message.reply_text(
            "💰 Pricelist Cookiebite:\n"
            "- Chocolate Cookies : Rp15.000\n"
            "- Butter Cookies    : Rp12.000\n"
            "- Almond Cookies    : Rp18.000\n"
            "- Cheese Cookies    : RP15000\n"
            "-Matcha Cookies     : RP12000"
        )

    elif "alamat" in text:
        await update.message.reply_text(
            "📍 Alamat Cookiebite:\n"
            "Tegal Selatan, Kota Tegal, Jawa Tengah"
        )

    elif "jam" in text or "operasional" in text:
        await update.message.reply_text(
            "⏰ Jam Operasional Cookiebite:\n"
            "Setiap hari 08.00 – 21.00 WIB"
        )
    
    
    if text == "cara order":
        context.user_data.clear()
        context.user_data["step"] = "produk"
        await update.message.reply_text(
            "🛒 Pilih produk:\n"
            "1. Chocolate Cookies\n"
            "2. Cheese Cookies\n"
            "3. Butter Cookies\n"
            "4. Almond Cookies\n"
            "5. Matcha Cookies\n\n"
            "Ketik nama produk"
        )

    # PILIH PRODUK
    elif context.user_data.get("step") == "produk":
        context.user_data["produk"] = text
        context.user_data["step"] = "jumlah"
        await update.message.reply_text("📦 Masukkan jumlah pesanan")

    
    elif context.user_data.get("step") == "jumlah":
        if not text.isdigit():
            await update.message.reply_text("⚠️ Jumlah harus angka")
            return
        context.user_data["jumlah"] = int(text)
        context.user_data["step"] = "nomor"
        await update.message.reply_text("Masukan No.HP/WhatsApp")


    elif context.user_data.get("step") == "nomor":
        context.user_data["nomor"] = int (text)
        context.user_data["step"] = "alamat"
        await update.message.reply_text("📍 Masukkan alamat lengkap")

    # ALAMAT
    elif context.user_data.get("step") == "alamat":
        context.user_data["alamat"] = text
    
        await update.message.reply_text(
            f"✅ Pesanan diterima!\n\n"
            f"🍪 Produk: {context.user_data['produk']}\n"
            f"📦 Jumlah: {context.user_data['jumlah']}\n"
            f"📍 Alamat: {context.user_data['alamat']}\n"
            f"📞 No.HP : {context.user_data['nomor']}\n"
            "Untuk pengiriman akan kami informasikan lewat WhatsApp\n"
            "Terima kasih sudah order di Cookiebite 🤎",
            parse_mode="Markdown"
        )

        context.user_data.clear()
   

    

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("produk", produk))
    app.add_handler(CommandHandler("pricelist", pricelist))
    app.add_handler(CommandHandler("alamat", alamat))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))

    print("Bot Cookiebite berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
=======
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    ContextTypes, 
    filters
)

TOKEN = "8414704529:AAE_c60w2yQ7fprPQS4fdjjcPwUFkAVgTFE"

async def reply_text(update, context):
    text = update.message.text.lower()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋 Saya chatbot Cookiebite!\n"
        "Silakan tanya seputar jam operasional, alamat, pricelist, cara order, atau produk kami."
    )

async def produk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍪 Produk Cookiebite:\n"
        "- Chocolate Cookies\n"
        "- Butter Cookies\n"
        "- Almond Cookies"
    )
async def pricelist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Pricelist:\n"
        "- Chocolate Cookies : Rp15.000\n"
        "- Butter Cookies     : Rp12.000\n"
        "- Almond Cookies     : Rp18.000"
    )
async def alamat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Alamat Cookiebite: Tegal Selatan, Kota Tegal, Jawa Tengah"
    )
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cara order di Cookiebite:\n"
        "Gofood\n"
        "Shopeefood\n" 
        "WhatsApp: 081327337031\n" 
        "Datang langsung ke alamat kami di Tegal Selatan, Kota Tegal."
    )
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    

    
    if text == "cara order":
        context.user_data.clear()
        context.user_data["step"] = "produk"
        await update.message.reply_text(
            "🛒 Pilih produk:\n"
            "1. Chocolate Cookies\n"
            "2. Cheese Cookies\n\n"
            "Ketik nama produk"
        )

    # PILIH PRODUK
    elif context.user_data.get("step") == "produk":
        context.user_data["produk"] = text
        context.user_data["step"] = "jumlah"
        await update.message.reply_text("📦 Masukkan jumlah pesanan")

    
    elif context.user_data.get("step") == "jumlah":
        if not text.isdigit():
            await update.message.reply_text("⚠️ Jumlah harus angka")
            return
        context.user_data["jumlah"] = int(text)
        context.user_data["step"] = "alamat"
        await update.message.reply_text("📍 Masukkan alamat lengkap")

    # ALAMAT
    elif context.user_data.get("step") == "alamat":
        context.user_data["alamat"] = text

        await update.message.reply_text(
            f"✅ Pesanan diterima!\n\n"
            f"🍪 Produk: {context.user_data['produk']}\n"
            f"📦 Jumlah: {context.user_data['jumlah']}\n"
            f"📍 Alamat: {context.user_data['alamat']}\n\n"
            "Terima kasih sudah order di Cookiebite 🤎",
            parse_mode="Markdown"
        )

        context.user_data.clear()
        
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "produk" in text:
        await update.message.reply_text(
            "🍪 Produk Cookiebite:\n"
            "- Chocolate Cookies\n"
            "- Butter Cookies\n"
            "- Almond Cookies"
        )

    elif "harga" in text or "pricelist" in text:
        await update.message.reply_text(
            "💰 Pricelist Cookiebite:\n"
            "- Chocolate Cookies : Rp15.000\n"
            "- Butter Cookies    : Rp12.000\n"
            "- Almond Cookies    : Rp18.000\n"
            "- Cheese Cookies    : RP15000\n"
            "-Matcha Cookies     : RP12000"
        )

    elif "alamat" in text:
        await update.message.reply_text(
            "📍 Alamat Cookiebite:\n"
            "Tegal Selatan, Kota Tegal, Jawa Tengah"
        )

    elif "jam" in text or "operasional" in text:
        await update.message.reply_text(
            "⏰ Jam Operasional Cookiebite:\n"
            "Setiap hari 08.00 – 21.00 WIB"
        )
    
    
    if text == "cara order":
        context.user_data.clear()
        context.user_data["step"] = "produk"
        await update.message.reply_text(
            "🛒 Pilih produk:\n"
            "1. Chocolate Cookies\n"
            "2. Cheese Cookies\n"
            "3. Butter Cookies\n"
            "4. Almond Cookies\n"
            "5. Matcha Cookies\n\n"
            "Ketik nama produk"
        )

    # PILIH PRODUK
    elif context.user_data.get("step") == "produk":
        context.user_data["produk"] = text
        context.user_data["step"] = "jumlah"
        await update.message.reply_text("📦 Masukkan jumlah pesanan")

    
    elif context.user_data.get("step") == "jumlah":
        if not text.isdigit():
            await update.message.reply_text("⚠️ Jumlah harus angka")
            return
        context.user_data["jumlah"] = int(text)
        context.user_data["step"] = "nomor"
        await update.message.reply_text("Masukan No.HP/WhatsApp")


    elif context.user_data.get("step") == "nomor":
        context.user_data["nomor"] = int (text)
        context.user_data["step"] = "alamat"
        await update.message.reply_text("📍 Masukkan alamat lengkap")

    # ALAMAT
    elif context.user_data.get("step") == "alamat":
        context.user_data["alamat"] = text
    
        await update.message.reply_text(
            f"✅ Pesanan diterima!\n\n"
            f"🍪 Produk: {context.user_data['produk']}\n"
            f"📦 Jumlah: {context.user_data['jumlah']}\n"
            f"📍 Alamat: {context.user_data['alamat']}\n"
            f"📞 No.HP : {context.user_data['nomor']}\n"
            "Untuk pengiriman akan kami informasikan lewat WhatsApp\n"
            "Terima kasih sudah order di Cookiebite 🤎",
            parse_mode="Markdown"
        )

        context.user_data.clear()
   

    

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("produk", produk))
    app.add_handler(CommandHandler("pricelist", pricelist))
    app.add_handler(CommandHandler("alamat", alamat))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))

    print("Bot Cookiebite berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
>>>>>>> 6c8ca8f925dab4d0b71a2231642f1c52e6b4a255
