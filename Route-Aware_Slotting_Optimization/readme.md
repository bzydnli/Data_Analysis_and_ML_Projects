Route-Aware Slotting Optimization with Genetic Algorithm

Bu proje, depo operasyonlarında karşılaşılan slotting (yerleşim) problemini ele alarak, Genetik Algoritma (GA) tabanlı bir optimizasyon yaklaşımı önermektedir. Çalışmanın temel odağı, yalnızca depo içi yerleşimi iyileştirmek değil; yerleşim kararlarının rota (routing) performansı üzerindeki etkisini de açık biçimde ortaya koymaktır.

Problem Tanımı

Depo operasyonlarında slotting problemi, ürünlerin depo içindeki raf veya lokasyonlara hangi düzenle yerleştirileceğinin belirlenmesini kapsar. Amaç genellikle sipariş toplama (order picking) süreçlerinde toplam operasyonel maliyeti ve süreyi minimize etmektir. Ürün sayısının ve olası yerleşim kombinasyonlarının hızla artması nedeniyle bu problem NP-hard sınıfında yer almaktadır.

Klasik slotting yaklaşımları çoğunlukla ürünlerin talep sıklığına veya basit mesafe ölçütlerine dayanır. Ancak bu yöntemler, sipariş toplama rotalarının yapısını ve zone (bölge) geçişlerini doğrudan dikkate almaz. Gerçek hayatta, özellikle çok zoneli depolarda, bir siparişin farklı zonelara yayılması operasyonel maliyeti ciddi biçimde artırmaktadır.

Bu çalışmada, rota duyarlı (route-aware) bir slotting yaklaşımı ele alınmış; toplam toplama mesafesi ile zone geçişleri arasında dengeli bir optimizasyon hedeflenmiştir.

Amaç

Bu projenin temel amaçları şunlardır:

Sipariş toplama rotalarına bağlı toplam maliyeti minimize etmek

Aşırı zone geçişlerini ceza terimleri aracılığıyla sınırlandırmak

Yerleşim (slotting) ve rota (routing) kararlarının birlikte ele alınmasının operasyonel etkisini göstermek

Yöntem
Genetik Algoritma (GA)

Slotting problemi, geniş çözüm uzayı ve kısıt yapısı nedeniyle klasik deterministik yöntemlerle etkin biçimde çözülememektedir. Bu nedenle sezgisel ve olasılıksal bir arama yöntemi olan Genetik Algoritma tercih edilmiştir.

GA kapsamında:

Her kromozom, ürünlerin slotlara atanma düzenini temsil eder

Amaç fonksiyonu;

mesafe bazlı maliyet

zone içi dağılım cezası

ardışık zone geçiş cezası
bileşenlerinden oluşur

Çaprazlama ve mutasyon operatörleri ile keşif–yoğunlaşma dengesi sağlanır

Deney Senaryoları

Çalışmada, yerleşim ve rota kararlarının etkisini ayırt edebilmek amacıyla üç ana senaryo değerlendirilmiştir:

1. Human-like Baseline (Gerçek Operasyonel Davranış)

Personelin zoneları sırayla gezdiği, ancak zone içi ürün sırasının rastgele olduğu sezgisel bir yürüyüş modeli.

2. GA Slotting + Rota Farkındalığı Olmayan Yürüyüş (GA Baseline)

Depo yerleşimi GA ile optimize edilmiştir; ancak rota belirleme aşamasında zone bilgisi dikkate alınmamıştır.

3. GA Slotting + Zone-Aware Greedy Routing (Önerilen Yöntem)

GA ile optimize edilmiş yerleşimin, zone farkındalıklı greedy bir rota stratejisi ile birlikte kullanıldığı senaryo.

Tüm senaryolar aynı rota maliyet fonksiyonu ile değerlendirilmiştir.

Deney Sonuçları

Elde edilen sonuçlar şu bulguları ortaya koymaktadır:

İnsan benzeri sezgisel rota en yüksek maliyeti üretmektedir

GA tabanlı yerleşim, rota farkındalığı olmadan kullanıldığında sınırlı bir iyileşme sağlamaktadır

En düşük operasyonel maliyet, yerleşim ve rota kararlarının entegre edildiği önerilen yaklaşımda elde edilmiştir

Bu durum, depo operasyonlarında yalnızca slotting optimizasyonunun yeterli olmadığını, rota stratejilerinin de kritik rol oynadığını göstermektedir.

Duyarlılık (Sensitivity) Analizleri
Mutation Rate Analizi

Farklı mutasyon oranları için birden fazla bağımsız koşum gerçekleştirilmiş; ortalama maliyet ve standart sapma değerleri incelenmiştir. Orta düzey mutasyon oranlarının, çözüm kalitesi ve kararlılık açısından en dengeli sonuçları verdiği gözlemlenmiştir.

Zone Transition Weight Analizi

Zone geçiş cezasının ağırlığı artırıldıkça çözüm kalitesinin bozulduğu tespit edilmiştir. Orta düzey ceza ağırlıkları arama sürecini yönlendirirken, aşırı yüksek değerler keşfi ciddi biçimde kısıtlamaktadır.

Bu analizler, önerilen yöntemin geniş bir parametre aralığında kararlı davrandığını göstermektedir.

Sonuç

Bu çalışma, GA tabanlı slotting yaklaşımının depo yerleşimini iyileştirdiğini; ancak asıl operasyonel kazanımın, yerleşim kararlarının zone farkındalıklı rota stratejileri ile birlikte ele alınması durumunda elde edildiğini ortaya koymaktadır. Ayrıca yapılan duyarlılık analizleri, yöntemin pratik uygulamalar için sağlam ve güvenilir bir optimizasyon çerçevesi sunduğunu göstermektedir.

Gelecek Çalışmalar

Çok amaçlı (multi-objective) optimizasyon yaklaşımları

Dinamik sipariş akışlarını içeren senaryolar

Öğrenmeye dayalı rota stratejileri (RL entegrasyonu)

Gerçek depo verileri ile saha doğrulaması
