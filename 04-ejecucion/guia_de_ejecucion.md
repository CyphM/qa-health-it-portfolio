# Guía de ejecución de los casos

Cómo ejecutar los 10 casos de [`casos_prescripcion.md`](../02-casos-de-prueba/casos_prescripcion.md) de forma ordenada y repetible.

## Antes de empezar
1. Abre la demo de OpenEMR desde la página oficial de demos (`demo.openemr.io`) y usa las credenciales públicas que el proyecto publica ahí para los perfiles médico, clínico y recepcionista. No se copian en este repositorio.
2. La demo **se reinicia cada día**: ejecuta todos los casos el mismo día y guarda la evidencia ese mismo día.
3. Anota una sola vez, al inicio: fecha, hora, **versión de OpenEMR** que muestra la demo, navegador y su versión.
4. Usa solo pacientes y medicamentos ficticios de la demo. Si una captura muestra algo que parece un dato real, no la subas.

## Orden recomendado
Algunos casos necesitan una prescripción previa, por eso el orden importa:

| Orden | Caso | Por qué en este punto |
|---|---|---|
| 1 | CP-002 | Búsqueda de medicamento: no depende de nada |
| 2 | CP-003, CP-004, CP-005 | Casos negativos: no deben dejar datos guardados |
| 3 | CP-001 | Crea la prescripción que usan los siguientes |
| 4 | CP-006, CP-010 | Editar e imprimir sobre la prescripción activa |
| 5 | CP-007 | Discontinuar: deja de existir una prescripción activa |
| 6 | CP-008 | Requiere un paciente con alergia registrada |
| 7 | CP-009 | Cambia de rol (recepcionista): hacerlo al final evita cerrar sesión en medio |

## Para cada caso
1. Sigue los pasos tal como están escritos; no improvises.
2. Compara con el resultado esperado.
3. Completa en el archivo de casos: **Resultado obtenido**, **Estado** (Aprobado / Fallido / Bloqueado / No aplicable) y **Evidencia** (nombre del archivo de la captura).
4. Si falla, crea un reporte con la [plantilla](../03-reporte-de-hallazgos/plantilla_reporte_hallazgo.md) (ID `HAL-001`, `HAL-002`...), enlazado al caso y al requisito.

## Cómo decidir el estado
| Estado | Cuándo |
|---|---|
| Aprobado | El resultado obtenido coincide con el esperado |
| Fallido | Difiere y el sistema se comporta mal (genera un hallazgo tipo *Defecto*) |
| Bloqueado | No se pudo ejecutar (la demo cayó, falta una precondición) |
| No aplicable | La función no existe en la demo (hallazgo tipo *Limitación del ambiente*) |

## Al terminar
Completa el [resumen de ejecución](plantilla_resumen_ejecucion.md) con las cifras y las conclusiones.

## Convención para las evidencias
Carpeta `04-ejecucion/evidencias/AAAA-MM-DD/` y archivos `CP-001_paso3.png`. Revisa cada captura antes de subirla.
