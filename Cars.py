#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests

adresse = "Paradisæblevej"
husnr = "74"
postnr = "2500"

url = f"https://api.dataforsyningen.dk/adresser?vejnavn={adresse}&husnr={husnr}&postnr={postnr}"
response = requests.get(url)
adresser = response.json()

første_adresse = adresser[0]
adgangsadresse = første_adresse["adgangsadresse"]
adgangspunkt = adgangsadresse["adgangspunkt"]

adressebetegnelse = første_adresse["adressebetegnelse"]
kommune_navn = adgangsadresse["kommune"]["navn"]
postnummer = adgangsadresse["postnummer"]["nr"]
postdistrikt = adgangsadresse["postnummer"]["navn"]
koordinater = adgangspunkt["koordinater"]
opstillingskreds = adgangsadresse["opstillingskreds"]["navn"]
afstemningsomraade = adgangsadresse["afstemningsområde"]["navn"]
storkreds = adgangsadresse["storkreds"]["navn"]
valglandsdel = adgangsadresse["valglandsdel"]["navn"]

print("Adresse:", adressebetegnelse)
print("Kommune:", kommune_navn)
print("Postnummer:", postnummer, postdistrikt)
print("Koordinater (lon, lat):", koordinater)
print("Opstillingskreds:", opstillingskreds)
print("Afstemningsområde:", afstemningsomraade)
print("Storkreds:", storkreds)
print("Valglandsdel:", valglandsdel)



valgtdata = pd.read_csv(
    "Folketingsvalg_2026_8. Syd_05-05-2026 11.13.47.csv",
    sep=";",
    encoding="utf-8"
)

valgdataGruppet = valgtdata.groupby("Partinavn").agg(
    Antal_stemmer = ("Stemmeatal", "count"))
