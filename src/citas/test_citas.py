import pytest

def validar_solapamiento(cita_nueva, citas_existentes):
    """
    CP-05: Valida que un terapeuta no tenga dos citas en el mismo horario.
    Retorna False si hay conflicto de agenda, True si la cita es válida.
    """
    for cita in citas_existentes:
        if (cita['terapeuta'] == cita_nueva['terapeuta'] and 
            cita['fecha'] == cita_nueva['fecha'] and 
            cita['hora'] == cita_nueva['hora']):
            return False
    return True

def test_evitar_solapamiento_citas():
    # 1. Cita agendada previa
    citas_existentes = [
        {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "10:00"}
    ]
    
    # 2. Cita duplicada (debe dar False)
    cita_duplicada = {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "10:00"}
    
    # 3. Cita en horario libre (debe dar True)
    cita_valida = {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "11:00"}
    
    # 4. Verificaciones
    assert validar_solapamiento(cita_duplicada, citas_existentes) == False
    assert validar_solapamiento(cita_valida, citas_existentes) == True
