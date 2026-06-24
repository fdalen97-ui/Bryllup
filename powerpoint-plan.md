# PowerPoint-plan – visuell ryggrad gjennom kvelden

PowerPoint brukes som **visuell støtte** for toastmasterens monolog – ikke
som hovedinnhold. Slides driver rytme, gir gjestene noe å se på i
overgangene, og sikrer at fellessang/Fireball-momenter blir tydelige.

**Hovedprinsipp**: Fredrik leverer ordene. PowerPoint forsterker. Hvis
PowerPoint krasjer, skal kvelden gå videre uten at noen merker det.

---

## 1. Teknisk oppsett

### 1.1 Anbefalt arkitektur

```
[Laptop] --HDMI--> [Projektor / TV på Maarud]
   ^
   |
[Klikker (USB-mottaker i laptop)]
   ^
   |
[Klikker-person sitter ved laptop]
```

- **Laptop**: Fredriks egen, eller låne fra venn. Sjekk HDMI-port.
- **Klikker**: trådløs presenter (se `utstyr.md`).
- **Klikker-person**: én navngitt venn som sitter ved laptopen og bytter
  slide på Fredriks signal (nikk eller håndtegn).
- **Musikk**: kjøres separat av Simen (lydtekniker) – **ikke** embedded i PowerPoint.

### 1.2 Hvorfor musikk skal være separat

PowerPoint + embedded lyd er notorisk skjørt:
- Codec-feil hvis filen flyttes mellom maskiner
- Volum kan ikke styres fra DJ-mikser
- Hvis slides krasjer, mister du musikken også
- Auto-spill ved slide-skift er upresist (lag på 0.5–2 sek)

**Løsning**: Simen har egen musikkliste (cue-liste i `simen-lyd.md`,
basert på `musikkplan.md`). Fredrik nikker = Simen fader inn musikken.
Slide bytter parallelt, men er ikke avhengig av musikken.

**Unntak**: korte jingler (Fireball, F1-nedtelling) kan være embedded hvis
de er max 10 sek og testet flere ganger.

---

## 2. Slide-struktur

| # | Tittel | Innhold | Når vises | Klikk-cue |
|---|--------|---------|-----------|-----------|
| 1 | Velkommen | «Michelle & Anders – 26. juni 2026» + bilde | Mens gjester tar plass (17:00–17:15) | Auto |
| 2 | Stikk 1 åpner | Sort slide (lar Fredrik være i fokus) | Når Fredrik begynner åpning | Klikk |
| 3 | Kveldens program | Liste: 11 taler, 3 retter, 2 pauser | Under «Her er kveldens plan...» | Klikk |
| 4 | Spilleregler | Tramping, klirring, nødutgang | Når Fredrik nevner det | Klikk |
| 5 | Trigger-shot | «Equinor» / «pitch deck» = drikk | Når regelen annonseres | Klikk |
| 6 | FF-jentene presenterer maten | «Feminin og fornem presenterer forretten» (Oda-rollen avklares) | Rett etter Werners tale, før forrett serveres | Klikk |
| 6b | F1 / Rumble-slide | Startflagg-bilde | Rett før brudeparet entrer | Klikk |
| 7 | Brudeparet entrer | Bilde av Michelle & Anders | Mens de går inn | Klikk |
| 8 | Tale 1 – Werner | Bilde + «Werner Seigerud, brudens far» | 5 sek før Werner reiser seg (FØR mat) | Klikk |
| 9 | Tale 2 – Anders til Michelle | Bilde + «Anders – brudgommen» | Før Anders reiser seg | Klikk |
| 10 | Tale 3 – Michelle (brudens tale) | Bilde + «Michelle, bruden» | Etter Anders' tale | Klikk |
| 11 | Helan går – tekst | Hele første vers, stor font | Etter de tre talene | Klikk |
| 12 | 🔥 FIREBALL RUNDE 1 | Stor brann-grafikk | Etter forretten (første servering) | Klikk |
| 13 | Tale 4 – Kjersti + Erik Nilsen | Bilde + «Anders' foreldre» | Under forrett, før de reiser seg | Klikk |
| 14 | Pause 1 | «10–15 min – strekk beina» + nedteller | Pausen før hovedrett | Klikk |
| 15 | Stikk 2 åpner | Sort slide | Etter buffet 2, når Fredrik begynner | Klikk |
| 16 | Tale 5 – Helene | Bilde + «Helene, Michelles forlover» | Før hun reiser seg | Klikk |
| 17 | ⚡ THUNDERSTRUCK | AC/DC-stilig grafikk + «Hver "thunder" = drikk» | Før Even-intro | Klikk |
| 18 | Tale 6 – Even | Bilde + «Even, Anders' forlover» | Etter Thunderstruck-flaska | Klikk |
| 19 | Tale 7 – Cathrine + Anette | Bilde av begge + «Michelles storesøstre» | Før de reiser seg | Klikk |
| 20 | Tale 8 – Ingrid + Ola | Bilde av begge + «Anders' søsken» | Før de reiser seg | Klikk |
| 21 | Pause 2 | «20 min – kaffe + Fireball» | Pausen | Klikk |
| 22 | 🔥 FIREBALL RUNDE 2 | Brann-grafikk | Etter hovedrett | Klikk |
| 23 | Stikk 3 åpner | Sort slide | Når Fredrik begynner | Klikk |
| 24 | Tale 9 – Kongsvinger-vennene | Bilde av gruppe + «Michelles barndomsvenner» | Før de reiser seg | Klikk |
| 25 | Tale 10 – «Feminin og fornem» | Bilde av gruppe + «Michelles Ås-gjeng (NMBU)» | Før de reiser seg | Klikk |
| 26 | Innslag – Broderskapet Unity | Bilde av gruppe + «Anders' Ås-vennegjeng» | Før de starter | Klikk |
| 27 | Tale 11 – Tom Christian | Bilde + «Tom Christian, venn av Anders – kveldens siste tale» | Før han reiser seg | Klikk |
| 28 | Stikk 4 åpner | Sort slide | Når Fredrik begynner | Klikk |
| 29–38 | Take on Me-påstander | Én påstand per slide, stor font | Sangen rulles, klikk hvert 15 sek | Klikk |
| 39 | We Didn't Start the Fire | Refrengtekst + skjelett | Hvis innslaget kjøres | Klikk |
| 40 | Takk for maten | «Tusen takk til kjøkkenet» | Avslutning | Klikk |
| 41 | 🔥 FIREBALL RUNDE 3 | Brann-grafikk | Etter dessert (før venne-talene) | Klikk |
| 42 | Dansegulvet åpnes | «Michelle & Anders – første dans» | Inn til dans | Klikk |
| 43 | Reserve | Sort slide | Hvis noe trekker ut | Klikk |

---

## 3. Designprinsipper

### 3.1 Lesbarhet fra bakerste bord

- **Bakgrunn**: mørk (sort eller mørk grå). Lyst rom = projektor blir
  vasket ut, mørk slide gir kontrast.
- **Font**: hvit eller lys gul, sans-serif (Helvetica, Arial, Inter).
- **Fontstørrelse**: minimum 60 pt for tekst som skal leses fra benkrad.
  Sang-tekst: 80 pt+.
- **Maks ord per slide**: 8. Sang-vers er unntak.

### 3.2 Bilder

- Alle taler-slides får ett portrettbilde.
- Få bildene fra brudeparet eller direkte fra talerne (sjekk samtykke).
- Sentrert, fyller halvparten av skjermen.
- Navn under bildet, relasjon til brudeparet under det igjen.

### 3.3 Konsistent layout

Bruk én mal for alle taler-slides:

```
┌─────────────────────────────────┐
│                                 │
│         [Bilde sentrert]        │
│                                 │
│         FORNAVN ETTERNAVN       │
│      Brudens far / forlover...  │
│                                 │
└─────────────────────────────────┘
```

Bytter du layout midt i kvelden, bryter du rytmen.

---

## 4. Sort slide som verktøy

Sort slide = ingen tekst, ingen bilder. Bruk når:
- Fredrik snakker langt og vil ha all oppmerksomhet
- Stillhet skal lande (etter en emosjonell tale)
- Du må «pause» visuelt mens noe annet skjer

Tildel **B-tasten** på klikkeren = blank skjerm. (Standard PowerPoint-shortcut.)
Klikker-person trenger å vite dette.

---

## 5. Backup-plan – hvis PowerPoint krasjer

Risiko: laptop fryser, projektor mister signal, klikker dør.

**Tre nivåer**:

1. **Slide-feil**: klikker-person trykker `Esc` → `F5` → starter på siste
   slide. Fredrik fyller med en setning: *«Mens vi venter på at maskinen
   skal følge med...»*
2. **Total PowerPoint-krasj**: Fredrik fortsetter uten visuell støtte.
   Sang-tekst printes ut som backup (10 ark – Helan går, Take on Me,
   Vi e fra Norge).
3. **Projektor dør**: gå over til kun stemme. Drop fellessang-arkene.

**Forhåndsregel**: ha PowerPoint åpen på **to maskiner** under middagen.
Sekundær laptop ved bordet til klikker-person, ikke koblet til projektor
men klar som backup.

---

## 6. Generalprøve – obligatorisk

**Når**: dagen før bryllupet, eller morgenen samme dag på Maarud.

**Hvem**: Fredrik + klikker-person + Simen (lydtekniker).

**Sjekkliste**:
- [ ] Slide 1 til 43 spiller gjennom uten feil
- [ ] Klikker rekker fra Fredriks plassering til laptopen
- [ ] Lyd fra anlegget testet på alle Fireball-jingler
- [ ] Fredrik øver Thunderstruck-cue + Fireball-cue mot Simen
- [ ] B-tast (sort skjerm) testet
- [ ] Backup-laptop testet
- [ ] Sangtekst-ark printet og lagt klar

---

## 7. Filhåndtering

- Lagre PowerPoint som **.pptx** på laptopen lokalt.
- Lagre én kopi på USB-stick.
- Lagre én kopi i skyen (Google Drive / OneDrive) som siste backup.
- Eksporter også til **PDF** – kan vises i hvilken som helst PDF-leser
  hvis PowerPoint ikke åpner.
- Filnavn: `bryllup-Michelle-Anders-2026-06-26-vFINAL.pptx`.

---

## 8. Avklares før bryllupet

- [ ] Maarud Gård: projektor / TV-skjerm tilgjengelig?
- [ ] HDMI-kabel lengde – rekker fra laptop-plass til projektor?
- [ ] Strømuttak ved klikker-bordet
- [ ] Hvem er klikker-person? (helst en venn, ikke en taler)
- [ ] Bilder samlet inn fra alle 11 taler + 1 innslag senest 2 uker før
- [ ] Generalprøve booket
