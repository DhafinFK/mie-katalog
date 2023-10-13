TAUTAN ADAPTABLE SAYA TIDAK ADA
-penjelasan-
akun saya di adaptable di disable
-akhir penjelasan-

--- tugas 2 ---

Checklist Item 1: Membuat project django baru

-> Saya membuat project baru dengan menjalankan command "django-admin startproject mie_katalog" setelah saya activate virtual environment. command tersebut saya akses dari command prompt dengan mengganti directory ke directory yang saya inginkan (yaitu directory khusus matkul pbp)

Checklist Item 2: Membuat aplikasi dengan nama main pada project tersebut

-> Saya membuat aplikasi dengan nama main dengan menjalankan command "django-admin startapp main" di command prompt sesuai dengan directory saat pertama kali saya startproject

Checklist Item 3: Melakukan routing pada proyek agar dapat menjalankan aplikasi

-> Saya melakukan routing aplikasi agar dipakai dalam project dengan memasukkan "main.apps.MainConfig" sesuai dokumntasi resmi dari django. Hal tersebut dilakukan agar ibaratnya menginstall sehingga dapat menggunakan segala setting, data, dan function yang telah di set didalam app tersebut.

Checklist Item 4: membuat model Item dan memberikan atribut yang sesuai

-> Saya membuat model item tetapi mengganti nama model tersebut menjadi Indomie karena tema yang saya ingin ambil adalah katalog seluruh indomie yang pernah ada dan bisa disortir serta bisa melihat tracking sisa stock dari indomie tersebut. Model indomie mengandung models name yang implementasikan sebagai nama dari jenis indomie yang saya set sebagai CharField dengan maximal length 200 character, field amount yang saya implementasikan sebagai sisa indomie jenis tertentu di dunia dengan default value 100, Description yang menjelaskan karakteristik atau memberikan komentar tentang jenis indomie tertentu, dan terakhir adalah field type yang merupakan charfield tetapi menggunakan choice jadi dapat dipilih antara mie goreng atau kuah.

Checklist Item 5: Membuat views.py

-> Saya membuat satu views katalog saja di app main sejauh ini yang hanya menunjukkan semua jenis mie beserta opsi untuk filter apabila menerima request method post yang kemudian akan disesuaikan dengan value yang diterima berdasarkan key dari post tersebut. Setiap kasus menerima request.method post ada kemungkinan mengganti context masing-masing sehingga output di website untuk view katalog. Kemudian view tersebut melakukan shortcut render yang disediakan oleh django untuk menentukan template yaitu

Checklist Item 6: Membuat routing pada urls.py

-> saya melakukan url routing dari urls.py di mie_katalog ke aplikasi main menggunakan tools dari django.urls yaitu include(). Hal tersebut saya lakukan dengan mengimport include dari django.urls. Saya melakukan routing sehingga apabila lanjutan url pattern dari localhost merupakan "/mie-katalog/" maka akan lanjut ke main app

Checklist Item 7: Melakukan deployment ke adaptable

-> Saya membuat repository baru di github saya untuk mie katalog ini dan kemudian saya sambungkan directory mie katalog ini dengan repository tersebut. Setelah saya sambungkan saya commit semua isi dari directory ini dan saya push ke github repository. Kemudian setelah saya melakukan push. Saya masuk ke adaptable dan launch app dari repository mie-katalog dengan basis dari aplikasi python karena menggunakan django, selain itu database yang dipake postgre sql meskipun dari django basis nya menggunakan sqlite. terakhir set versi python yang sesuai dan command line untuk start project.

Bagan request client ke web app:

client ---(mengirim request)---> Cek url config di urls.py project -----(nemu include ke main)---->cek url config di urls.py main ----(nemu url config yg sesuai)----> cek views yang sesuai dengan url config yang dicek -----(refer ke)----> database yang hasil pembuatan dari models.py ----(kembali lagi)----> views.py mengolah request berdasarkan query database yang tepat

penjelasan: Jadi client akan mengirimkan request yang berupa url tertentu. Url tersebut kemudian akan diperiksa di urls.py project terlebih dahulu dan dalam konteks ini akan menjalankan function include() ke app. Setelah di sambungkan patternya dengan urls.py di app main maka akan dialihkan ke views.py untuk menjalankan fbv yang sesuai di views.py. Kemudian apabila di views yang sesuai memerlukan query database maka akan menggunakan instance dari models yang didefiniskan di models.py yang tersimpan di database. setelah mendapatkan query database yang sesuai maka akan kembali ke views untuk mengolah data tersebut.

Mengapa Kita menggunakan virtual environment:

Jadi setiap project akan membutuhkan dependencies nya masing-masing. dalam konteks python maka akan ada beberapa pip package yang perlu di install apabila hanya menggunakan satu environment utama maka environment tersebut akan berantakan dan menumpuk dengan package yang belum tentu akan dipakai lagi. Apabila kita membuat virtual environment untuk suatu project khusus yaitu virtual environment kita hanya perlu menginstall package yang dibutuhkan saja tanpa menambah-nambah hal-hal yang sekiranya tidak akan dipakai karena sudah sesuai dengan kebutuhan project

Perbedaan MVC, MVT, MVVM

Definisi dari ketiganya bisa dimulai dari 2 huruf pertama yaitu M dan V. M = Model yang bertanggung jawab untuk mengelola data dan logika aplikas. Model berintteraksi langsung dengan database dan mengatur bagaimana data akan ditampilkan. Sedangkan V = View yang bertanggung jawab untuk menampilkan data tersebut. View adalah interface pengguna, seperti halaman web atau tampilan aplikasi

Perbedaan utama terdapat pada huruf-huruf terakhir setelah MV dimana C = controller yang mengatur alur kontrol dalam aplikasi, menerima input dari puengguna, memprosesnya, dan mengirim perintah ke model atau view yang sesuai. T = Template yang menggambarkan data dari model menjadi tampilan yang konkret bagian ini intinya menformat tampilan. VM = ViewModel sebuah komponen tambahan yang memisahkan logika tampilan dari data. Viewmodel mengubah data dari model menjadi bentuk yang dapat ditampilkan oleh view

selain dari tiga huruf tersebut MVC dan MVT cenderung lebih tradisional dibandingkan MVVM yang lebih modern dan merupakan evolusi lebih baru.

--- tugas 3 ---

PERBEDAAN POST & GET:

POST dan GET keduanya merupakan http request method namun terdapat beberapa perbedaan dimana:

1. Tujuan utama dari get method merupakan request data dari server sedangkan post method digunakan untuk mengirim data ke server untuk di proses
2. Pengiriman data pada method get melalui append di kalimat url sedangkan post method tidak append data yang ingin di kirim di kalimat url dan terdapat di request body nya. Sehingga dapat mengirim lebih banyak data dan lebih cocok untuk mengirim data yang ingin dirahasiakan karena tidak muncul di URL
3. Karena get method menambahkan pengiriman data ke kalimat url maka dianggap tidak se aman post method karena post method tidak menunjukkan data transmission dalam url nya

PERBEDAAN XML, JSON, dan HTML:

1. JSON dan XML lah format file utama yang digunakan untuk pertukaran dan pengaturan presentasi struktur data
2. JSON lebih sering digunakan untuk API untuk pertukaran data antara client dan server
3. XML dan HTML menggunakan tag untuk pengkategorian data, bedanya XML lebih untuk pertukaran data sedangkan HTML lebih sering digunakan untuk membuat tampilan di website

ALASAN JSON SERING DIGUNAKAN DALAM PERTUKARAN DATA ANTARA APLIKASI WEB MODERN:

1. JSON ringan dan human readable serta machine readable. Serta syntax nya mirip dengan javascript
2. JSON sudah natively supported dalam banyak browsing engine sehingga penggunaannya luas
3. JSON memang di design untuk menjadi sangat efisien untuk transfer data dalam web
4. Compatible dengan javascript yang telah digunakan sangat luas
5. Sudah sangat terkenal untuk membuat API yang memungkinkan komunikasi antara frontend dan backend.
6. dn masih banyak lagi

PEMBUATAN SEMUA OBJECTIVE TUGAS 2:

1. saya menggunakan fitur form yang disediakan oleh django framework dengan membuat file baru bernama forms.py. Didalam forms.py saya membuat class form untuk model Indomie dan menuliskan semua fields yang akan dijadikan editable input. Kemudian saya melakukan url routing dari domain/mie-katalog/ ke create-mie jadi domain/mie-katalog/create-mie. url tersebut mengarah ke create mie view yang berfungsi untuk menerima request method POST dari form.html yang menggunakan django logic untuk menampilkan semua field input. Apabila method == POST dan form yang di post valid maka form tersebut akan di save sebagai instancce baru dari Indomie model dan dimasukkan ke database. Apabila tidak memenuhi syarat method == POST dan form tidak valid maka akan kembali ke page form.html sampai form yang dibuat benar atau user memencet ancor "back" yang mengarahkan ke katalog utama. Apabila berhasil, maka user akan di redirect kembali ke main katalog menggunakan django urls httpresponseredirect.

2. Untuk membuat 5 fungsi views. pertama saya membuat 5 url routing dengan salah satu url routing ke main katalog yang merupakan display data mengguanakan html. dalam main katalog saya menggunakan django logic pada html template untuk for loop semua context 'mies' yang di passing dari katalog view. Setelah itu saya membuat masing-masing view untuk show json, show sml, show xml by id, show json by id. Cara kerja show json dan show xml mirip dengan mengambil semua object indomie dari database dan di query ke dalam variabel data yang kemudian menjadi bagian context dari masing-view. Perbedaan dari show xml dan show json adalah penggunaan serializers pada django dimana serializers melakukan data serialization sehingga menjadi format json atau xml sesuai view yang diakses. Sedangkan untuk show xml by id dan show json by id sama saja melakukan data serialization pada data yang sudah di assign sebelumnya, namun saat ini data bukan semua instance dari object indomie melainkan satu object saja yang di filter berdsarkan primary key. argumen primary key yang di passing ke function show by id didapatkan dari url config dimana terdapat /<int:id>/ potongan url tersebut akan mem passing id yang diisi menjadi argumen pk=id di show by id views.

3. Untuk menjawab pertanyaan-pertanyaan yang perlu dijawab di readme.md ini, Saya pertama menanyakan chatgpt untuk referensi materi dan kemudian jawaban dari chatgpt juga. Kemudian saya crosscheck jawaban dari chatgpt dan referensi-referensi yang terpercaya sehingga saya yakin dengan jawaban yang akan saya tulis.

AKSES URL DENGAN POSTMAN:

1. /xml/
   ![xml](https://github.com/DhafinFK/mie-katalog/blob/main/gambar_untuk_readme/xml_noid.png)
2. /json/
   ![JSON](https://github.com/DhafinFK/mie-katalog/blob/main/gambar_untuk_readme/json_noid.png)
3. /xml/'id'
   ![xml_id](https://github.com/DhafinFK/mie-katalog/blob/main/gambar_untuk_readme/xml_id.png)
4. /json/'id'
   ![JSON_id](https://github.com/DhafinFK/mie-katalog/blob/main/gambar_untuk_readme/json_id.png)
5. / (html)
   ![HTML](https://github.com/DhafinFK/mie-katalog/blob/main/gambar_untuk_readme/html.png)

--- tugas 4 ---

1. UserCreationForm dari django merupakan built in form yang membuat sebuah user tanpa previlage apapun selama diberikan username dan password. secara default usercreationform memiliki tiga field input yaitu username, password1, dan password2. password ada dua agar user bisa konfirmasi ulang password yang telah dimasukkan ke dalam input fields. UserCreationForm merupakan child class dari forms.ModelForm yang dimana modelnya adalah user. karena UserCreationForm merupakan child dari modelform maka form ini bisa dicek valid atau tidak. Hasil cek validasi akan menyimpan cleaned data yang lagi-lagi bisa diakses berdasarkan key yang sesuai.

   Beberapa keuntungan dari UserCreationForm adalah:

   1. Sangat sederhana untuk diimplementasikan karena kode-kode sudah dibuat oleh django dan hanya perlu disesuaikan dengan view yang dibuat
   2. Sudah terdapat built-in validations untuk input field. jadi pengguna tidak perlu membuat function/method tambahan untuk memeriksa kebenaran atau kelengkapan dari form tersebut.
   3. Sudah handle password checking.

   Beberapa Kekurangan dari UserCreationForm adalah:

   1. Customization yang terbatas karena pada akhirnya kita menggunakan sesuatu yang sudah disediakan oleh django.
   2. Tidak menyediakan email confirmation atau bahkan email input
   3. Tidak ideal untuk form pembuatan user yang lebih advance yang membutuhkan data-data lain karen UserCreationForm menggunakan username-password fields. Bila diperlukan input untuk pembuatan user yang lebih lengkap maka perlu customization atau membuat form tersendiri.

2. Authentication: merupakan proses validasi atau authentication apakah user tertentu sudah terdaftar didalam, biasanya digunakan untuk login. Authorization: pemberian previlage-previlage atau assign role tertentu untuk user tertentu. Kedua proses tersebut penting agar data-data bisa di assign ke pemiliknya masing-masing dan setiap user memiliki batasan. Tidak sembarang user bisa mengakses semua fitur atau data yang tersedia dalam website. Untuk membatasi kebebasan tersebut adalah dengan authentication dan authorization. Untuk bagian authorization lebih khususnya, diperlukan karena setiap pengguna bisa saja memiliki peran yang berbeda-beda dan tidak semua peran memiliki kebebasan akses yang sama.

3. Cookies dalam konteks web development merupakan potongan kode kecil yang disimpan di client-side yang digunakan untuk menyimpan data-data yang terkait dengan session pengguna. Django sendiri menggunakan cookies untuk mengelola data sesi pengguna. informasi-informasi penting terkait login session user akan disimpan adalam cookie oleh django. Tentunya data yang disimpan sudah melalui proses enkripsi oleh django sehingga informasi tersebut aman.

4. secara default penggunaan cookies aman selama diimplementasikan dengan benar karena berbagai security measures yang sudah dilengkapi dengan sistem cookies termasuk django. Namun, cookies tetap memiliki resiko keamanan dimana pada akhirnya data yang disimpan dalam cookies mungkin saja data krusial atau data yang penting. Jika implementasi cookies yang digunakan tidak memiliki security measures yang baik cookies dapat menjadi sasaran serangan man-in-the-middle untuk intercept data yang dikirimkan data melalui jaringan. selain itu cookies dapat menjadi resiko keamanan bagi orang-orang yang tidak ingin data pribadinya tersimpan atau tersebar sama sekali. Terakhir cookie bisa saja dicuri dengan cookie theft. Lagi-lagi resiko tersebut semakin besar apabila implementasi cookie sistem yang digunakan tidak secure atau security measures nya kurang optimal.

5. tahapan melakukan checklist
   checklist item 1:
   Saya mengimplementasikan fungsi registrasi, login, dan logout dengan menggunakan function based views dan belum menggunakan class based views atau form-form yang sudah disediakan oleh django.

- Untuk login saya membuat fbv login yang menerima request.method yaitu 'POST'. bila dari request method tersebut diambil key username dan password dan dimasukkan ke dalam variabel masing-masing untuk di authenticate. hasil authentication dimasukan ke dalam variabel user. Apabila authentication berhasil maka akan dilakukan function login yang disediakan oleh django untuk variabel user tadi. Jika berhasil akan memberikan url route menuju katalog utama dan mengatur key 'last_login' sebagai datetime.now() atau sekarang kemudian cookie dioper ke dalam komputer karena cookie cara kerjanya seperti dictionary. Namun, apabila user gagal authentication nya maka akan render page login yang sama dengan memberikan message-message yang di display di page. Login page menggunakan html table yang menjabarkan login form yang dibuat dari python. Saya membuat url pattern login di url localhost agar langsung bisa login. dan apabila django masih menyimpan login session dari user sebelumnya maka akan langsung redirect ke page utama katalog.

- Untuk registrasi saya membuat function based views kembali yang menerima request method dan menggunakan template form dari python juga. form yang digunakan menggunakan form built in dari django yaitu UserCreationForm yang dimasukkan ke dalam context apabila request method bukan post. Namun apabila request method nya post maka request.POST akan dijadikan parameter untuk user creaton form untuk mengambil value2 dari input/field yang disediakan dalam form. Kemudian form tersebut dicek apakah sudah valid (berarti sudah mengisi semua input field dengan sesuai). saya menambahkan fitur dimana bila telah registrasi langsung login dengan akun yang baru saja di registrasi. karena form sudah dilakukan method .is_valid() maka sekarang data dari form sudah dirapihkan dalam cleaned data dan bisa diambil id 'username' dan 'password1' untuk dimasukkan kedalam variabel-variabel yang sesuai. setelah menyesuaikan variabel maka tahapan berikutnya adalah login yang sama seperti tahapan login pada fbv login view. Untuk user interface yang digunakan untuk registrasi mengextend base.html dan menggunakan html table untuk merapihkan posisi.

- Untuk logout saya membuat fbv logout yang menyimpan user yang saat ini logged in dan melakukan built in function dari django logout(). setelah logout, user akan langsung redirect ke login page. Untuk logout view tidak memerlukan html file karena hanya menjalankan function logout dan tidek perlu menampilkan user interface.

checklist item 2 & 3:

- membuat field baru di model indomie dengan menambahkan foreignkey yang terhubung dengan seorang user. Foreignkey membuat hubungan antara satu model dengan model yang lain disini seorang user bisa terhubung dengan beberapa indomie. (foreignkey merupakan many-to-one relationship)
- saat di makemigrations terpaksa semua data yang saya buat langsung dihubungkan ke superuser
- karena sekarang bisa membuat user dengan registrasi maka saya membuat dua akun yang sudah saya cantumkan nama dan password dari kedua dummy account.
- setelah membuat kedua dummy account. Saya login ke masing-masing account dan membuat item item atau mie yang sudah dibuat sehingga langsung terhubung dengan user yang sedang log in. di main katalog sudah diatur dimana user hanya bisa melihat indomie yang telah ditambahkan oleh dirinya.

checklist item 4:

- dengan menggunakan .set_cookie untuk mengatur key dalam cookie dengan value yang sesuai.
- cookie bertingkah seperti dictionary dalam python.
- karena sudah memberikan key dan value dalam cookie maka kedua key dan value yang ada di dalam cookie bisa digunakan oleh view-view lain. seperti pada main katalog dimana cookie menampilkan detail terakhir login seorang user. selama dimasukkan ke dalam context maka bisa di akses di html file menggunakan django logic.

--- tugas 5 ---

1. element selector digunakan untuk memilih elemen-elemen tertentu dari suatu html. Elemen-elemen yang dipilih kemudian dapat diubah penampilan, penempatan, dan alignment secara individu maupun secara berkelompok menggunakan class, id, ataupun langsung select elemen itu sendiri (e.g. input, paragraph, heading). Selector ini sangat berguna untuk customize User Interface atau display dari website kita. Waktu paling tepat untuk menggunakan selector adalah saat kita ingin memperbagus design dari frontend website kita karena tentunya design yang bagus tidak dapat dilakukan tanpa melakukan select pada suatu element atau komponen dari html. Lebih spesifiknya apabila ada group atau bahkan elemen individu yang ingin kita ubah penamipilannya, penempatan, atau ukurannya.
2. tag-tag yang terdapat dalam html5 sangat banyak, berikut adalah beberapa contoh dari tag-tag yang terdapat didalam html5:
   - <a> tag atau anchor yang digunakan untuk mencantumkan hyperlink dalam sebuat tulisan/string
   - <body> menandai bagian mana yang termasuk body dari suatu html file
   - <button> tag untuk membuat suatu button yang dapat di click
   - <div> tag yang membagi bagi kode-kode yang terdapat dalam html file kita menjadi bagian-bagian tertentu yang dapat dinamakan oleh kita
   - <h1> - <h6> tag yang merepresentasikan heading dalam suatu html file
   - <head> tag yang tidak berada dalam body tapi mengandung informasi di bagian had suatu website
   - <hr> tag yang membuat suatu horizontal line
   - <img> tag yang merepresentasikan suatu file image yang akan dipasang di page website
   - <html> tag yang mendefinisikan root dari html document
   - <input> tag yang membuat input yang dapat berupa berbagai macam jenis di suatu html tag
   - <link> tag yang menyambungkan dan mnjelaskan hubungan antara sebuah document html dan document luar
   - <ul> tag untuk unordered list yang tidak menampikan urutan dari item-item yang didalamnya
   - <ol> tag untuk ordered list yang menampilkan urutan dari item-item yang didalmya
   - <li> tag yang mendefinisikan suatu list item untuk ol dan ul
   - <main> seperti div namun menandakan bagian utama dari html file
   - <meta> menyatakan susunan metadata suatu isi dokumen
   - <p> tag yang mendefinisikan suatu paragraf yang berisikan teks
   - <span> membagi bagian tertentu dari suatu teks yang tidak memberikan style secara default
   - <strong> bold
   - <style> tag untuk menyelimpkan code css dalam bagian head dari html document
   - <table> membuat html table
   - <td> tag cell dalam table
   - <tr> tag row dalam table
   - <textarea> seperti input textfield namun muat untuk multiline
   - dan masih banyak lagi
3. margin dan padding keduanya adalah format spacing untuk suatu elemen didalam container. Namun perbedaannya adalah elemen yang bergerak dan elemen yang terdiam apabila diberikan spacing. spacing menggunakan margin membuat space antara container dengan elemen yang didalamnya, jadi bisa ibaratnya apabila ada dua elemen didalam suatu container. Kemudian elemen 1 dari 2 elemen diberikan padding. Yang menjadi target utama perubahan posisi adalah elemen 1 karena menambah spacing antara elemen dan container. Sedangkan margin memberikan space antar elemen. Kita ambil kasus yang sebelumnya dimana terdapat 2 item. Sekarang elemen 2yang diberikan spacing berupa margin. elemen satu yang akan terdorong karena margin membuat space antara elemen dan elemen lain bukan membuat space antara elemen dan container. Keduanya mudah seklai tertukar.
4. Keduanya adalah framework css yang membuat hidup kita lebih mudah dalam menuliskan css code. Namun terdapat perbedaan

   - Bootstrap banyak menyediakan pre designed components yang membuat kita tidak perlu ngoding lebih banyak kode. Selain itu dengan menyediakan pre designed components framework bootstrap dapat membuat komponen-komponen yang lebih konsisten dibandingkan dengan kita menulis sendiri. Selain itu bootstrap melakukan styling berdasarkan kelas kelas yang dibuat dalam html file. Jadi bootstrap mentarget class-class yang sudah ada di html atau yang kita buat sendiri. Karena design bootstrap banyak yang sudah dibuat oleh bootstrap maka design kita akan terlihat "bootstrap"ish atau bisa dikenali sebagai design yang menggunakan framework bootstrap
   - Tailwind lebih fleksibel design nya dibandingkan bootstrap karena tidak menyediakan pre designed components kecuali mengimport package-package dan library tailwind. Tailwind sangat mudah untuk dicustomize karena tadi tidak menyediakan pre designed components secara default dan kita bisa men define sendiri styling class. Selain define class sendiri utuk styling kita juga bisa mengoverride styling untuk design-design tertentu karena css memiliki low specifity atau tidak terlalu spesifik untuk suatu komponen saja.

   Menurut saya pribadi penggunaan tailwind dan bootstrap hanya dibagi menjadi dua kasus. Apabila kita ingin membuat design dengan sangat cepat dan ringkas kita akan menggunakan bootstrap karena pre design components nya. sedangkan saat kita ingin menggunakan framework yang sangat fleksibel tapi tidak ingin menggunakan css native maka kita akan menggunakan tailwind.

5. Saya mengerjakan step by step satu per satu menggunakan css native tanpa framework karena saya masih ingin mengasaha skill native css agar saat saya pindah ke framework tailwind saya akan lebih mengerti. Mohon maaf kakak yang memeriksa tugas saya karena saya belum bisa melekukan semua checkpoint fully karena dampak dari tugas matkul sebelah terima kasih ya kak. Semoga diberkati

--- Tugas 6 ---

1. program synchronous disebut juga sequential merupakan program yang menjalankan tugas satu persatu. Program yang berada di bawah suatu program lain tidak akan terjalankan bila program yang diatasnya belum selesai. sync programming lebih lambat daripada async tetapi sangat cocok untuk program yang bergantung pada hasil processing satu sama lain. Sedangkan async programming merupakan program yang tidak harus menunggu tugas program diatasnya untuk melanjutkan ke program berikutnya.

2. Paradigma event driven programming adalah metode pengembangan perangkat lunak di mana program merespons peristiwa, seperti tindakan pengguna atau peristiwa sistem, secara otomatis, tanpa harus secara langsung menunggu peristiwa tersebut. Program mengatur fungsi-fungsi atau "penangan peristiwa" yang akan dieksekusi saat peristiwa tertentu terjadi. salah satu dari penerapan paradigma tersebut adalah melakukan suatu program atau perintah tertentu ketika suatu tombol ditekan di halaman website dengan menambahkan event-listener

3. async pada ajax memanfaatkan kemampuan javascript untuk mengakses tiap-tiap dom dan mengubah atau memanipulasi dom tanpa perlu refresh seluruh page. Dari kemampuan javascript tersebut AJAX menggabungkan javascript dengan xml. XML diakses menggunakan XMLHttpRequest pada django yang digunakan untuk mengoper data dari database yang diperlukan. Data tersebut kemudian dapat digunakan untuk memanipulasi dom di html document.

alurnya:
browser menerima event => server memproses request dari event tersebut => browser menerima hasil proses dari server secara async

4. untuk method get ajax saya menggunakannya di dua bagian. bagian pertama adalah untuk mengambil data dalam bentuk json dari database untuk dioper ke refresh page karena refresh page berfungsi untuk menampilkan data yang baru ditambah. Selain itu method get juga saya tambahkan untuk fitur rekomendasi indomie untuk pengguna. cara kerjanya adalah ada interaksi ajax dengan django secara async yang mengambil mie random untuk direkomendasikan. Sedangkan method POST saya menggunakan design bawaan bootstrap untuk permasalahan modal. input dari semua modal kemudian di clear saat sudah tidak dipakai atau sudah di submit. Semua data dari modal tersebut dioper ke view khusu async ajax yang kemudian membuat instance dari indomie yang baru. setelah membuat mie baru kemudian function yang mengandung post memanggil function refresh untuk memperbarui tampilan katalog.

Untuk permasalahn routing seperti biasa saja.

tautan: http://dhafin-fadhlan-tugas.pbp.cs.ui.ac.id.
