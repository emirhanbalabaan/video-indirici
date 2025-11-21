import streamlit as st
import yt_dlp
import time

# --- 1. SEO & SAYFA AYARLARI (GLOBAL KEYWORDS) ---
st.set_page_config(
    page_title="Video Downloader - TikTok, Instagram, YouTube (No Watermark)",
    page_icon="⬇️",
    layout="centered",
    menu_items={
        'Get Help': 'https://www.google.com',
        'About': "Best Free Video Downloader / En İyi Video İndirici"
    }
)

# --- 2. BAŞLIK (HOOK) ---
st.title("⬇️ Reklamsız Video İndirici")
st.header("Download Videos from YouTube, Instagram, TikTok & X")
st.markdown("""
**%100 Ücretsiz, Programsız ve Reklamsız.**
*Free, Fast, No Ads & No Watermark.*
""")

# --- 3. GİRİŞ KUTUSU ---
url = st.text_input("Link:", placeholder="https://www.instagram.com/reel/...")

# --- 4. İNDİRME MOTORU ---
def get_video_info(video_url):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info
    except Exception as e:
        return None

# --- 5. İŞLEM VE SONUÇ ---
if st.button("Videoyu Bul / Find Video 🚀", type="primary"):
    if url:
        with st.spinner("Processing... / İşleniyor..."):
            info = get_video_info(url)
            
            if info:
                # Bilgileri Çek
                title = info.get('title', 'Video')
                thumb = info.get('thumbnail', None)
                direct_url = info.get('url', None)
                platform = info.get('extractor_key', 'Unknown')
                
                # Başarı Mesajı
                st.success("✅ Video Hazır! / Ready!")
                
                # Kapak Resmi
                if thumb:
                    st.image(thumb, use_container_width=True)
                
                st.write(f"**Title:** {title}")
                st.caption(f"Source: {platform} | Quality: HD")
                
                st.divider()
                
                # --- GARANTİLİ İNDİRME BUTONU (HATA VERMEZ) ---
                if direct_url:
                    st.link_button("📥 İNDİR / DOWNLOAD (MP4)", direct_url, type="primary")
                    
                    st.info("""
                    💡 **İpucu / Tip:** Butona basınca video açılırsa, videonun üzerine **Sağ Tıkla > Farklı Kaydet** yapın.
                    *If video opens in new tab, Right Click > Save As.*
                    """)
                
            else:
                st.error("Video not found. / Video bulunamadı. (Linkin herkese açık olduğundan emin olun).")
    else:
        st.warning("Please paste a link. / Lütfen link yapıştırın.")

# --- 6. SEO BÖLÜMÜ (TRAFİK İÇİN KRİTİK) ---
st.markdown("---")

with st.expander("🌍 Sıkça Sorulan Sorular & FAQ (SEO)", expanded=True):
    st.markdown("""
    ### 🇹🇷 Nasıl İndirilir?
    1. Videonun bağlantısını kopyalayın.
    2. Kutucuğa yapıştırın ve butona basın.
    3. **"İndir"** butonuna tıklayın.
    
    **Özellikler:**
    * **Instagram Reels İndir:** Kalite kaybı olmadan indirin.
    * **TikTok Logosuz:** Filigran olmadan temiz video.
    * **YouTube MP4:** Videoları telefonunuza kaydedin.
    
    ---
    
    ### 🇬🇧 How to Download?
    1. **Copy the link** of the video.
    2. Paste it above and click "Find".
    3. Click the **Download** button.
    
    **Why use this tool?**
    * **TikTok Downloader No Watermark:** Save TikToks without the logo.
    * **Instagram Saver:** Download Reels, Stories and Posts.
    * **YouTube to MP4:** Fast and free converter.
    * **Twitter Video Downloader:** Save videos from X.
    
    *Keywords: online video downloader, free video saver, tiktok no watermark, instagram reels download, youtube mp4 converter, twitter video save, hd video downloader, mobil video indir, ücretsiz video indir.*
    """)

st.caption("© 2025 Universal Downloader. Personal use only.")