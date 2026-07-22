#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from vbts import VBTS
from export import Export
from bist import BIST


def main():

    print("=" * 60)
    print(" TradingView WatchList Generator")
    print("=" * 60)

    #---------------------------------------------------
    # Veri Kaynakları
    #---------------------------------------------------

    vbts = VBTS()
    vbts.load()

    bist = BIST()

    all_symbols = set(bist.get_symbols())

    #---------------------------------------------------
    # Tedbir Listeleri
    #---------------------------------------------------

    brut = vbts.brut()

    kredi = vbts.kredi()

    aciga = vbts.aciga()

    emir = vbts.emir()

    tek_fiyat = vbts.tek_fiyat()

    internet = vbts.internet()

    depo = vbts.depo()

    vbts_all = vbts.all()

    #---------------------------------------------------
    # Alt Pazar
    #---------------------------------------------------

    alt_pazar = bist.get_alt_pazar()

    #---------------------------------------------------
    # Ana Trade Listesi
    #---------------------------------------------------

    trade_list = (
        all_symbols
        - alt_pazar
        - brut
    )

    #---------------------------------------------------
    # Diğer Tedbirler
    #---------------------------------------------------

    diger = (
        vbts_all
        - brut
        - kredi
        - aciga
        - emir
        - tek_fiyat
        - internet
        - depo
    )

    #---------------------------------------------------
    # Export
    #---------------------------------------------------

    exp = Export()

    exp.save(
        "TradingView_BIST_Tum.txt",
        all_symbols,
        "BIST Tum"
    )

    exp.save(
        "TradingView_TradeList.txt",
        trade_list,
        "Trade List"
    )

    exp.save(
        "TradingView_AltPazar.txt",
        alt_pazar,
        "Alt Pazar"
    )

    exp.save(
        "TradingView_BrutTakas.txt",
        brut,
        "Brut Takas"
    )

    exp.save(
        "TradingView_VBTS.txt",
        vbts_all,
        "VBTS"
    )

    exp.save(
        "TradingView_KrediliIslemYasagi.txt",
        kredi,
        "Kredili Islem Yasagi"
    )

    exp.save(
        "TradingView_AcigaSatisYasagi.txt",
        aciga,
        "Aciga Satis Yasagi"
    )

    exp.save(
        "TradingView_EmirPaketi.txt",
        emir,
        "Emir Paketi"
    )

    exp.save(
        "TradingView_TekFiyat.txt",
        tek_fiyat,
        "Tek Fiyat"
    )

    exp.save(
        "TradingView_InternetEmirYasagi.txt",
        internet,
        "Internet Emir Yasagi"
    )

    exp.save(
        "TradingView_DepoSarti.txt",
        depo,
        "Depo Sarti"
    )

    exp.save(
        "TradingView_DigerTedbirler.txt",
        diger,
        "Diger Tedbirler"
    )

    exp.save(
        "TradingView_BrutTakas_AltPazar.txt",
        brut & alt_pazar,
        "Brut Takas + Alt Pazar"
    )

    #---------------------------------------------------
    # Rapor
    #---------------------------------------------------

    exp.report({

        "Toplam BIST"               : len(all_symbols),

        "Trade List"                : len(trade_list),

        "Alt Pazar"                 : len(alt_pazar),

        "Brut Takas"                : len(brut),

        "VBTS Toplam"               : len(vbts_all),

        "Kredili Islem Yasagi"      : len(kredi),

        "Aciga Satis Yasagi"        : len(aciga),

        "Emir Paketi"               : len(emir),

        "Tek Fiyat"                 : len(tek_fiyat),

        "Internet Emir Yasagi"      : len(internet),

        "Depo Sarti"                : len(depo),

        "Diger Tedbirler"           : len(diger)

    })

    print()

    print("Tamamlandi.")

    print("=" * 60)


if __name__ == "__main__":
    main()