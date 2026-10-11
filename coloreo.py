#!/usr/bin/env python3
"""Coloreo de mapas con P = (S, A, T, s0, G, c)."""
import argparse, csv
from collections import deque

class ProblemaColoreo:
    def __init__(self, nombres, aristas, k=4):
        self.n, self.k, self.nombres = len(nombres), k, list(nombres)
        self.s0 = (0,) * self.n
        self.vecinos = [set() for _ in range(self.n)]
        pos = {m: i for i, m in enumerate(self.nombres)}
        for a, b in aristas:
            i, j = pos[a], pos[b]
            self.vecinos[i].add(j); self.vecinos[j].add(i)

    def decididos(self, s): return self.n - s.count(0)
    def colores_usados(self, s): return len({x for x in s if x})

    def es_valido(self, s):
        if len(s) != self.n or any(not (0 <= x <= self.k) for x in s): return False, "longitud o valor inválido"
        if 0 in s and any(x != 0 for x in s[s.index(0):]): return False, "decisión tras un cero"
        for i, x in enumerate(s):
            if x and any(s[j] == x for j in self.vecinos[i] if j < i):
                return False, f"conflicto en vecinos"
        return True, ""

    def es_meta(self, s): return self.es_valido(s)[0] and 0 not in s

    def acciones(self, s):
        if 0 not in s: return []
        v = self.decididos(s)
        tomados = {s[j] for j in self.vecinos[v] if s[j]}
        return [c for c in range(1, self.k + 1) if c not in tomados]

    def transicion(self, s, c):
        v = self.decididos(s)
        return s[:v] + (c,) + s[v + 1:]

    def costo(self, s, c): return 0 if c in s else 1

    def resolver(self):
        def dfs(s):
            if self.es_meta(s): return []
            for c in self.acciones(s):
                t = self.transicion(s, c)
                res = dfs(t)
                if res is not None: return [(s, c, self.costo(s, c))] + res
            return None
        return dfs(self.s0)

def contar(p):
    por_nivel, cola = [1], deque([(p.s0, 0)])
    total_est = 1
    while cola:
        s, i = cola.popleft()
        for c in p.acciones(s):
            if i + 1 >= len(por_nivel): por_nivel.append(0)
            por_nivel[i + 1] += 1
            total_est += 1
            cola.append((p.transicion(s, c), i + 1))
    return {"estados": total_est, "metas": por_nivel[-1] if len(por_nivel) == p.n + 1 else 0, "por_nivel": por_nivel}

def pruebas():
    ar = [("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")]
    p = ProblemaColoreo(list("ABCD"), ar, k=3)
    assert p.es_valido(p.s0)[0]
    assert p.acciones(p.s0) == [1, 2, 3]
    assert p.transicion((1, 0, 0, 0), 2) == (1, 2, 0, 0)
    assert p.costo((1, 2, 0, 0), 2) == 0 and p.costo((1, 2, 0, 0), 3) == 1
    assert p.es_meta((1, 2, 3, 1))
    print("Todas las pruebas pasaron con éxito.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pruebas", action="store_true")
    args = ap.parse_args()
    if args.pruebas: pruebas()
    else: print("Ejecuta con --pruebas para verificar el modelo.")
