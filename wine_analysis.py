# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Veri setini okuyoruz
df = pd.read_csv('winemag-data-130k-v2.csv')

# 1. Yıldız derecelerini hesaplayan fonksiyon
def calculate_star_ratings(df):
    # Koşulları tanımlıyoruz
    conditions = [
        (df['country'] == 'Canada'),         # Kanada şarapları otomatik 3 yıldız alır
        (df['points'] >= 95),                # 95 ve üstü puan = 3 yıldız
        (df['points'].between(85, 94)),      # 85-94 arası puan = 2 yıldız
        (df['points'] < 85)                  # 85’ten düşük puan = 1 yıldız
    ]
    choices = [3, 3, 2, 1]  # Her koşula karşılık gelen yıldız sayıları
    return pd.Series(np.select(conditions, choices, default=1))

# Yıldız derecelerini veri setine ekliyoruz
df['star_ratings'] = calculate_star_ratings(df)

# 2. Analiz: Ülkelere göre ortalama puanlar (ilk 10)
country_avg_points = df.groupby('country')['points'].mean().sort_values(ascending=False).head(10)
print("10 Countries with the Highest Average Score:")
print(country_avg_points)

# 3. Görselleştirme: Yıldız derecelerinin dağılımı
plt.figure(figsize=(8, 6))  # Grafik boyutunu ayarlıyoruz
df['star_ratings'].value_counts().sort_index().plot(kind='bar', color='orange')  # Çubuk grafik çiziyoruz
plt.title('Yıldız Derecelerinin Dağılımı')  # Başlık
plt.xlabel('Yıldız Sayısı')  # X ekseni etiketi
plt.ylabel('İnceleme Sayısı')  # Y ekseni etiketi
plt.xticks(rotation=0)  # X ekseni yazılarını düz tutuyoruz
plt.savefig('star_distribution.png')  # Grafiği dosya olarak kaydediyoruz
plt.show()  # Grafiği ekranda gösteriyoruz

# 4. Kanada şaraplarını kontrol etme
canada_wines = df[df['country'] == 'Canada'][['points', 'star_ratings']]
print("\nKanada Şarapları (İlk 5 Satır):")
print(canada_wines.head())

# 5. Veri setinin temel istatistikleri
print("\nVeri Seti Özeti:")
print(df[['points', 'star_ratings']].describe())