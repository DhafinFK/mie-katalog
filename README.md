TAUTAN ADAPTABLE SAYA TIDAK ADA
-penjelasan-
akun saya di adaptable di disable
-akhir penjelasan-


Checklist dan penjelasan:

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
2. /json/
3. /xml/'id'
4. /json/'id'
5. / (html)