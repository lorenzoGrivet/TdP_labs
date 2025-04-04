@echo off
REM === Elenco dei submodules da convertire ===
set SUBMODULES=nyc-hotspots provaFlet quadrato_magico simulazione_03_06_2020 simulazione_29_06_2020 simulazione_esame_04_09_2020 simulazione_esame_1_6_21 simulazione_esame_30_06_2023 simulazione_esame_bianca simulazione_ufo test_connessione

echo Inizio conversione dei submodules in cartelle normali...

for %%S in (%SUBMODULES%) do (
    echo --------------------------------------------
    echo Conversione submodule: %%S

    git submodule deinit -f %%S
    git rm -f %%S
    rmdir /S /Q .git\modules\%%S

    REM Ripristino la cartella dai file ancora presenti
    echo Ripristino cartella %%S come normale directory...
    xcopy /E /I /Y %%S %%S_temp
    mkdir %%S
    xcopy /E /I /Y %%S_temp %%S
    rmdir /S /Q %%S_temp

    git add %%S
)

echo --------------------------------------------
git commit -m "Convertiti submodules in cartelle normali"
echo Fatto!
