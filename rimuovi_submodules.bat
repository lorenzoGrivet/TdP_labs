@echo off
REM === Elenco dei submodules da rimuovere e convertire ===
set SUBMODULES=nyc-hotspots provaFlet quadrato_magico simulazione_03_06_2020 simulazione_29_06_2020 simulazione_esame_04_09_2020 simulazione_esame_1_6_21 simulazione_esame_30_06_2023 simulazione_esame_bianca simulazione_ufo test_connessione

echo Inizio la rimozione completa dei submodules e la conversione in cartelle normali...

for %%S in (%SUBMODULES%) do (
    echo --------------------------------------------
    echo Rimuovo il submodule: %%S

    REM Rimuovo il submodule dal repo principale
    git submodule deinit -f %%S
    git rm -f %%S
    rmdir /S /Q .git\modules\%%S

    REM Controllo e rimuovo voci residue da .gitmodules
    echo Rimuovo voce residua da .gitmodules per %%S...
    powershell -Command "(Get-Content .gitmodules) -replace '^\[submodule \"%%S\"\].*?$', '' | Set-Content .gitmodules"

    REM Controllo e rimuovo voci residue da .git/config
    echo Rimuovo voce residua da .git/config per %%S...
    powershell -Command "(Get-Content .git/config) -replace '^\[submodule \"%%S\"\].*?$', '' | Set-Content .git/config"

    REM Ripristino la cartella dai file ancora presenti
    echo Ripristino cartella %%S come normale directory...
    xcopy /E /I /Y %%S %%S_temp
    mkdir %%S
    xcopy /E /I /Y %%S_temp %%S
    rmdir /S /Q %%S_temp

    REM Aggiungo la cartella ripristinata come normale directory
    git add %%S
)

REM Committing final changes
git add .gitmodules
git commit -m "Rimozione completa riferimenti submodules e conversione in cartelle normali"
echo Conversione completata con successo!

REM Fare il push delle modifiche
git push
echo Modifiche pushate al repository remoto!
