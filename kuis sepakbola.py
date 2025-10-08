import streamlit as st
import random

# Judul Aplikasi
st.title("🏆 Game Teka-Teki Sepak Bola")
st.write("Jawablah 20 soal berikut! Setiap jawaban benar bernilai +5 skor.")

# Inisialisasi session_state untuk skor dan indeks
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.skor = 0
    st.session_state.finished = False
    st.session_state.pertanyaan = random.sample([
        {
            "soal": "Siapa pemain yang dijuluki 'La Pulga'?",
            "pilihan": ["A. Cristiano Ronaldo", "B. Lionel Messi", "C. Neymar", "D. Kylian Mbappe"],
            "jawaban": "B"
        },
        {
            "soal": "Negara mana yang pertama kali menjadi juara Piala Dunia (1930)?",
            "pilihan": ["A. Brasil", "B. Argentina", "C. Uruguay", "D. Italia"],
            "jawaban": "C"
        },
        {
            "soal": "Berapa jumlah pemain inti dalam satu tim sepak bola?",
            "pilihan": ["A. 9", "B. 10", "C. 11", "D. 12"],
            "jawaban": "C"
        },
        {
            "soal": "Siapa kiper legendaris Italia yang terkenal dengan julukan 'Superman'?",
            "pilihan": ["A. Buffon", "B. Casillas", "C. Cech", "D. Neuer"],
            "jawaban": "A"
        },
        {
            "soal": "Negara manakah yang memenangkan Piala Dunia 2014?",
            "pilihan": ["A. Brasil", "B. Jerman", "C. Spanyol", "D. Argentina"],
            "jawaban": "B"
        },
        {
            "soal": "Siapa pencetak gol terbanyak sepanjang masa Piala Dunia?",
            "pilihan": ["A. Miroslav Klose", "B. Ronaldo Nazario", "C. Pele", "D. Messi"],
            "jawaban": "A"
        },
        {
            "soal": "Klub manakah yang dijuluki 'The Red Devils'?",
            "pilihan": ["A. Liverpool", "B. AC Milan", "C. Manchester United", "D. Arsenal"],
            "jawaban": "C"
        },
        {
            "soal": "Di negara mana klub Barcelona berada?",
            "pilihan": ["A. Italia", "B. Spanyol", "C. Portugal", "D. Prancis"],
            "jawaban": "B"
        },
        {
            "soal": "Apa nama stadion utama Real Madrid?",
            "pilihan": ["A. Camp Nou", "B. Old Trafford", "C. Santiago Bernabeu", "D. San Siro"],
            "jawaban": "C"
        },
        {
            "soal": "Siapa pemain Brasil yang dijuluki 'O Rei' (Sang Raja)?",
            "pilihan": ["A. Ronaldinho", "B. Pele", "C. Romario", "D. Rivaldo"],
            "jawaban": "B"
        },
        {
            "soal": "Siapa pemain dengan julukan 'CR7'?",
            "pilihan": ["A. Cristiano Ronaldo", "B. Carlos Tevez", "C. Luka Modric", "D. Gareth Bale"],
            "jawaban": "A"
        },
        {
            "soal": "Apa warna jersey utama timnas Jerman?",
            "pilihan": ["A. Putih", "B. Biru", "C. Hitam", "D. Merah"],
            "jawaban": "A"
        },
        {
            "soal": "Berapa menit normal permainan sepak bola?",
            "pilihan": ["A. 60 menit", "B. 80 menit", "C. 90 menit", "D. 100 menit"],
            "jawaban": "C"
        },
        {
            "soal": "Siapa yang mendapat Ballon d'Or terbanyak?",
            "pilihan": ["A. Messi", "B. Ronaldo", "C. Zidane", "D. Modric"],
            "jawaban": "A"
        },
        {
            "soal": "Negara mana yang menjadi tuan rumah Piala Dunia 2022?",
            "pilihan": ["A. Rusia", "B. Qatar", "C. Amerika Serikat", "D. Jepang"],
            "jawaban": "B"
        },
        {
            "soal": "Klub mana yang memiliki julukan 'The Blues'?",
            "pilihan": ["A. Chelsea", "B. Manchester City", "C. Everton", "D. Napoli"],
            "jawaban": "A"
        },
        {
            "soal": "Apa nama kompetisi antarklub paling bergengsi di Eropa?",
            "pilihan": ["A. Europa League", "B. Liga Champions", "C. Piala Super", "D. Nations League"],
            "jawaban": "B"
        },
        {
            "soal": "Siapa pelatih yang dijuluki 'The Special One'?",
            "pilihan": ["A. Guardiola", "B. Klopp", "C. Mourinho", "D. Ancelotti"],
            "jawaban": "C"
        },
        {
            "soal": "Negara manakah yang memenangkan Piala Dunia 1998?",
            "pilihan": ["A. Brasil", "B. Prancis", "C. Jerman", "D. Argentina"],
            "jawaban": "B"
        },
        {
            "soal": "Klub mana yang pernah memiliki trio MSN (Messi, Suarez, Neymar)?",
            "pilihan": ["A. Real Madrid", "B. PSG", "C. Barcelona", "D. Juventus"],
            "jawaban": "C"
        }
    ], k=20)

# Menampilkan soal jika belum selesai
if not st.session_state.finished:
    current = st.session_state.pertanyaan[st.session_state.index]
    st.subheader(f"Soal {st.session_state.index + 1}")
    st.write(current["soal"])

    # Opsi jawaban
    pilihan = st.radio("Pilih jawaban kamu:", current["pilihan"], key=f"radio_{st.session_state.index}")

    if st.button("Kirim Jawaban"):
        jawaban_user = pilihan.split(".")[0]  # Ambil huruf A/B/C/D

        if jawaban_user == current["jawaban"]:
            st.success("✔ Benar! +5 skor")
            st.session_state.skor += 5
        else:
            st.error(f"✘ Salah! Jawaban benar adalah {current['jawaban']}")

        # Lanjut ke soal berikutnya
        if st.session_state.index < 19:
            st.session_state.index += 1
        else:
            st.session_state.finished = True

# Tampilkan hasil akhir
if st.session_state.finished:
    st.markdown("## 🎉 HASIL AKHIR")
    st.write(f"Skor akhir kamu adalah **{st.session_state.skor}** dari **100**")
    if st.button("Main Lagi"):
        for key in st.session_state.keys():
            del st.session_state[key]
