# open-post-uuid


Djnago da uuid orqali ma'lumotlarni  ishalash va shifrlash
Django, Python dasturlash tilida yozilgan bir veb-kutubxona (web framework) hisoblanadi. UUID (Universally Unique Identifier) esa global aniqlash belg'ilari sifatida ishlatiluvchi bir identifikator hisoblanadi. Django, UUID'lar uchun integratsiya qilishni o'z ichiga olgan.

UUID'lar uni yaratayotgan qurilmalar, dasturlar, va h.k.ning turli maqsadlari uchun ishlatiladi. Bu belg'ilarni ishlatish sizning ma'lumotlar bazasidagi yozuvlarning bitta identifikator (ID) sifatida xizmat qilishi mumkin, shuningdek URL, fayl yoki ob'ekt identifikatorlari sifatida ham xizmat qilishi mumkin.

Django'da UUID'lar shu mavzuda to'g'ri integratsiya qilingan. Shu sababli, siz Django'da UUID'lar yaratishingiz va ularni ma'lumotlar bazasida yozuvlarga identifikator sifatida qo'shishingiz mumkin. Ushbu usul ma'lumotlar bazasidagi yozuvlarning ulardan foydalanish bilan o'zaro almashtirish qilishni ham osonlashtiradi.

Django'da UUID'lar foydalanish uchun uuid kutubxonasi yoki Django REST framework, Django's built-in uuid dastlabki sahifalari, shu bilan birga uuid yaratishni osonlashtiradigan oddiy model ma'lumotlarini integratsiya qilish mumkin.

args va kwargs: "args" va "kwargs"lar Python'da funksiyalarga argumentlar o'rnatingan daftarlar (list) va lug'atlar (dictionary) sifatida foydalaniladigan xususiyatlar hisoblanadi. Django'da, "args" va "kwargs"lar bitta funksiya yoki sinfni boshqarishda foydalaniladi. Misol uchun, bir model obyektini yaratishda MyModel.objects.create() funksiyasi args va kwargslarni qabul qiladi. Bu yordamda, siz MyModel sinfidagi ustunlarga, misol uchun name va agega, qiymatlar berishingiz mumkin. Bu qiymatlar "kwargs" yordamida to'g'ridan-to'g'ri sinfga o'tkaziladi va uni avtomatik ravishda yaratadi:
python
Copy code
MyModel.objects.create(name="John", age=25)
pk: "pk" ("primary key") shunchaki ma'lumotlar bazasidagi yozuvning bitta xususiy belgisidir. Barcha Django model sinflari "pk" nomi bilan bitta standart xususiyatga ega, shuningdek, "pk" xususiyati avtomatik ravishda yaratiladi. "pk" xususiyati, ma'lumotlar bazasidagi yozuvlar (records) orasida har bir yozuvni bitta xususiy belg'ilarga (unique identifier) bog'laydi.
Django'da bitta yozuvni boshqa yozuvga bog'lash uchun, "ForeignKey" xususiyati ishlatiladi. "ForeignKey" yordamida bitta yozuvning "pk" xususiyati boshqa yozuvda yoziladi. Misol uchun, agar siz "Person" va "Address" model calsslari o'zlashtirsangiz, "Address" model sinfindagi bitta yozuvni "Person" model sinfiga bog'lash uchun "ForeignKey" xususiyati ishlatishingiz mumkin:

class Person(models.Model):
    name = models.CharField(max_length=50)

class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)

Yukoridagi misolda, "Address" sinfida person xususiyati "ForeignKey" bilan "Person" sinfi bilan bog'lanadi. "person" xususiyati "Person" sinfi uchun "pk" xususiyati bilan bog'lanadi. "on_delete" argumenti esa "Person" sinfida yozuv o'chirilganda "Address" sinfi bilan bog'langan yozuvlar ham o'chirilishini ta'minlaydi.