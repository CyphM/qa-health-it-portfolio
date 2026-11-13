# Portafolio QA — Sistemas de salud

[![Trazabilidad](https://github.com/CyphM/qa-health-it-portfolio/actions/workflows/trazabilidad.yml/badge.svg)](https://github.com/CyphM/qa-health-it-portfolio/actions/workflows/trazabilidad.yml)

Portafolio de QA con plan de pruebas, casos de prueba y reportes de hallazgos sobre **OpenEMR**, un sistema de salud de código abierto. Todo el trabajo usa la demo pública de OpenEMR y **datos 100 % ficticios**: no hay información de pacientes, hospitales ni empresas reales.

**Autor:** Rodrigo Vargas León · Ingeniero en Informática, especialización en Calidad de Software
[LinkedIn](https://www.linkedin.com/in/rodrigo-vargas-leon)

## Qué hay aquí

| Carpeta | Contenido | Estado |
|---|---|---|
| [`01-plan-de-pruebas`](01-plan-de-pruebas/plan_de_pruebas.md) | Alcance, estrategia, ambiente, criterios de entrada y salida, riesgos | Borrador |
| [`02-casos-de-prueba`](02-casos-de-prueba/casos_prescripcion.md) | 10 casos de prueba del flujo de prescripción y su [matriz de trazabilidad](02-casos-de-prueba/matriz_trazabilidad.md), validada automáticamente | Diseñados, pendientes de ejecutar |
| [`03-reporte-de-hallazgos`](03-reporte-de-hallazgos/plantilla_reporte_hallazgo.md) | Plantilla para reportar defectos | Lista |
| [`04-ejecucion`](04-ejecucion/guia_de_ejecucion.md) | Guía para ejecutar los casos y plantilla de resumen de ejecución | Lista |
| [`tools`](tools/validar_trazabilidad.py) | Script que verifica que requisitos, casos y matriz sean consistentes | Lista |

## Cómo trabajo

1. Defino requisitos funcionales de referencia para el flujo a probar.
2. Diseño casos de prueba trazables a cada requisito (camino feliz, negativos y límites).
3. Ejecuto los casos en la demo y registro resultado obtenido y evidencia.
4. Reporto cada defecto con pasos reproducibles, resultado esperado y obtenido, y prioridad.

## Nota

OpenEMR es un proyecto independiente y esta es una práctica personal sin relación con sus desarrolladores. Los requisitos son supuestos definidos para este ejercicio, no especificaciones oficiales del producto.
