Olympic Data Analysis – Exploratory Data Analysis (EDA)

Bu çalışma, Kaggle’daki 120 Years of Olympic History veri seti üzerinde kapsamlı bir Exploratory Data Analysis (EDA) çalışmasıdır. Amaç, yıllar içinde olimpiyat sporcularının özelliklerini, demografik yapısını, madalya dağılımlarını ve trendlerini analiz etmek ve eksik/bozuk verileri temizleyerek veri setini makine öğrenimine hazır hâle getirmektir.

Hedefler

* Bu çalışmada aşağıdaki sorulara yanıt aranmıştır:
* Sporcuların Age, Height, Weight dağılımları nasıldır?
* Bu değişkenler Sport, Sex, Season gibi kategorik değişkenlere göre nasıl değişir?
* Veri setinde eksik değerler nerelerde yoğunlaşmıştır?
* Eksik değerleri doldurmak için hangi yöntem istatistiksel olarak en doğrusudur?
* Sıradışı (anormal) gözlemler hangileridir ve hangi spor dallarında daha sık görülür?
* Yıllara göre madalya dağılımı nasıl değişmiştir?
* Fiziksel özellikler olimpik sporlar arasında nasıl farklılaşmaktadır?

Kullanılan Yöntemler 

1. Veri Ön İşleme

* Eksik değer analizi
* Kategorik değişkenlerin incelenmesi
* Veri türü dönüşümleri
* Duplicate kayıt kontrolü
2. Eksik Değer Doldurma 

* Bu projede iki aşamalı bir yaklaşım kullanılmaktadır:
* Spor + cinsiyete göre ortalama doldurma
* Kalıcı eksikler için KNN Imputer
* Event, Sport, Sex, Age gibi özellikler kullanılarak benzer sporcular baz alınır
* Bu yöntem çok değişkenli yapıyı korur ve daha gerçekçi değerler üretir

3. Anomali Tespiti 

* IQR yöntemi 
* Çoklu değişkende uç olan sporcuları tespit eden özel fonksiyon
* Spor bazında fiziksel profil analizleri

4. Veri Görselleştirme

* Histogramlar
* Boxplot’lar
* Groupby görselleştirmeleri
* Sport-Year pivot tabloları
* Trend analizleri

5. Madalya Analizi

* Yıllara göre toplam madalyalar
* Yaz/Kış Olimpiyat farkları
* Spor branşına göre madalya eğilimleri

Çıkarımlar

* Fiziksel özellikler (boy/kilo) spor türüne göre çok güçlü farklılıklar gösteriyor.
* Height & Weight değişkenleri 1900–1950 arası yoğun eksik, son yıllarda daha düzenli.
* Spor türüne göre KNN imputasyonu, tek değişkenli ortalama doldurmadan çok daha doğru.
* Gymnastics sporcuları en düşük Height/Weight ortalamalarına sahip, Basketball ve Volleyball en yüksek.
* Anomali tespiti özellikle 1900’lerin ikinci yarısındaki ölçüm hatalarını ortaya çıkarıyor.
* Yıllar ilerledikçe sporcuların ortalama boy ve ağırlıkları yükselme trendi gösteriyor.
