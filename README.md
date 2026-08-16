# Analiza dostępności przestrzennej szkół podstawowych w Gminie i Mieście Chojnice

## O projekcie
Celem projektu było zbadanie dostępności pieszej do placówek oświatowych w Gminie i Mieście Chojnice oraz identyfikacja obszarów wykluczenia transportowego (> 3000 m od najbliższej szkoły).

## Narzędzia i Metodologia
* **Oprogramowanie:** QGIS 3.40.12
* **Analizy sieciowe:**
  * `ORS Tools` – wyznaczenie izochron dojścia (3 km) wzdłuż sieci drogowej.
  * `QNEAT3` – kalkulacja macierzy kosztów (OD Matrix) z centroidów budynków do placówek szkolnych po sieci OSM.
* **Źródła danych:** OpenStreetMap, BDOT10k, PRG, QuickOSM.

## Wykonane kroki
1. Zebranie danych informacji publicznej Gminy i Miasta Chojnice
2. Pobranie mapy podkładowej z OpenStreetMap i QuickOSM
3. Wygenerowanie centroidów dla geometrii budynków mieszkalnych.
4. Przypisanie budynków do najbliższych szkół na podstawie najkrótszego dystansu drogowego (`total_cost`).
5. Analiza izochron zasięgu 3000 m od szkół.
6. Wyznaczenie stref wykluczenia oraz opracowanie kompozycji kartograficznej z wycinkami analitycznymi (Inset Maps).

![Mapa optymalnej sieci szkół](<Analiza dostępności przestrzennej szkół w Gminie i Mieście Chojnice.png>)
---
*Autor: Jakub Knitter*  
*Data: 2026*
