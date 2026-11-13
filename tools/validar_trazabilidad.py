#!/usr/bin/env python3
"""Verifica que la matriz de trazabilidad coincida con los casos y el plan.

Reglas:
  1. Todo requisito del plan aparece en la matriz y tiene al menos un caso.
  2. Todo caso apunta al menos a un requisito que existe en el plan.
  3. La matriz coincide exactamente con lo que declaran los casos.

Uso: python tools/validar_trazabilidad.py   (devuelve 1 si hay diferencias)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLAN = RAIZ / "01-plan-de-pruebas" / "plan_de_pruebas.md"
CASOS = RAIZ / "02-casos-de-prueba" / "casos_prescripcion.md"
MATRIZ = RAIZ / "02-casos-de-prueba" / "matriz_trazabilidad.md"


def requisitos_del_plan() -> set[str]:
    return set(re.findall(r"^\| (RF-\d+) \|", PLAN.read_text(encoding="utf-8"), re.M))


def casos_declarados() -> dict[str, set[str]]:
    """Devuelve {CP-xxx: {RF-xx, ...}} leyendo la línea 'Requisitos' de cada caso."""
    out: dict[str, set[str]] = {}
    actual = None
    for linea in CASOS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"### (CP-\d+)", linea)
        if m:
            actual = m.group(1)
            out[actual] = set()
        elif actual and "**Requisitos:**" in linea:
            out[actual] = set(re.findall(r"RF-\d+", linea.split("Prioridad")[0]))
    return out


def matriz() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for linea in MATRIZ.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (RF-\d+) \| ([^|]+) \|", linea)
        if m:
            out[m.group(1)] = set(re.findall(r"CP-\d+", m.group(2)))
    return out


def main() -> int:
    reqs, casos, mat = requisitos_del_plan(), casos_declarados(), matriz()
    errores = []

    for rf in sorted(reqs - set(mat)):
        errores.append(f"{rf} está en el plan pero no en la matriz")
    for rf in sorted(set(mat) - reqs):
        errores.append(f"{rf} está en la matriz pero no en el plan")
    for cp, rfs in sorted(casos.items()):
        if not rfs:
            errores.append(f"{cp} no declara ningún requisito")
        for rf in sorted(rfs - reqs):
            errores.append(f"{cp} apunta a {rf}, que no existe en el plan")

    esperado: dict[str, set[str]] = {rf: set() for rf in reqs}
    for cp, rfs in casos.items():
        for rf in rfs & reqs:
            esperado[rf].add(cp)
    for rf in sorted(reqs & set(mat)):
        if not esperado[rf]:
            errores.append(f"{rf} no tiene ningún caso")
        if esperado[rf] != mat[rf]:
            errores.append(
                f"{rf}: la matriz dice {sorted(mat[rf])} pero los casos dicen {sorted(esperado[rf])}"
            )

    if errores:
        print("Trazabilidad con diferencias:")
        for e in errores:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(reqs)} requisitos, {len(casos)} casos, matriz consistente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
