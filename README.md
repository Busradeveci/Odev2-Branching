# Ödev2-Branching - Şarap İncelemeleri Analizi

Bu proje, Yapay Zeka ve Teknoloji Akademisi Git GitHub Ödevi 2 için hazırlanmıştır. Kaggle’dan alınan "Wine Reviews" veri setini kullanarak şarap puanlarını yıldız derecelerine çevirir ve analiz yapar.

## Proje Detayları
- **Veri Seti**: `winemag-data-130k-v2.csv` (Kaggle’dan indirildi, GitHub’a yüklenmedi, `.gitignore` ile hariç tutuldu).
- **Kod**: `wine_analysis.py` - Puanları yıldızlara çevirir, ülkelere göre analiz yapar ve grafik çizer.
- **Grafik**: `star_distribution.png` - Yıldız derecelerinin dağılımını gösterir.

## Branch’ler
- **main**: Orijinal kod, grafik rengi mavi (skyblue).
- **feature-color-change**: Grafik rengi turuncu (orange) olarak değiştirildi.

## Gereksinimler
- Python 3.x
- Kütüphaneler: `pandas`, `numpy`, `matplotlib`

## Nasıl Çalıştırılır?
1. `winemag-data-130k-v2.csv` dosyasını Kaggle’dan indirin: [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)
2. Kütüphaneleri kurun: `pip install pandas numpy matplotlib`
3. Kodu çalıştırın: `python wine_analysis.py`

## Ödev Notu
Bu proje, Git kullanımını göstermek için iki branch ile hazırlanmıştır. Veri seti boyutu nedeniyle GitHub’a yüklenmemiştir.