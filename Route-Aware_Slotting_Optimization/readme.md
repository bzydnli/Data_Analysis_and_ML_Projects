Route-Aware Slotting Optimization (Genetic Algorithm)

Bu proje, depo operasyonlarında karşılaşılan slotting (raf yerleşimi) problemini ele alır ve Genetik Algoritma (GA) tabanlı bir optimizasyon yaklaşımı sunar. Amaç, yalnızca depo içi yerleşimi iyileştirmek değil; yerleşim kararlarının rota (routing) performansı üzerindeki etkisini de açık biçimde ortaya koymaktır.

Projede Ne Yapılıyor?

* Depo içindeki ürünler için optimize edilmiş bir raf yerleşimi oluşturuluyor

* Genetik Algoritma kullanılarak rota ve zone geçişlerini dikkate alan bir maliyet fonksiyonu optimize ediliyor

* Yerleşim ve rota kararlarının ayrı ayrı ve birlikte operasyonel maliyete etkisi karşılaştırılıyor

Neden Önemli?

Çoğu slotting çalışması yalnızca: ürün popülerliği,talep sıklığı,mesafe gibi faktörlere odaklanır.

Bu projede ise: zone geçişleri, rota davranışı, yerleşim–rota entegrasyonu birlikte ele alınmaktadır. Bu yaklaşım, gerçek depo operasyonlarında karşılaşılan karmaşıklığı daha iyi yansıtır.

Kullanılan Yaklaşım
🔹 Genetik Algoritma

Her kromozom bir ürün–raf yerleşimini temsil eder

Amaç fonksiyonu; mesafe maliyeti, zone içi dağılım, zone geçiş cezası bileşenlerinden oluşur

Çaprazlama ve mutasyon ile keşif–yoğunlaşma dengesi sağlanır

🔹 Routing Stratejileri

Projede üç farklı senaryo karşılaştırılmıştır:

Human-like Baseline
Zone sıralı, ancak zone içi rastgele yürüyüş (gerçekçi ama verimsiz)

GA Slotting + Basit Rota
Depo optimize, ancak rota farkındalığı yok

GA Slotting + Zone-Aware Routing (Önerilen)
Yerleşim ve rota kararlarının entegre edildiği yapı

Öne Çıkan Sonuçlar

* GA tabanlı yerleşim, baseline çözüme kıyasla ölçülebilir iyileşme sağlamaktadır

* En büyük operasyonel kazanç, yerleşim ve rota kararlarının birlikte optimize edilmesiyle elde edilmiştir

* Mutasyon oranı ve zone ceza ağırlığı için yapılan duyarlılık analizleri, yöntemin kararlı ve sağlam davrandığını göstermektedir

Yapılan Analizler

* Baseline vs GA karşılaştırması

* Rota davranışı görsel analizi

* Mutation rate duyarlılık analizi

* Zone transition weight duyarlılık analizi



Kullanılan Teknolojiler

* Python

* NumPy, Pandas

* Matplotlib

* Sezgisel optimizasyon (Genetic Algorithm)

Kimler İçin?

* Optimizasyon ve sezgisel algoritmalarla ilgilenenler

* Depo / lojistik problemleri üzerine çalışanlar

* ML & OR (Operations Research) portfolyosu oluşturmak isteyenler

* Yüksek lisans / araştırma projeleri için örnek arayanlar

Geliştirme Fikirleri

* Çok amaçlı optimizasyon (multi-objective GA)

* Gerçek zamanlı sipariş akışı senaryoları

* Öğrenmeye dayalı rota stratejileri (RL)

* Gerçek depo verileri ile saha testi

Not:
Bu proje, akademik bir çalışma mantığıyla geliştirilmiş olup portfolyo amaçlı olarak paylaşılmaktadır. Kod ve deney yapısı, genişletilmeye ve farklı senaryolara uyarlanmaya uygundur.
