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


