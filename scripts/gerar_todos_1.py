"""Executa todos os scripts de gráficos, um após o outro."""
import subprocess
import sys
from pathlib import Path

pasta = Path(__file__).resolve().parent
for script in sorted(pasta.glob("grafico_*.py")):
    print(f"-> {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)
