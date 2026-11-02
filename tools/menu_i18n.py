#!/usr/bin/env python3
"""Menu translations for both apps. Edit here, then run: python3 tools/menu_i18n.py
Rewrites the generated blocks in main.swift and windows/aura.cpp (between the BEGIN/END markers).
Russian system → Ukrainian menu (no Russian translation on purpose)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = ["enabled", "auto", "sound", "access", "app", "exclude", "game", "appLang", "noBinding", "exclusions", "recent",
        "bindings", "empty", "login", "words", "wordsTitle", "wordsInfo", "save", "cancel", "uiLang", "system", "hint",
        "report", "reportBody", "update", "updateDue", "donate", "quit"]
# code, native name, then one line per key (in KEYS order)
LANGS = """
en English
Enabled
Auto-correction
Sound
⚠︎ Grant access: Accessibility
App:
Don't work in this app
Game — AURA paused
Language for this app
No binding
Exclusions
Don't work in (recent apps)
Language bindings
Empty
Launch at login
My words…
AURA Switcher — my words
AURA Switcher treats these words as correct: it never changes them, and fixes them when typed in the wrong layout. Separate them with commas.
Save
Cancel
Menu language
System
Double ⇧ — convert word/selection
Report a problem…
What happened and in which app:
Check for updates…
⬆︎ An update may be available — check
Support AURA Switcher ☕
Quit

uk Українська
Увімкнено
Автовиправлення
Звук
⚠︎ Надайте доступ: Універсальний доступ
Програма:
Не працювати в цій програмі
Гра — AURA на паузі
Мова для цієї програми
Без прив'язки
Винятки
Не працювати в (останні програми)
Прив'язки мов
Порожньо
Запускати під час входу
Мої слова…
AURA Switcher — мої слова
Ці слова AURA Switcher вважає правильними: не змінює їх, а набрані не в тій розкладці — виправляє на них. Через кому.
Зберегти
Скасувати
Мова меню
Системна
Подвійний ⇧ — змінити мову слова/виділення
Повідомити про проблему…
Що сталося і в якій програмі:
Перевірити оновлення…
⬆︎ Можливо, вийшло оновлення — перевірити
Підтримати AURA Switcher ☕
Вихід

pl Polski
Włączone
Autokorekta
Dźwięk
⚠︎ Nadaj dostęp: Dostępność
Aplikacja:
Nie działaj w tej aplikacji
Gra — AURA wstrzymana
Język dla tej aplikacji
Bez przypisania
Wyjątki
Nie działaj w (ostatnie aplikacje)
Przypisania języków
Pusto
Uruchamiaj przy logowaniu
Moje słowa…
AURA Switcher — moje słowa
AURA Switcher uznaje te słowa za poprawne: nigdy ich nie zmienia, a wpisane w złym układzie poprawia na nie. Oddziel je przecinkami.
Zapisz
Anuluj
Język menu
Systemowy
Podwójny ⇧ — zmień układ słowa/zaznaczenia
Zgłoś problem…
Co się stało i w jakiej aplikacji:
Sprawdź aktualizacje…
⬆︎ Może być dostępna aktualizacja — sprawdź
Wesprzyj AURA Switcher ☕
Zakończ

de Deutsch
Aktiviert
Autokorrektur
Ton
⚠︎ Zugriff erlauben: Bedienungshilfen
App:
In dieser App nicht aktiv
Spiel — AURA pausiert
Sprache für diese App
Keine Zuordnung
Ausnahmen
Nicht aktiv in (letzte Apps)
Sprachzuordnungen
Leer
Bei Anmeldung starten
Meine Wörter…
AURA Switcher — meine Wörter
AURA Switcher hält diese Wörter für richtig: ändert sie nie und korrigiert sie, wenn sie im falschen Layout getippt wurden. Durch Kommas trennen.
Sichern
Abbrechen
Menüsprache
System
Doppel-⇧ — Wort/Auswahl umwandeln
Problem melden…
Was ist passiert und in welcher App:
Nach Updates suchen…
⬆︎ Möglicherweise gibt es ein Update — prüfen
AURA Switcher unterstützen ☕
Beenden

es Español
Activado
Autocorrección
Sonido
⚠︎ Conceder acceso: Accesibilidad
App:
No funcionar en esta app
Juego — AURA en pausa
Idioma para esta app
Sin asignación
Excepciones
No funcionar en (apps recientes)
Idiomas asignados
Vacío
Abrir al iniciar sesión
Mis palabras…
AURA Switcher — mis palabras
AURA Switcher considera correctas estas palabras: nunca las cambia y las corrige si se escriben con la distribución equivocada. Sepáralas con comas.
Guardar
Cancelar
Idioma del menú
Sistema
Doble ⇧ — convertir palabra/selección
Informar de un problema…
Qué pasó y en qué app:
Buscar actualizaciones…
⬆︎ Puede haber una actualización — comprobar
Apoyar AURA Switcher ☕
Salir

fr Français
Activé
Correction automatique
Son
⚠︎ Autoriser l'accès : Accessibilité
App :
Ne pas fonctionner dans cette app
Jeu — AURA en pause
Langue pour cette app
Aucune association
Exceptions
Ne pas fonctionner dans (apps récentes)
Langues associées
Vide
Ouvrir à la connexion
Mes mots…
AURA Switcher — mes mots
AURA Switcher considère ces mots comme corrects : il ne les modifie jamais et les corrige s'ils sont tapés avec la mauvaise disposition. Séparez-les par des virgules.
Enregistrer
Annuler
Langue du menu
Système
Double ⇧ — convertir le mot/la sélection
Signaler un problème…
Ce qui s'est passé et dans quelle app :
Rechercher des mises à jour…
⬆︎ Une mise à jour est peut-être disponible — vérifier
Soutenir AURA Switcher ☕
Quitter

it Italiano
Attivo
Correzione automatica
Suono
⚠︎ Concedi accesso: Accessibilità
App:
Non funzionare in questa app
Gioco — AURA in pausa
Lingua per questa app
Nessuna associazione
Eccezioni
Non funzionare in (app recenti)
Lingue associate
Vuoto
Apri al login
Le mie parole…
AURA Switcher — le mie parole
AURA Switcher considera corrette queste parole: non le cambia mai e le corregge se digitate con il layout sbagliato. Separale con virgole.
Salva
Annulla
Lingua del menu
Sistema
Doppio ⇧ — converti parola/selezione
Segnala un problema…
Cosa è successo e in quale app:
Controlla aggiornamenti…
⬆︎ Potrebbe esserci un aggiornamento — controlla
Sostieni AURA Switcher ☕
Esci

pt Português
Ativado
Correção automática
Som
⚠︎ Conceder acesso: Acessibilidade
App:
Não funcionar nesta app
Jogo — AURA em pausa
Idioma para esta app
Sem associação
Exceções
Não funcionar em (apps recentes)
Idiomas associados
Vazio
Abrir ao iniciar sessão
As minhas palavras…
AURA Switcher — as minhas palavras
O AURA Switcher considera estas palavras corretas: nunca as altera e corrige-as se forem digitadas no layout errado. Separe-as com vírgulas.
Guardar
Cancelar
Idioma do menu
Sistema
Duplo ⇧ — converter palavra/seleção
Comunicar um problema…
O que aconteceu e em que app:
Procurar atualizações…
⬆︎ Pode haver uma atualização — verificar
Apoiar o AURA Switcher ☕
Sair

tr Türkçe
Etkin
Otomatik düzeltme
Ses
⚠︎ Erişim izni verin: Erişilebilirlik
Uygulama:
Bu uygulamada çalışma
Oyun — AURA duraklatıldı
Bu uygulama için dil
Atama yok
İstisnalar
Şurada çalışma (son uygulamalar)
Dil atamaları
Boş
Oturum açılışında başlat
Kelimelerim…
AURA Switcher — kelimelerim
AURA Switcher bu kelimeleri doğru kabul eder: asla değiştirmez, yanlış düzende yazılırsa onlara düzeltir. Virgülle ayırın.
Kaydet
İptal
Menü dili
Sistem
Çift ⇧ — kelimeyi/seçimi dönüştür
Sorun bildir…
Ne oldu ve hangi uygulamada:
Güncellemeleri denetle…
⬆︎ Güncelleme olabilir — denetle
AURA Switcher'ı destekle ☕
Çık

nl Nederlands
Ingeschakeld
Autocorrectie
Geluid
⚠︎ Geef toegang: Toegankelijkheid
App:
Niet werken in deze app
Game — AURA gepauzeerd
Taal voor deze app
Geen koppeling
Uitzonderingen
Niet werken in (recente apps)
Taalkoppelingen
Leeg
Starten bij inloggen
Mijn woorden…
AURA Switcher — mijn woorden
AURA Switcher beschouwt deze woorden als juist: verandert ze nooit en verbetert ze als ze in de verkeerde indeling zijn getypt. Scheid ze met komma's.
Bewaar
Annuleer
Menutaal
Systeem
Dubbel ⇧ — woord/selectie omzetten
Probleem melden…
Wat er gebeurde en in welke app:
Zoek naar updates…
⬆︎ Er is misschien een update — controleren
Steun AURA Switcher ☕
Stop

cs Čeština
Zapnuto
Automatické opravy
Zvuk
⚠︎ Udělte přístup: Zpřístupnění
Aplikace:
Nefungovat v této aplikaci
Hra — AURA pozastavena
Jazyk pro tuto aplikaci
Bez přiřazení
Výjimky
Nefungovat v (nedávné aplikace)
Přiřazení jazyků
Prázdné
Spouštět po přihlášení
Moje slova…
AURA Switcher — moje slova
AURA Switcher považuje tato slova za správná: nikdy je nemění a opraví je, když jsou napsána ve špatném rozložení. Oddělte je čárkami.
Uložit
Zrušit
Jazyk nabídky
Systémový
Dvojitý ⇧ — převést slovo/výběr
Nahlásit problém…
Co se stalo a v jaké aplikaci:
Zkontrolovat aktualizace…
⬆︎ Možná je k dispozici aktualizace — zkontrolovat
Podpořit AURA Switcher ☕
Ukončit

sv Svenska
Aktiverad
Autokorrigering
Ljud
⚠︎ Ge åtkomst: Hjälpmedel
App:
Arbeta inte i den här appen
Spel — AURA pausad
Språk för den här appen
Ingen koppling
Undantag
Arbeta inte i (senaste appar)
Språkkopplingar
Tomt
Starta vid inloggning
Mina ord…
AURA Switcher — mina ord
AURA Switcher ser dessa ord som rätt: ändrar dem aldrig och rättar dem om de skrivs med fel layout. Separera med kommatecken.
Spara
Avbryt
Menyspråk
System
Dubbel-⇧ — konvertera ord/markering
Rapportera ett problem…
Vad hände och i vilken app:
Sök efter uppdateringar…
⬆︎ Det kan finnas en uppdatering — kontrollera
Stöd AURA Switcher ☕
Avsluta

fi Suomi
Käytössä
Automaattinen korjaus
Ääni
⚠︎ Anna käyttöoikeus: Käyttöapu
Ohjelma:
Älä toimi tässä ohjelmassa
Peli — AURA tauolla
Kieli tälle ohjelmalle
Ei liitosta
Poikkeukset
Älä toimi ohjelmassa (viimeisimmät)
Kieliliitokset
Tyhjä
Käynnistä kirjautuessa
Omat sanat…
AURA Switcher — omat sanat
AURA Switcher pitää näitä sanoja oikeina: ei koskaan muuta niitä ja korjaa ne, jos ne on kirjoitettu väärällä asettelulla. Erota pilkuilla.
Tallenna
Kumoa
Valikon kieli
Järjestelmä
Kaksois-⇧ — muunna sana/valinta
Ilmoita ongelmasta…
Mitä tapahtui ja missä ohjelmassa:
Tarkista päivitykset…
⬆︎ Päivitys saattaa olla saatavilla — tarkista
Tue AURA Switcheriä ☕
Lopeta

ro Română
Activat
Corectare automată
Sunet
⚠︎ Acordați acces: Accesibilitate
Aplicație:
Nu funcționa în această aplicație
Joc — AURA în pauză
Limba pentru această aplicație
Fără asociere
Excepții
Nu funcționa în (aplicații recente)
Limbi asociate
Gol
Pornește la autentificare
Cuvintele mele…
AURA Switcher — cuvintele mele
AURA Switcher consideră aceste cuvinte corecte: nu le schimbă niciodată și le corectează dacă sunt tastate în aranjamentul greșit. Separați-le prin virgulă.
Salvează
Anulează
Limba meniului
Sistem
Dublu ⇧ — convertește cuvântul/selecția
Raportează o problemă…
Ce s-a întâmplat și în ce aplicație:
Caută actualizări…
⬆︎ Poate există o actualizare — verifică
Susține AURA Switcher ☕
Ieșire

hu Magyar
Bekapcsolva
Automatikus javítás
Hang
⚠︎ Hozzáférés megadása: Kisegítő lehetőségek
Alkalmazás:
Ne működjön ebben az alkalmazásban
Játék — AURA szüneteltetve
Nyelv ehhez az alkalmazáshoz
Nincs hozzárendelés
Kivételek
Ne működjön itt (legutóbbi alkalmazások)
Nyelvi hozzárendelések
Üres
Indítás bejelentkezéskor
Saját szavak…
AURA Switcher — saját szavak
Az AURA Switcher ezeket a szavakat helyesnek tekinti: soha nem módosítja őket, és kijavítja, ha rossz kiosztással gépelték. Vesszővel válassza el.
Mentés
Mégse
Menü nyelve
Rendszer
Dupla ⇧ — szó/kijelölés átalakítása
Probléma bejelentése…
Mi történt és melyik alkalmazásban:
Frissítések keresése…
⬆︎ Lehet, hogy van frissítés — ellenőrzés
Az AURA Switcher támogatása ☕
Kilépés

el Ελληνικά
Ενεργό
Αυτόματη διόρθωση
Ήχος
⚠︎ Δώστε πρόσβαση: Προσβασιμότητα
Εφαρμογή:
Να μη λειτουργεί σε αυτή την εφαρμογή
Παιχνίδι — AURA σε παύση
Γλώσσα για αυτή την εφαρμογή
Χωρίς αντιστοίχιση
Εξαιρέσεις
Να μη λειτουργεί σε (πρόσφατες εφαρμογές)
Αντιστοιχίσεις γλωσσών
Κενό
Εκκίνηση κατά τη σύνδεση
Οι λέξεις μου…
AURA Switcher — οι λέξεις μου
Το AURA Switcher θεωρεί σωστές αυτές τις λέξεις: δεν τις αλλάζει ποτέ και τις διορθώνει όταν πληκτρολογηθούν με λάθος διάταξη. Χωρίστε τις με κόμμα.
Αποθήκευση
Ακύρωση
Γλώσσα μενού
Συστήματος
Διπλό ⇧ — μετατροπή λέξης/επιλογής
Αναφορά προβλήματος…
Τι συνέβη και σε ποια εφαρμογή:
Έλεγχος για ενημερώσεις…
⬆︎ Ίσως υπάρχει ενημέρωση — έλεγχος
Υποστηρίξτε το AURA Switcher ☕
Έξοδος

bg Български
Включено
Автокорекция
Звук
⚠︎ Дайте достъп: Достъпност
Програма:
Да не работи в тази програма
Игра — AURA е на пауза
Език за тази програма
Без обвързване
Изключения
Да не работи в (последни програми)
Обвързани езици
Празно
Стартиране при вход
Моите думи…
AURA Switcher — моите думи
AURA Switcher смята тези думи за правилни: никога не ги променя и ги поправя, ако са написани с грешната подредба. Разделете ги със запетая.
Запази
Отказ
Език на менюто
Системен
Двоен ⇧ — смяна на езика на дума/селекция
Съобщете за проблем…
Какво се случи и в коя програма:
Проверка за актуализации…
⬆︎ Може да има актуализация — проверете
Подкрепете AURA Switcher ☕
Изход

he עברית
מופעל
תיקון אוטומטי
צליל
⚠︎ תנו גישה: נגישות
יישום:
לא לפעול ביישום זה
משחק — AURA מושהית
שפה ליישום זה
ללא שיוך
חריגים
לא לפעול ב (יישומים אחרונים)
שיוכי שפה
ריק
הפעלה בעת התחברות
המילים שלי…
AURA Switcher — המילים שלי
AURA Switcher מתייחס למילים אלה כנכונות: לעולם לא משנה אותן, ומתקן אליהן כשהן מוקלדות בפריסה הלא נכונה. הפרידו בפסיקים.
שמירה
ביטול
שפת התפריט
מערכת
⇧ כפול — המרת מילה/בחירה
דיווח על בעיה…
מה קרה ובאיזה יישום:
בדיקת עדכונים…
⬆︎ ייתכן שיש עדכון — בדיקה
תמכו ב-AURA Switcher ☕
יציאה

ar العربية
مفعّل
التصحيح التلقائي
الصوت
⚠︎ امنح الوصول: تسهيلات الاستخدام
التطبيق:
لا تعمل في هذا التطبيق
لعبة — AURA متوقف مؤقتًا
لغة هذا التطبيق
بدون ربط
الاستثناءات
لا تعمل في (التطبيقات الأخيرة)
ربط اللغات
فارغ
التشغيل عند تسجيل الدخول
كلماتي…
AURA Switcher — كلماتي
يعدّ AURA Switcher هذه الكلمات صحيحة: لا يغيّرها أبدًا، ويصحّحها إليها إذا كُتبت بالتخطيط الخطأ. افصل بينها بفواصل.
حفظ
إلغاء
لغة القائمة
النظام
⇧ مزدوج — تحويل الكلمة/التحديد
الإبلاغ عن مشكلة…
ماذا حدث وفي أي تطبيق:
التحقق من التحديثات…
⬆︎ قد يتوفر تحديث — تحقّق
ادعم AURA Switcher ☕
إنهاء

hi हिन्दी
चालू
स्वतः सुधार
ध्वनि
⚠︎ अनुमति दें: सुलभता
ऐप:
इस ऐप में काम न करें
गेम — AURA रुका हुआ
इस ऐप की भाषा
कोई बंधन नहीं
अपवाद
इनमें काम न करें (हाल के ऐप)
भाषा बंधन
खाली
लॉगिन पर शुरू करें
मेरे शब्द…
AURA Switcher — मेरे शब्द
AURA Switcher इन शब्दों को सही मानता है: इन्हें कभी नहीं बदलता, और गलत लेआउट में टाइप होने पर इन्हीं में सुधार देता है। अल्पविराम से अलग करें।
सहेजें
रद्द करें
मेनू की भाषा
सिस्टम
दो बार ⇧ — शब्द/चयन बदलें
समस्या बताएँ…
क्या हुआ और किस ऐप में:
अपडेट जाँचें…
⬆︎ शायद नया अपडेट आया है — जाँचें
AURA Switcher का समर्थन करें ☕
बंद करें

ko 한국어
켜기
자동 수정
소리
⚠︎ 접근 권한 허용: 손쉬운 사용
앱:
이 앱에서 작동 안 함
게임 — AURA 일시 중지됨
이 앱의 언어
지정 안 함
예외
작동 안 함 (최근 앱)
언어 지정
비어 있음
로그인 시 실행
내 단어…
AURA Switcher — 내 단어
AURA Switcher는 이 단어들을 올바른 단어로 봅니다. 절대 바꾸지 않고, 잘못된 자판으로 입력되면 이 단어로 고칩니다. 쉼표로 구분하세요.
저장
취소
메뉴 언어
시스템
⇧ 두 번 — 단어/선택 영역 변환
문제 신고…
무슨 일이 어느 앱에서 있었나요:
업데이트 확인…
⬆︎ 업데이트가 있을 수 있습니다 — 확인
AURA Switcher 후원하기 ☕
종료
"""

langs = []  # (code, name, [strings])
for block in LANGS.strip().split("\n\n"):
    head, *lines = block.split("\n")
    code, name = head.split(" ", 1)
    assert len(lines) == len(KEYS), (code, len(lines))
    lines[KEYS.index("app")] += " "  # "App: " + app name
    langs.append((code, name, lines))

def esc(s): return s.replace("\\", "\\\\").replace('"', '\\"')

def put(path, begin, end, body):
    p = ROOT / path; s = p.read_text()
    s2, n = re.subn(re.escape(begin) + r".*?" + re.escape(end), lambda _: begin + "\n" + body + end, s, flags=re.S)
    assert n == 1, path
    p.write_text(s2)

B, E = "// BEGIN menu strings — generated by tools/menu_i18n.py, edit there", "// END menu strings"
swift = "let uiLangs = [" + ", ".join(f'"{c}"' for c, _, _ in langs) + "]\n"
swift += "let uiLangNames = [" + ", ".join(f'"{n}"' for _, n, _ in langs) + "]\n"
swift += "let uiStrings: [String: [String]] = [ // key: one string per uiLangs\n"
for i, k in enumerate(KEYS):
    swift += f'    "{k}": [' + ", ".join(f'"{esc(l[i])}"' for _, _, l in langs) + "],\n"
swift += "]\n"
put("main.swift", B, E, swift)

cpp = f"static const int UI_N = {len(langs)};\n"
cpp += "static const wchar_t* const UI_LANGS[UI_N] = {" + ", ".join(f'L"{c}"' for c, _, _ in langs) + "};\n"
cpp += "static const wchar_t* const UI_NAMES[UI_N] = {" + ", ".join(f'L"{n}"' for _, n, _ in langs) + "};\n"
cpp += "static const wchar_t* const UI_STR[][UI_N] = { // row: English first, then the other UI_LANGS\n"
for i, k in enumerate(KEYS):
    cpp += "    {" + ", ".join(f'L"{esc(l[i])}"' for _, _, l in langs) + "},\n"
cpp += "};\n"
put("windows/aura.cpp", B, E, cpp)
print(f"{len(langs)} languages × {len(KEYS)} strings")
