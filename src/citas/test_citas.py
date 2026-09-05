# src/citas/citas.py

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

def registrar_cita():
    print("Registro de cita psicologica")

# ==========================================
# PRUEBA AUTOMATIZADA (Caso Crítico CP-05)
# ==========================================
def test_evitar_solapamiento_citas():
    # Cita previamente agendada en la base de datos
    citas_existentes = [
        {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "10:00"}
    ]
    
    # Intento de registrar una cita duplicada en el mismo horario
    cita_duplicada = {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "10:00"}
    
    # Intento de registrar una cita válida en otro horario
    cita_valida = {"terapeuta": "Dr. Juan Pérez", "fecha": "2026-09-10", "hora": "11:00"}
    
    # Validaciones (CP-05)
    assert validar_solapamiento(cita_duplicada, citas_existentes) == False
    assert validar_solapamiento(cita_valida, citas_existentes) == True
