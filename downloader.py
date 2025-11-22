import streamlit as st
import yt_dlp
import os
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Video İndirici - Garantili",
    page_icon="⬇️",
    layout="centered"
)

# --- BAŞLIK ---
st.title("⬇️ Garantili Video İndirici")
st.info("Instagram, TikTok, YouTube videolarını 403 hatası almadan indir.")

# --- GİRİŞ ---
url = st.text_input("Video Linki:", placeholder="https://www.instagram.com/reel/...")

# --- İNDİRME VE İŞLEME FONKSİYONU ---
def download_video_server_side(video_url):
    """Videoyu sunucuya indirir ve dosya yolunu döndürür."""
    
    # Geçici dosya adı (karışıklık olmasın diye zaman damgası ekliyoruz)
    filename = f"video_{int(time.time())}.mp4"
    
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # En iyi MP4
        'outtmpl': filename,             # Dosya adı
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True) # Download=True yaptık!
            video_title = info.get('title', 'video')
            return filename, video_title
    except Exception as e:
        return None, str(e)

# --- BUTON VE İŞLEM ---
if st.button("Videoyu Hazırla ve İndir 🚀", type="primary"):
    if url:
        progress_text = "Video sunucuya indiriliyor... (Bu işlem videonun boyutuna göre 5-10 saniye sürebilir)"
        my_bar = st.progress(0, text=progress_text)
        
        try:
            # 1. Videoyu Sunucuya İndir
            file_path, title_or_error = download_video_server_side(url)
            my_bar.progress(50, text="Video işleniyor...")
            
            if file_path and os.path.exists(file_path):
                my_bar.progress(100, text="Hazır!")
                time.sleep(0.5)
                my_bar.empty() # Barı gizle
                
                st.success("✅ Video Başarıyla Hazırlandı!")
                st.write(f"**Başlık:** {title_or_error}")
                
                # 2. Dosyayı Okuyup Kullanıcıya Sun (Streamlit Download Button)
                with open(file_path, "rb") as file:
                    btn = st.download_button(
                        label="📥 VİDEOYU CİHAZINA KAYDET (MP4)",
                        data=file,
                        file_name=f"video_indirici_{int(time.time())}.mp4",
                        mime="video/mp4",
                        type="primary"
                    )
                
                # 3. Temizlik (Sunucuyu şişirmemek için dosyayı sil)
                # Not: Dosya buton tıklanıp indirildikten sonra silinmeli ama 
                # Streamlit'te bu anlık olduğu için şimdilik dosyayı sunucuda bırakıyoruz.
                # Streamlit Cloud her yeniden başlatmada temizlenir.
                
            else:
                st.error(f"İndirme başarısız oldu. Hata: {title_or_error}")
        except Exception as e:
            st.error(f"Beklenmedik hata: {e}")
    else:
        st.warning("Lütfen link yapıştırın.")

# --- BİLGİ ---
st.markdown("---")
with st.expander("Neden 'Hazırla' demem gerekiyor?"):
    st.write("""
    Instagram ve YouTube gibi siteler, direkt link paylaşımını engeller (403 Hatası). 
    Bu yüzden sistemimiz videoyu önce kendi güvenli sunucusuna çeker, paketler ve size **garantili** bir dosya olarak sunar.
    Bu yöntem %100 çalışır.
    """)