from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    Source: https://www.turkcebilgi.com/meslekler_listesi
    """

    jobs = [
        "Acentacı",
        "Acil durum yönetmeni",
        "Adli tabip",
        "Agronomist",
        "Ağ yöneticisi",
        "Aşçı",
        "Aşçıbaşı",
        "Ahşap tekne yapımcısı",
        "Aile hekimi",
        "Aktar",
        "Akortçu",
        "Aktör",
        "Aktüer",
        "Aktris",
        "Akustikçi",
        "Albay",
        "Ambalajcı",
        "Ambarcı",
        "Ambulans şoförü",
        "Amiral",
        "Anahtarcı",
        "Anestezi uzmanı",
        "Anestezi teknikeri",
        "Animatör",
        "Antika satıcısı",
        "Antropolog",
        "Apartman yöneticisi",
        "Araba satıcısı",
        "Araba yıkayıcısı",
        "Arabacı",
        "Arabulucu",
        "Araştırmacı",
        "Arıcı",
        "Arkeolog",
        "Armatör",
        "Arpist",
        "Arşivci",
        "Artist",
        "Asansörcü",
        "Asistan",
        "Asker",
        "Astrofizikçi",
        "Astrolog",
        "Astronom",
        "Astronot",
        "Astsubay",
        "Atlet",
        "Av bekçisi",
        "Avcı",
        "Avizeci",
        "Avukat",
        "Ayakçı (otogar, lokanta)",
        "Ayakkabı boyacısı",
        "Ayakkabı tamircisi",
        "Ayakkabıcı",
        "Ayı oynatıcısı",
        "Araba tamircisi",
        "Bacacı",
        "Badanacı",
        "Baharatçı",
        "Bahçe bitkileri uzmanı",
        "Bahçıvan",
        "Bakan",
        "Bakıcı",
        "Bakırcı",
        "Bakkal",
        "Bakteriyolog",
        "Balıkçı",
        "Balerin",
        "Balon pilotu",
        "Bankacı",
        "Banker",
        "Barmen",
        "Barmeyd",
        "Basketbolcu",
        "Başbakan",
        "Başçavuş",
        "Başdümenci",
        "Başhemşire",
        "Başkan",
        "Başkomiser",
        "Başpiskopos",
        "Başrahip",
        "Belediye başkanı",
        "Belediye meclisi üyesi",
        "Benzinci",
        "Berber",
        "Besteci",
        "Biletçi",
        "Bilgisayar mühendisi",
        "Bilgisayar programcısı",
        "Bilgisayar tamircisi",
        "Bilim insanı",
        "Bilirkişi",
        "Binicilik",
        "Biracı",
        "Bisikletçi",
        "Biyografi yazarı",
        "Biyolog",
        "Biyomedikal Mühendisi",
        "Bobinajcı",
        "Bombacı",
        "Bomba imhacı",
        "Borsacı",
        "Borucu",
        "Botanikçi",
        "Boyacı",
        "Bozacı",
        "Böcekbilimci",
        "Börekçi",
        "Bulaşıkçı",
        "Buldozer operatörü",
        "Bütçe uzmanı",
        "Büyükelçi",
        "Besicilik",
        "Bilgi İşlemci",
        "Camcı",
        "Cerrah",
        "Celep",
        "Cellat",
        "Cost Control",
        "Cillopçu",
        "Cumhurbaşkanı",
        "Çamaşırcı",
        "Çantacı",
        "Çarkçı",
        "Çatıcı",
        "Çaycı",
        "Çevirmen",
        "Çevrebilimci",
        "Çevre mühendisi",
        "Çeyizci",
        "Çıkıkçı",
        "Çıkrıkçı",
        "Çiçekçi",
        "Çiftçi",
        "Çiftlik işletici",
        "Çikolatacı",
        "Çilingir",
        "Çinici",
        "Çitçi",
        "Çoban",
        "Çocuk doktoru",
        "Çorapçı",
        "Çöp işçisi",
        "Çöpçü",
        "Çırak",
        "Çevik Kuvvet",
        "Dadı",
        "Daktilograf",
        "Dalgıç",
        "Damıtıcı",
        "Danışman",
        "Dansöz",
        "Davulcu",
        "Debbağ",
        "Dedektif",
        "Değirmen işçisi",
        "Değirmenci",
        "Demirci",
        "Demiryolu işçisi",
        "Denetçi",
        "Denetleyici",
        "Denizci",
        "Depocu",
        "Derici",
        "Desinatör",
        "Devlet memuru",
        "Dilci",
        "Dilenci",
        "Diplomat",
        "Diş hekimi",
        "Diyetisyen",
        "Dizgici",
        "Doğalgazcı",
        "Doğramacı",
        "Doğum uzmanı",
        "Dok işçisi",
        "Dokumacı",
        "Doktor",
        "Dondurmacı",
        "Dökümcü",
        "Döşemeci",
        "Dövizci",
        "Dublajcı",
        "Duvarcı",
        "Dümenci",
        "Diş teknisyeni",
        "Ebe",
        "Eczacı",
        "Eczacı kalfası",
        "Editör",
        "Eğitimci",
        "Eğitmen",
        "Ekonomist",
        "Elektrik mühendisi",
        "Elektronik mühendisi",
        "Elektrik-Elektronik mühendisi",
        "Elektronik ve Haberleşme mühendisi",
        "Elektrikçi",
        "Eleştirmen",
        "Embriyolog",
        "Emlakçı",
        "Emniyet amiri",
        "Emniyet genel müdürü",
        "Endüstri mühendisi",
        "Endüstri sistemleri mühendisi",
        "Enstrüman imalatçısı",
        "Ergonomist",
        "Eskici",
        "Esnaf",
        "Estetisyen",
        "Etolojist",
        "Etimolog",
        "Etnolog",
        "Ev hanımı",
        "Fabrika işçisi",
        "Fahişe",
        "Falcı",
        "Fermantasyon işçisi",
        "Fıçıcı",
        "Fırıncı",
        "Figüran",
        "Film yapımcısı",
        "Film yönetmeni",
        "Filozof",
        "Finansör",
        "Fizikçi",
        "Fizyonomist",
        "Fizyoterapist",
        "Acil tıp teknisyeni",
        "Fon yöneticisi",
        "Forklift operatörü",
        "Fotoğrafçı",
        "Futbolcu",
        "Gardiyan",
        "Galerici",
        "Garson",
        "Gazete dağıtıcısı",
        "Gazete satıcısı",
        "Gazeteci",
        "Gelir uzmanı",
        "Gelir uzman yardımcısı",
        "Gemici",
        "General",
        "Genetik mühendisi",
        "Geyşa",
        "Gezgin",
        "Gezici vaiz",
        "Gıda mühendisi",
        "Gitarist",
        "Gondolcu",
        "Gökbilimci",
        "Göz doktoru",
        "Gözetmen",
        "Gözlükçü",
        "Grafiker",
        "Gramer uzmanı",
        "Greyder operatörü",
        "Guru",
        "Güfteci",
        "Gümrük memuru",
        "Gümrük müşaviri",
        "Gümrük müşavir yardımcısı",
        "Gümrük uzmanı",
        "Gündelikçi",
        "Güzellik uzmanı",
        "Haberci",
        "Haddeci",
        "Haham",
        "Hakem",
        "Halıcı",
        "Halkbilimci",
        "Hamal",
        "Hamamcı",
        "Hamurkâr",
        "Hareket memuru",
        "Haritacı",
        "Harita mühendisi",
        "Hastabakıcı",
        "Hattat",
        "Hava trafikçisi",
        "Havacı",
        "Haydut",
        "Hayvan bakıcısı",
        "Hayvan terbiyecisi",
        "Hemşire",
        "Hesap uzmanı",
        "Heykeltıraş",
        "Hırdavatçı",
        "Hırsız",
        "Hidrolikçi",
        "Hizmetçi",
        "Hokkabaz",
        "Host",
        "Hostes",
        "Hukukçu",
        "Hurdacı",
        "İcra memuru",
        "İç mimar",
        "İğneci",
        "İhracatçı",
        "İktisatçı",
        "İlahiyatçı",
        "İllüzyonist",
        "İmam",
        "İnsan kaynakları uzmanı",
        "İnşaat mühendisi",
        "İnşaatçı",
        "İpçi",
        "İplikçi",
        "İstatistikçi",
        "İstihkâmcı",
        "İşaretçi",
        "İşçi",
        "İşletmeci",
        "İşletme mühendisi",
        "İşportacı",
        "İş ve Uğraşı Terapisti",
        "İtfaiyeci",
        "İthalatçı",
        "Jeofizik mühendisi",
        "Jeoloji mühendisi",
        "Jeolog",
        "Jeomorfolog",
        "Jinekolog",
        "Jimnastikçi",
        "Jokey",
        "Kabin görevlisi",
        "Kabuk soyucusu",
        "Kadın berberi",
        "Kadın terzisi",
        "Kâğıtçı",
        "Kahveci",
        "Kâhya",
        "Kalaycı",
        "Kalıpçı",
        "Kaloriferci",
        "Kamarot",
        "Kameraman",
        "Kamyoncu",
        "Kapı satıcısı",
        "Kapıcı",
        "Kaplamacı",
        "Kaportacı",
        "Kaptan",
        "Kardinal",
        "Kardiyolog",
        "Karikatürist",
        "Karoserci",
        "Karpuzcu",
        "Kasap",
        "Kasiyer",
        "Kat görevlisi",
        "Kâtip",
        "Kayıkçı",
        "Kaymakam",
        "Kaynakçı",
        "Kazıcı",
        "Kebapçı",
        "Kemancı",
        "Kesimci",
        "Keskin Nişancı",
        "Kırtasiyeci",
        "Kimyager",
        "Kimya mühendisi",
        "Kitapçı",
        "Klarnetçi",
        "Koleksiyoncu",
        "Komedyen",
        "Komisyoncu",
        "Komiser",
        "Konserveci",
        "Konsolos",
        "Konsomatris",
        "Kontrolör",
        "Konveyör operatörü",
        "Kopyalayıcı",
        "Koreograf",
        "Korgeneral",
        "Koramiral",
        "Korsan",
        "Koruma görevlisi",
        "Komiser",
        "Komiser yardımcısı",
        "Kozmolog",
        "Köfteci",
        "Kömürcü",
        "Köpek eğiticisi",
        "Köşe yazarı",
        "Kuaför",
        "Kuşçu",
        "Kumarbaz",
        "Kumaşçı",
        "Kumcu",
        "Kuru temizlemeci",
        "Kuruyemişçi",
        "Kurye",
        "Kuşbilimci",
        "Kuyumcu",
        "Kürkçü",
        "Kütüphaneci",
        "Krupiye",
        "Laborant",
        "Laboratuvar işçisi",
        "Lahmacuncu",
        "Lehimci",
        "Levazımcı",
        "Lobici",
        "Lokantacı",
        "Lokomotifçi",
        "Lostromo",
        "Lostracı",
        "Lokman",
        "Madenci",
        "Makasçı",
        "Makastar",
        "Maketçi",
        "Makinist",
        "Makine mühendisi",
        "Makine zabiti",
        "Makyajcı",
        "Mali hizmetler uzmanı",
        "Manastır baş rahibesi",
        "Manav",
        "Manifaturacı",
        "Manikürcü",
        "Manken",
        "Marangoz",
        "Masör",
        "Masöz",
        "Matador",
        "Matbaacı",
        "Matematikçi",
        "Matkapçı",
        "Medya Planlama Uzmanı",
        "Memur",
        "Menajer",
        "Mermerci",
        "Metalurji mühendisi",
        "Meteoroloji uzmanı",
        "Metin yazarı",
        "Mevsimlik işçi",
        "Meydancı",
        "Meyhaneci",
        "Mezarcı",
        "Midyeci",
        "Mikrobiyolog",
        "Milletvekili",
        "Mimar",
        "Misyoner",
        "Mobilyacı",
        "Modacı",
        "Model",
        "Modelci",
        "Modelist",
        "Montajcı",
        "Montör",
        "Motor tamircisi",
        "Motorcu",
        "Muhabbet tellalı",
        "Muhabir",
        "Muhafız",
        "Muhasebeci",
        "Muhtar",
        "Mumyalayıcı",
        "Muzcu",
        "Mübaşir",
        "Müdür",
        "Müezzin",
        "Müfettiş",
        "Müşavir",
        "Mühendis",
        "Müneccim",
        "Mürebbiye",
        "Müsteşar",
        "Müteahhit",
        "Mütercim",
        "Müze müdürü",
        "Müzik yönetmeni",
        "Müzisyen",
        "Nalıncı",
        "Nakışçı",
        "Nakliyeci",
        "Nalbant",
        "Nalbur",
        "Noter",
        "Obuacı",
        "Ocakçı",
        "Odacı",
        "Oduncu",
        "Okçu",
        "Okul müdürü",
        "Okutman",
        "Operatör",
        "Opera sanatçısı",
        "Orgcu",
        "Orgeneral",
        "Orman mühendisi",
        "Ornitolog",
        "Otelci",
        "Oto elektrikçisi",
        "Oto lastik tamircisi",
        "Oto tamircisi",
        "Oto yedek parçacı",
        "Overlokçu",
        "Oymacı",
        "Oyuncu",
        "Oyun hostesi",
        "Oyun yazarı",
        "Oyuncakçı",
        "Öğretmen",
        "Öğretim elemanı",
        "Öğretim görevlisi",
        "Öğretim üyesi",
        "Örmeci",
        "Ön muhasebeci",
        "Ön muhasebe sorumlusu",
        "Ön muhasebe yardımcı elemanı",
        "Ön büro elemanı",
        "Özel şoför",
        "Paketleyici",
        "Palyaço",
        "Pandomimci",
        "Pansiyoncu",
        "Pansumancı",
        "Papa",
        "Papaz",
        "Paralı asker",
        "Park bekçisi",
        "Pastörizör",
        "Patolog",
        "Peçeteci",
        "Pencereci",
        "Perukçu",
        "Peyzaj mimarı",
        "Peyzaj teknikeri",
        "Pideci",
        "Pilavcı",
        "Pilot",
        "Piskopos",
        "Piyade",
        "Piyango satıcısı",
        "Piyanist",
        "Polis memuru",
        "Polis şefi",
        "Polisajcı",
        "Pompacı",
        "Postacı",
        "Profesör",
        "Proktolog",
        "Protokol görevlisi",
        "Psikiyatr",
        "Psikolog",
        "Psikolojik danışmanlık ve rehberlik",
        "Paramedik",
        "Radyolog",
        "Redaktör",
        "Rehber",
        "Rejisör",
        "Reklamcı",
        "Rektör",
        "Rektör yardımcısı",
        "Remayözcü",
        "Ressam",
        "Resepsiyon memuru",
        "Rot balansçı",
        "Radyoloji teknisyeni/teknikeri",
        "Saat tamircisi",
        "Saatçi",
        "Sağlık teknisyeni",
        "Sahil koruma",
        "Saksofoncu",
        "Salepçi",
        "Sanat yönetmeni",
        "Sanayici",
        "Sansürcü",
        "Santral memuru",
        "Saraç",
        "Sarraf",
        "Satış elemanı",
        "Savcı",
        "Saz şairi",
        "Sekreter",
        "Senarist",
        "Sepetçi",
        "Serbest muhasebeci mali müşavir",
        "Ses teknisyeni",
        "Seyis",
        "Sınırlı baş makinist",
        "Sicil memuru",
        "Sigortacı",
        "Sihirbaz",
        "Silahçı",
        "Silindir operatörü",
        "Simitçi",
        "Simyacı",
        "Sistem mühendisi",
        "Sistem yöneticisi",
        "Siyasetçi",
        "Soğuk demirci",
        "Sokak çalgıcısı",
        "Sokak satıcısı",
        "Son ütücü",
        "Sorgu hâkimi",
        "Sosyal hizmet uzmanı",
        "Sosyolog",
        "Spiker",
        "Stenograf",
        "Stilist",
        "Striptizci",
        "Su tesisatçısı",
        "Subay",
        "Sucu",
        "Suflör",
        "Sulh hâkimi",
        "Sunucu",
        "Susuz araç yıkama",
        "Sünnetçi",
        "Sürveyan",
        "Sütanne",
        "Sütçü",
        "Şahinci",
        "Şair",
        "Şapel papazı",
        "Şapkacı",
        "Şarap üreticisi",
        "Şarkıcı",
        "Şarkı sözü yazarı",
        "Şarküter",
        "Şekerci",
        "Şemsiyeci",
        "Şifre çözümleyici",
        "Şimşirci",
        "Şoför",
        "Tabakçı",
        "Tabelacı",
        "Tahsildar",
        "Taksici",
        "Tarım işçisi",
        "Tarihçi",
        "Tasarımcı",
        "Taşçı",
        "Taşlayıcı",
        "Tatlıcı",
        "Tavukçu",
        "Tayfa",
        "Tefeci",
        "Teğmen",
        "Tekniker",
        "Teknisyen",
        "Teknoloji uzmani",
        "Telefon operatörü",
        "Telekız",
        "Televizyon tamircisi",
        "Tellal",
        "Temizlikçi",
        "Temsilci",
        "Terapist",
        "Tercüman",
        "Terzi",
        "Tesgahtar",
        "Tesisatçı",
        "Tesviyeci",
        "Test mühendisi",
        "Test pilotu",
        "Teşrifatçı",
        "Tiyatro yönetmeni",
        "Tombalacı",
        "Topçu",
        "Tornacı",
        "Turizmci",
        "Tuğgeneral",
        "Tuhafiyeci",
        "Turşucu",
        "Tuzcu",
        "Tümamiral",
        "Tümgeneral",
        "Uçuş teknisyeni",
        "Ulaşım sorumlusu",
        "Ustabaşı",
        "Uydu antenci",
        "Uzay mühendisi",
        "Uzay bilimcisi",
        "Uzman Jandarma",
        "Uzman Çavuş",
        "Üretici",
        "Ürolog",
        "Ütücü",
        "Vaiz",
        "Vali",
        "Vergi denetmeni",
        "Vergi müfettişi",
        "Vergi tahakkuk memuru",
        "Veritabanı yöneticisi",
        "Veri hazırlama ve kontrol işletmeni",
        "Vestiyerci",
        "Veteriner hekim",
        "Veteriner sağlık teknikeri",
        "Veteriner sağlık teknisyeni",
        "Veznedar",
        "Video editörü",
        "Vinç operatörü",
        "Vitrinci",
        "Viyolonselci",
        "Yarbay",
        "Yardımcı hakem",
        "Yardımcı hizmetli",
        "Yardımcı pilot",
        "Yargıç",
        "Yatırım uzmanı",
        "Yayıncı",
        "Yazar",
        "Yazı işleri müdürü",
        "Yazılım mühendisi",
        "Yelkenci",
        "Yeminli mali müşavir",
        "Yeminli tercüman",
        "Yer gösterici",
        "Yer teknisyeni",
        "Yerölçmeci",
        "Yoğurtçu",
        "Yol bekçisi",
        "Yorgancı",
        "Yorumcu",
        "Yönetici",
        "Yüzücü",
        "Yönetmen",
    ]
