# Casos de prueba — Flujo de prescripción (OpenEMR)

**Versión:** 0.1 · **Estado general:** diseñados, **pendientes de ejecutar**.
Las columnas *Resultado obtenido*, *Estado* y *Evidencia* se completan al ejecutar cada caso en la demo (anotar fecha, hora y versión del navegador).

**Datos de prueba comunes:** cualquier paciente ficticio de la demo; medicamentos genéricos de uso común (por ejemplo amoxicilina 500 mg, paracetamol 500 mg). **Rol:** médico, salvo que se indique otro.

## Tipos de flujo
- **Normal:** el proceso como debería funcionar (camino feliz).
- **Alternativo:** el proceso cambia por una condición distinta (alergia, otro rol).
- **Excepción:** el usuario o el dato se salen de lo esperado (campo vacío, valor inválido, límite).

## Matriz de trazabilidad
| Requisito | Casos |
|---|---|
| RF-01 | CP-001 |
| RF-02 | CP-003, CP-004, CP-005 |
| RF-03 | CP-001 |
| RF-04 | CP-006, CP-007 |
| RF-05 | CP-008 |
| RF-06 | CP-010 |
| RF-07 | CP-009 |
| RF-08 | CP-002 |

---

### CP-001 — Crear prescripción válida (camino feliz)
- **Requisitos:** RF-01, RF-03 · **Prioridad:** Alta · **Flujo:** Normal
- **Precondición:** sesión iniciada como médico; paciente ficticio abierto.
- **Pasos:** 1) Ir a la sección de prescripciones del paciente. 2) Crear una nueva prescripción. 3) Ingresar medicamento, dosis, vía, frecuencia y cantidad válidos. 4) Guardar.
- **Resultado esperado:** la prescripción se guarda y aparece como activa en la ficha del paciente con los datos ingresados.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-002 — Buscar medicamento por nombre parcial
- **Requisitos:** RF-08 · **Prioridad:** Media · **Flujo:** Normal
- **Precondición:** igual que CP-001.
- **Pasos:** 1) Abrir una nueva prescripción. 2) Escribir las primeras letras de un medicamento conocido (p. ej. "amox").
- **Resultado esperado:** el sistema sugiere o lista medicamentos que coinciden con el texto.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-003 — Guardar sin medicamento (negativo)
- **Requisitos:** RF-02 · **Prioridad:** Alta · **Flujo:** Excepción (dato faltante)
- **Pasos:** 1) Abrir una nueva prescripción. 2) Completar dosis y cantidad, dejando el medicamento vacío. 3) Intentar guardar.
- **Resultado esperado:** el sistema no guarda y muestra un mensaje indicando el campo obligatorio.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-004 — Dosis con valor no válido (negativo)
- **Requisitos:** RF-02 · **Prioridad:** Media · **Flujo:** Excepción (dato inválido)
- **Pasos:** 1) Abrir una nueva prescripción con medicamento válido. 2) Ingresar en dosis un valor negativo (por ejemplo −5) o texto sin sentido. 3) Intentar guardar.
- **Resultado esperado:** el sistema rechaza el valor o lo advierte; no guarda una dosis inválida.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-005 — Cantidad igual a cero (valor límite)
- **Requisitos:** RF-02 · **Prioridad:** Media · **Flujo:** Excepción (valor límite)
- **Pasos:** 1) Abrir una nueva prescripción con datos válidos. 2) Ingresar cantidad 0. 3) Intentar guardar.
- **Resultado esperado:** el sistema rechaza la cantidad 0 o muestra una advertencia.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-006 — Editar una prescripción existente
- **Requisitos:** RF-04 · **Prioridad:** Media · **Flujo:** Normal
- **Precondición:** existe una prescripción activa (crear con CP-001).
- **Pasos:** 1) Abrir la prescripción. 2) Cambiar la dosis a otro valor válido. 3) Guardar.
- **Resultado esperado:** el cambio se guarda y se refleja en la ficha del paciente.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-007 — Discontinuar una prescripción
- **Requisitos:** RF-04 · **Prioridad:** Alta · **Flujo:** Normal
- **Precondición:** existe una prescripción activa.
- **Pasos:** 1) Abrir la prescripción activa. 2) Discontinuarla o marcarla como inactiva.
- **Resultado esperado:** deja de aparecer como activa, sin perder su historial.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-008 — Prescribir a un paciente con alergia registrada
- **Requisitos:** RF-05 · **Prioridad:** Alta · **Flujo:** Alternativo (riesgo clínico)
- **Precondición:** paciente ficticio con una alergia registrada (p. ej. penicilina).
- **Pasos:** 1) Crear una prescripción de un medicamento de la misma familia (p. ej. amoxicilina). 2) Guardar.
- **Resultado esperado:** el sistema muestra una advertencia de alergia antes o al guardar.
- **Nota:** si la demo no tiene activada esta función, registrar como **limitación del ambiente**, no como defecto.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-009 — Recepcionista intenta prescribir (permisos)
- **Requisitos:** RF-07 · **Prioridad:** Alta · **Flujo:** Alternativo (rol no autorizado)
- **Precondición:** sesión iniciada con el rol de recepcionista.
- **Pasos:** 1) Abrir la ficha de un paciente. 2) Intentar crear una prescripción.
- **Resultado esperado:** la opción no está disponible o el sistema deniega la acción.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_

### CP-010 — Imprimir o exportar la prescripción
- **Requisitos:** RF-06 · **Prioridad:** Media · **Flujo:** Normal
- **Precondición:** existe una prescripción activa.
- **Pasos:** 1) Abrir la prescripción. 2) Usar la opción de imprimir o generar PDF.
- **Resultado esperado:** se genera un documento con los datos del paciente y del medicamento sin errores de formato.
- **Resultado obtenido:** _pendiente_ · **Estado:** Pendiente · **Evidencia:** _pendiente_
