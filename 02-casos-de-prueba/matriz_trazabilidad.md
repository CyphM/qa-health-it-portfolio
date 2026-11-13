# Matriz de trazabilidad — Flujo de prescripción (OpenEMR)

Cada requisito del [plan de pruebas](../01-plan-de-pruebas/plan_de_pruebas.md) debe tener al menos un caso en [`casos_prescripcion.md`](casos_prescripcion.md), y cada caso debe apuntar al menos a un requisito. Esta matriz se valida automáticamente con `tools/validar_trazabilidad.py`.

| Requisito | Casos | Nº de casos | Cobertura |
|---|---|---|---|
| RF-01 | CP-001 | 1 | Mínima |
| RF-02 | CP-003, CP-004, CP-005 | 3 | Buena |
| RF-03 | CP-001 | 1 | Mínima |
| RF-04 | CP-006, CP-007 | 2 | Aceptable |
| RF-05 | CP-008 | 1 | Mínima (depende de la demo) |
| RF-06 | CP-010 | 1 | Mínima |
| RF-07 | CP-009 | 1 | Mínima |
| RF-08 | CP-002 | 1 | Mínima |

## Lectura
- **Sin requisitos sin cubrir:** los 8 requisitos tienen al menos un caso.
- **Cobertura mínima** significa un solo caso: alcanza para una primera pasada, pero si aparece un defecto conviene agregar casos (más datos, otros roles, otros medicamentos).
- **RF-01 y RF-03** dependen del mismo caso (CP-001): si falla, quedan sin verificar ambos.
- **RF-05** puede resultar una limitación de la demo y no un defecto (ver nota de CP-008).
