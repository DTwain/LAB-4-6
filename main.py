from UI.console import run_console
from UI.batch import run_batch

tip_meniu = input("Alege tipul meniului ( CONSOLE / BATCH ): ")

if tip_meniu == "CONSOLE":
    run_console()
else :
    run_batch() 