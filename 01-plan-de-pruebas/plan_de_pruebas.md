# Plan de pruebas — Flujo de prescripción en OpenEMR

| | |
|---|---|
| **Autor** | Rodrigo Vargas León |
| **Versión** | 0.1 (borrador) |
| **Sistema bajo prueba** | OpenEMR, demo pública (`demo.openemr.io`) |
| **Tipo de pruebas** | Funcionales, manuales |

## 1. Objetivo
Verificar que el flujo de prescripción de medicamentos funciona según los requisitos de referencia (sección 4), identificando defectos antes de un uso clínico.

## 2. Alcance
**Dentro:** crear, buscar, editar, discontinuar e imprimir prescripciones; validación de campos; permisos por rol.
**Fuera:** facturación, agenda, portal del paciente, integraciones externas, rendimiento y seguridad.

## 3. Ambiente de pruebas
- Demo pública de OpenEMR (los datos se reinician cada día, por eso la evidencia debe registrarse el mismo día de la ejecución).
- Credenciales públicas de demostración publicadas por el proyecto (perfiles médico, clínico y recepcionista).
- Navegador de escritorio actualizado. Registrar versión del navegador y fecha/hora de cada ejecución.
- **Datos:** solo pacientes y medicamentos ficticios de la demo. No ingresar datos reales bajo ninguna circunstancia.

## 4. Requisitos de referencia (definidos para este ejercicio)
| ID | Requisito |
|---|---|
| RF-01 | El médico puede crear una prescripción indicando medicamento, dosis, vía, frecuencia y cantidad. |
| RF-02 | El sistema valida los campos obligatorios y rechaza valores no válidos. |
| RF-03 | Las prescripciones activas se muestran en la ficha del paciente. |
| RF-04 | Una prescripción puede editarse y discontinuarse. |
| RF-05 | Si el paciente tiene una alergia registrada al medicamento, el sistema lo advierte (se verifica si la demo lo soporta). |
| RF-06 | La prescripción puede imprimirse o exportarse. |
| RF-07 | Solo los roles autorizados pueden prescribir. |
| RF-08 | El medicamento se puede buscar por nombre. |

## 5. Estrategia
Casos manuales diseñados con técnicas de **partición de equivalencia**, **valores límite** y casos **negativos**. Prioridad Alta para el camino feliz, la seguridad del paciente (alergias, permisos), los campos obligatorios y la discontinuación de prescripciones; Media para el resto.

## 6. Criterios
- **Entrada:** demo disponible, credenciales funcionando, casos revisados.
- **Salida:** 100 % de casos de prioridad Alta ejecutados, sin defectos críticos abiertos, defectos restantes documentados.

## 7. Riesgos
| Riesgo | Mitigación |
|---|---|
| La demo se reinicia cada día y puede cambiar su versión | Registrar versión y fecha en cada ejecución; guardar capturas |
| Algunas funciones (p. ej. alertas de alergia) pueden no estar activas en la demo | Documentarlo como limitación, no como defecto |
| Los requisitos son supuestos propios | Indicarlo en el README y en cada reporte |

## 8. Entregables
Casos de prueba, [matriz de trazabilidad](../02-casos-de-prueba/matriz_trazabilidad.md), reportes de hallazgos y un [resumen de ejecución](../04-ejecucion/plantilla_resumen_ejecucion.md).
