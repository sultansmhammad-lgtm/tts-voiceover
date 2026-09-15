import streamlit as st

st.set_page_config(page_title="Free TTS", layout="centered")
st.title("🎙️ Free TTS Voiceover")

text = st.text_area("Text likho:", height=200)

if st.button("Generate Audio"):
    if text.strip():
        # Using Google's free TTS API
        from gtts import gTTS
        import io
        
        tts = gTTS(text=text, lang='en', slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        
        st.audio(audio_fp, format="audio/mp3")
        st.download_button("⬇️ Download", audio_fp, "voiceover.mp3", "audio/mp3")
    else:
        st.warning("Text likho!")
