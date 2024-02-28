import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle

class OperacionesConjuntos:
    
    """Este metodo es para crear la interfaz de usuario"""
    
    def __init__(self):

        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Operaciones entre conjuntos")
        
        # Crea los widgets de la interfaz
        self.lbl_conjunto_a = tk.Label(self.ventana, text="Conjunto A:")
        self.lbl_conjunto_a.grid(row=0, column=0)
        
        self.entrada_conjunto_a = tk.Entry(self.ventana)
        self.entrada_conjunto_a.grid(row=0, column=1)
        
        self.lbl_conjunto_b = tk.Label(self.ventana, text="Conjunto B:")
        self.lbl_conjunto_b.grid(row=1, column=0)
        
        self.entrada_conjunto_b = tk.Entry(self.ventana)
        self.entrada_conjunto_b.grid(row=1, column=1)
        
        self.btn_union = tk.Button(text="Unión", command=self.calcular_union)
        self.btn_union.grid(row=3, column=0)

        self.btn_interseccion = tk.Button(text="Intersección", command=self.calcular_interseccion)
        self.btn_interseccion.grid(row=3, column=1)

        self.btn_diferencia = tk.Button(text="Diferencia", command=self.calcular_diferencia)
        self.btn_diferencia.grid(row=4, column=0)

        self.btn_complemento = tk.Button(text="Complemento", command=self.calcular_complemento)
        self.btn_complemento.grid(row=4, column=1)

        self.btn_cardinalidad_A = tk.Button(text="Cardinalidad A", command=self.calcular_cardinalidad_A)
        self.btn_cardinalidad_A.grid(row=5, column=0)

        self.btn_cardinalidad_B = tk.Button(text="Cardinalidad B", command=self.calcular_cardinalidad_B)
        self.btn_cardinalidad_B.grid(row=5, column=1)

        self.btn_subconjunto = tk.Button(text="Subconjunto", command=self.calcular_subconjunto)
        self.btn_subconjunto.grid(row=6, column=0)

        self.btn_disjuntos = tk.Button(text="Disjuntos", command=self.calcular_disjuntos)
        self.btn_disjuntos.grid(row=6, column=1)

        # Crear un canvas para los diagramas de Venn
        self.fig = Figure(figsize=(5,   4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.ventana)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

        # Crear un widget de texto para mostrar los resultados
        self.salida = tk.Text(self.ventana, height=8)
        self.salida.grid(row=8, column=0, columnspan=2)

    """Estos metodos son para poder hacer las operaciones para los conjuntos"""

    def union(self, conjunto_a, conjunto_b):
        resultado = set()
        for elemento in conjunto_a:
            resultado.add(elemento)
        for elemento in conjunto_b:
            resultado.add(elemento)
        return resultado

    def interseccion(self, conjunto_a, conjunto_b):
        resultado = set()
        for elemento in conjunto_a:
            if elemento in conjunto_b:
                resultado.add(elemento)
        return resultado

    def diferencia(self, conjunto_a, conjunto_b):
        resultado = set()
        for elemento in conjunto_a:
            if elemento not in conjunto_b:
                resultado.add(elemento)
        return resultado

    def complemento(self, conjunto, universo):
        resultado = set()
        for elemento in universo:
            if elemento not in conjunto:
                resultado.add(elemento)
        return resultado

    def cardinalidad(self, conjunto):
        return len(conjunto)

    def subconjunto(self, conjunto_a, conjunto_b):
        for elemento in conjunto_a:
            if elemento not in conjunto_b:
                return False
        return True

    def disjuntos(self, conjunto_a, conjunto_b):
        for elemento in conjunto_a:
            if elemento in conjunto_b:
                return False
        return True
    
    def imprimir_resultados(self, conjunto_a, conjunto_b, resultado):
        self.salida.delete(1.0, tk.END)  # Limpiar el recuadro de salida
        self.salida.insert(tk.END, f"Conjunto A: {conjunto_a}\n")  # Imprimir el conjunto A
        self.salida.insert(tk.END, f"Conjunto B: {conjunto_b}\n")  # Imprimir el conjunto B
        self.salida.insert(tk.END, f"Resultado: {resultado}\n")  # Imprimir el resultado 

    """Estos metodos me reciben los datos ingresados, hacen la operacion requerida y me imprimen los diagramas"""
    
    def calcular_union(self):
        conjunto_a = set(self.entrada_conjunto_a.get().split(","))
        conjunto_b = set(self.entrada_conjunto_b.get().split(","))       
        resultado = self.union(conjunto_a, conjunto_b)
        self.diagrama_union(conjunto_a, conjunto_b, resultado)

    def calcular_interseccion(self):
        conjunto_a = set(self.entrada_conjunto_a.get().split(","))
        conjunto_b = set(self.entrada_conjunto_b.get().split(","))       
        resultado = self.interseccion(conjunto_a, conjunto_b)
        self.diagrama_interseccion(conjunto_a, conjunto_b, resultado)
    
    def calcular_diferencia(self):
        conjunto_a = set(self.entrada_conjunto_a.get().split(","))
        conjunto_b = set(self.entrada_conjunto_b.get().split(","))
        resultado = self.diferencia(conjunto_a, conjunto_b)
        self.diagrama_diferencia(conjunto_a, conjunto_b, resultado)

    def calcular_complemento(self):
        conjunto_a = set(self.entrada_conjunto_a.get().split(","))
        conjunto_b = set(self.entrada_conjunto_b.get().split(","))  
        universo = set(self.union(conjunto_a, conjunto_b))
        resultado = self.complemento(conjunto_a, universo)
        self.diagrama_complemento(conjunto_a, conjunto_b, resultado)

    def calcular_cardinalidad_A(self):
        conjunto_a = set(self.entrada_conjunto_a.get().split(","))
        resultado = self.cardinalidad(conjunto_a)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, f"Cardinalidad: {resultado}")

    def calcular_cardinalidad_B(self):
        conjunto_b = set(self.entrada_conjunto_b.get().split(","))
        resultado = self.cardinalidad(conjunto_b)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, f"Cardinalidad: {resultado}")

    def calcular_subconjunto(self):
        a = set(self.entrada_conjunto_a.get().split(","))
        b = set(self.entrada_conjunto_b.get().split(","))
        es_subconjunto = self.subconjunto(a, b)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, f"¿{a} es subconjunto de {b}? \n- {es_subconjunto}")

    def calcular_disjuntos(self):
        a = set(self.entrada_conjunto_a.get().split(","))
        b = set(self.entrada_conjunto_b.get().split(","))
        son_disjuntos = self.disjuntos(a, b)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, f"¿{a} y {b} son disjuntos? \n- {son_disjuntos}")

    """Estos metodos son parra imprimir los diagramas de venn"""

    def diagrama_union(self, conjunto_a, conjunto_b, resultado):
        # Limpiar el canvas
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.axis('off')

        # Dibujar los círculos
        circle1 = Circle((0.5,   0.5),   0.33, fill=False)
        ax.add_patch(circle1)

        nuevo_conjunto_a = self.union(conjunto_a, conjunto_b)

        # Imprimir los conjuntos dentro de los círculos
        ax.text(0,  1, f"UNION", ha='center', va='center', fontsize=9)
        ax.text(0.5,  0.5, f"{nuevo_conjunto_a}", ha='center', va='center', fontsize=9)

        # Actualizar el canvas
        self.canvas.draw()

        # Invocar el método para imprimir los resultados
        self.imprimir_resultados(conjunto_a, conjunto_b, resultado)
    
    def diagrama_interseccion(self, conjunto_a, conjunto_b, resultado):
        # Limpiar el canvas
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.axis('off')

        # Dibujar los círculos
        circle1 = Circle((0.6,   0.5),   0.33, fill=False)
        circle2 = Circle((0.4,   0.5),   0.33, fill=False)
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        nuevo_conjunto_a = self.diferencia(conjunto_a, conjunto_b)
        nuevo_conjunto_b = self.diferencia(conjunto_b, conjunto_a)
        nuevo_int = self.interseccion(conjunto_a, conjunto_b)

        # Imprimir los conjuntos dentro de los círculos
        ax.text(0,  1, f"INTERSECCION", ha='center', va='center', fontsize=9)
        ax.text(0.8,  0.4, f"{nuevo_conjunto_a}", ha='center', va='center', fontsize=9)
        ax.text(0.2,  0.6, f"{nuevo_conjunto_b}", ha='center', va='center', fontsize=9)
        ax.text(0.5,  0.5, f"{nuevo_int}", ha='center', va='center', fontsize=9)

        # Actualizar el canvas
        self.canvas.draw()

        # Invocar el método para imprimir los resultados
        self.imprimir_resultados(conjunto_a, conjunto_b, resultado)

    def diagrama_diferencia(self, conjunto_a, conjunto_b, resultado):
        # Limpiar el canvas
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.axis('off')

        # Dibujar los círculos
        circle1 = Circle((0.5,   0.5),   0.33, fill=False)
        ax.add_patch(circle1)

        nuevo_conjunto_a = self.diferencia(conjunto_a, conjunto_b)

        # Imprimir los conjuntos dentro de los círculos
        ax.text(0,  1, f"DIFERENCIA", ha='center', va='center', fontsize=9)
        ax.text(0.5,  0.5, f"{nuevo_conjunto_a}", ha='center', va='center', fontsize=9)

        # Actualizar el canvas
        self.canvas.draw()

        # Invocar el método para imprimir los resultados
        self.imprimir_resultados(conjunto_a, conjunto_b, resultado)

    def diagrama_complemento(self, conjunto_a, conjunto_b, resultado):
        # Limpiar el canvas
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.axis('off')

        # Dibujar los círculos
        circle1 = Circle((0.5,   0.5),   0.33, fill=False)
        ax.add_patch(circle1)

        nuevo_conjunto_a = self.complemento(conjunto_a, conjunto_b)

        # Imprimir los conjuntos dentro de los círculos
        ax.text(0,  1, f"COMPLEMENTO", ha='center', va='center', fontsize=9)
        ax.text(0.5,  0.5, f"{nuevo_conjunto_a}", ha='center', va='center', fontsize=9)

        # Actualizar el canvas
        self.canvas.draw()

        # Invocar el método para imprimir los resultados
        self.imprimir_resultados(conjunto_a, conjunto_b, resultado)

if __name__ == "__main__":
    app = OperacionesConjuntos()
    app.ventana.mainloop()

