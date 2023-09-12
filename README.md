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