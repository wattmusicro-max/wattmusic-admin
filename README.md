# wattmusic-admin

Codul paginii de admin **wattmusic.ro/trupa-mea-admin** (WATT Music · Admin), împărțit pe module.

Aici e **doar cod**. Datele (oferte, contracte, plăți, lead-uri, CNP-uri) stau în baza de date Supabase,
accesibilă numai după login în admin. Nu pune niciodată date de clienți în acest depozit — e public.

## Cum e organizat

| Folder | Ce era în Elementor | Ce conține |
|---|---|---|
| `src/admin/` | widgetul HTML `tm0admw` | baza adminului (login, taburi, paginile mirilor), social media, KPI, Asociate, Deal trupe |
| `src/oferte/` | widgetul HTML `tm0ofradm` | ofertele și tot ce ține de ele: WhatsApp, întâlniri, disponibilitate, pipeline, statistici, descalificați, calendar & lead-uri, contracte semnate, backup |

Fiecare fișier `NN-nume.html` e un modul (stil + markup + script). Ordinea în care se lipesc e în `ORDINE.txt`
din fiecare folder — contează, unele module se bazează pe cele dinainte.

### Module – admin (`src/admin`)
- `00-baza` – stilul general, structura paginii, login, taburile, paginile mirilor, Ask Mada, invitații Trupa Mea
- `10-tm-names` – nume afișate pentru tour manageri
- `20-social-vz` – tabul Social media + mutarea „Discuții cu potențial” în tabul lui
- `30-social-snap` – instantaneu cu postările din social media
- `40-kpi` – Statistici & KPI
- `50-asociate`, `51-asociate-ui`, `52-asociate-sold` – Asociate (criptat cu parolă), interfața și soldul
- `60-deal-trupe` – Deal trupe

### Module – oferte (`src/oferte`)
- `00-anti-salt` – ascunde blocurile până ajung în tabul lor (fără salturi la încărcare)
- `01-oferte-baza` – lista de oferte + formularul de ofertă nouă
- `02-prefill` – completare formular din link
- `03-busy-data` – `WM_BUSY`: zilele ocupate per trupă (public, doar „ocupat”, fără nume de clienți)
- `04-libere-whatsapp` – trupe libere la dată + trimitere pe WhatsApp
- `05-trupa-mea-acces` – retrimite accesul Trupa Mea
- `06-editare`, `07-prelungire`, `08-cautare` – modifică / prelungește / caută oferte
- `09-intalniri`, `10-intalniri-panou` – invitații la întâlnire și panoul întâlnirilor
- `11-disponibilitate` – tabelul de disponibilitate trupe
- `12-pipeline` – Discuții cu potențial mare de semnare
- `13-statistici` – statistici lunare reclame → contracte
- `14-verificare-data`, `15-verificare-locatie` – validări în formular
- `16-descalificati` – clienți descalificați
- `17-calendar-leaduri` – Calendar & contracte + Lead-uri (mutate din WattMusic Booking)
- `18-contracte-semnate` – tabul Contracte semnate (documente Drive + bani)
- `19-whatsapp-web` – pe laptop deschide WhatsApp Web direct (emoji corecte)
- `20-backup-zilnic` – backup zilnic al datelor în Drive (scriptul Google „WattMusic Backup Admin”)

## Cum se publică o modificare

1. Modifici modulul din `src/…`.
2. `python3 tools/build.py` → refă `dist/tm0admw.html` și `dist/tm0ofradm.html` și afișează amprenta SHA-256.
3. Commit + push, apoi tag de versiune (`v1.0.1` etc.).
4. Pagina încarcă `dist/` prin jsDelivr la versiunea fixată în widgetul din Elementor.
   Revenire la o versiune veche = schimbi numărul versiunii în widget.

## Siguranță
- Backup zilnic al datelor + al codului paginii: Drive → „WattMusic – Backup admin (privat)”.
- `dist/` la tag-ul `v1.0.0` e identic, byte cu byte, cu ce era în Elementor pe 11.11.2026.

## Încărcătorul din Elementor (`loader/`)
- Widgetul `tm0admw` conține `loader/elementor-tm0admw.html` cu `__VERSIUNE__` înlocuit de codul commit-ului publicat.
  El descarcă `dist/tm0admw.html` și `dist/tm0ofradm.html` (jsDelivr, cu rezervă raw.githubusercontent.com)
  și le pune în pagină în ordine: întâi adminul, apoi ofertele.
- Widgetul `tm0ofradm` conține doar `loader/elementor-tm0ofradm.html` (locul unde intră ofertele).
- Versiunea încărcată se vede în consolă: `WM_ADMIN_VERSION`.
- Codul vechi, întreg, rămâne în `dist/` la commit-ul `de4d202` și în backupurile din Drive.
