_usuario_actual = None


def iniciar_sesion(usuario):
    global _usuario_actual
    _usuario_actual = usuario


def cerrar_sesion():
    global _usuario_actual
    _usuario_actual = None


def obtener_usuario_actual():
    return _usuario_actual


def hay_sesion():
    return _usuario_actual is not None
