#NODOS DE COMPORTAMIENTOS INTELIGENTES DE CADA CRIATURA
# nodos/comportamiento.py

# =========================
# ESTADOS DE EJECUCIÓN
# =========================
EXITO = "EXITO"
FALLO = "FALLO"
EJECUTANDO = "EJECUTANDO"

# =========================
# NODO HOJA: Ver Entorno
# =========================
class NodoVerEntorno:
    def __init__(self, criatura, mapa):
        self.criatura = criatura
        self.mapa = mapa

    def ejecutar(self):
        if not hasattr(self.criatura, "vision") or not hasattr(self.criatura, "posicion"):
            return FALLO

        vision = self.criatura.vision
        pos_x, pos_y = self.criatura.posicion

        celdas_visibles = []
        for dx in range(-vision, vision + 1):
            for dy in range(-vision, vision + 1):
                nuevo_x = pos_x + dx
                nuevo_y = pos_y + dy
                if 0 <= nuevo_x < len(self.mapa) and 0 <= nuevo_y < len(self.mapa[0]):
                    celda = self.mapa[nuevo_x][nuevo_y]
                    if celda.objeto:
                        celdas_visibles.append({
                            "x": nuevo_x,
                            "y": nuevo_y,
                            "objeto": str(celda.objeto)
                        })

        # Actualizar memoria de la criatura
        self.criatura.memoria = celdas_visibles

        return EXITO if celdas_visibles else FALLO

# =========================
# ÁRBOL DE COMPORTAMIENTO
# =========================
class ArbolComportamiento:
    def __init__(self, criatura, mapa):
        # Por ahora solo contiene un nodo simple
        self.raiz = NodoVerEntorno(criatura, mapa)

    def ejecutar(self):
        return self.raiz.ejecutar()
