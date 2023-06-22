meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "DEFO": "Kata Definitely yang berarti Pasti",
            "TTYL": "Singkatan dari Talk to You Later yang memiliki arti Kita bicara lagi nanti ya",
            "ICB": "Singkatan dari I Can't Believe yang memiliki arti Aku Tidak Percaya"
            }
            
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    
    else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("Kata tidak ditemukan")
