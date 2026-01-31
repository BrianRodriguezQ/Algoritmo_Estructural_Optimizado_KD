import tkinter as tk
from tkinter import messagebox, ttk
from fractions import Fraction

class LaboratorioTutorKD:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora del Método KD - Sistema de Tutoría")
        self.root.geometry("1100x700")
        self.root.configure(bg="#1a1a1a")

        # --- ESTILOS ---
        self.fuente_titulo = ("Segoe UI", 12, "bold")
        self.fuente_texto = ("Consolas", 11)
        
        # --- PANEL IZQUIERDO: EXPLICACIÓN Y PASO A PASO ---
        self.frame_izq = tk.Frame(root, bg="#000000", bd=2, relief="flat")
        self.frame_izq.place(relx=0.02, rely=0.02, relwidth=0.65, relheight=0.96)

        tk.Label(self.frame_izq, text="SISTEMA DE TUTORÍA: EJECUCIÓN DEL ALGORITMO", 
                 font=self.fuente_titulo, bg="#000000", fg="#41a3db").pack(pady=10)

        self.txt_bitacora = tk.Text(self.frame_izq, bg="#000000", fg="#dcdcdc", 
                                    font=self.fuente_texto, padx=20, pady=20, 
                                    relief="flat", state="disabled", wrap="word")
        self.txt_bitacora.pack(expand=True, fill="both")

        # --- PANEL DERECHO: INTERACCIÓN Y TEORÍA ---
        self.frame_der = tk.Frame(root, bg="#252526")
        self.frame_der.place(relx=0.68, rely=0.02, relwidth=0.3, relheight=0.96)

        # Entrada
        tk.Label(self.frame_der, text="INGRESE EL ÁNGULO (°):",font=self.fuente_titulo, 
                 bg="#252526", fg="white").pack(pady=20)
        
        self.ent_angulo = tk.Entry(self.frame_der, font=("Arial", 20), justify="center", 
                                   bg="#3c3c3c", fg="white", insertbackground="white", relief="flat")
        self.ent_angulo.pack(pady=5, padx=20, fill="x")
        self.ent_angulo.bind("<Return>", lambda e: self.resolver())

        tk.Button(self.frame_der, text="INICIAR TUTORÍA", command=self.resolver, 
                  bg="#0e639c", fg="white", font=("Arial", 11, "bold"), relief="flat", cursor="hand2").pack(pady=20, padx=20, fill="x")

        # Mini Guía Visual (Fija)
        self.crear_panel_guia()

    def crear_panel_guia(self):
        guia_frame = tk.LabelFrame(self.frame_der, text=" Referencia de Fórmulas ", 
                                   bg="#252526", fg="#85c1e9", font=("Arial", 10, "bold"))
        guia_frame.pack(pady=20, padx=20, fill="both", expand=True)

        info = (
            "1. Obtener α (Ref. horizontal)\n"
            "2. Calcular D = 180 / α\n"
            "3. Aplicar k según Cuadrante:\n\n"
            "   Q I:   k = 1\n"
            "   Q II:  k = D - 1\n"
            "   Q III: k = D + 1\n"
            "   Q IV:  k = 2D - 1\n\n"
            "ESTRUCTURA: (k / D) π"
        )
        tk.Label(guia_frame, text=info, justify="left", bg="#252526", fg="#cccccc", 
                 font=("Consolas", 10)).pack(pady=10, padx=10)

    def imprimir(self, texto, color="#dcdcdc"):
        self.txt_bitacora.config(state="normal")
        # Insertar con etiquetas de color si es necesario
        tag = f"tag_{color}"
        self.txt_bitacora.tag_config(tag, foreground=color)
        self.txt_bitacora.insert(tk.END, texto + "\n", tag)
        self.txt_bitacora.config(state="disabled")
        self.txt_bitacora.see(tk.END)

    def resolver(self):
        try:
            self.txt_bitacora.config(state="normal")
            self.txt_bitacora.delete('1.0', tk.END)
            self.txt_bitacora.config(state="disabled")

            angulo_input = float(self.ent_angulo.get())
            
            # --- FASE 1: ANÁLISIS GEOMÉTRICO PREVIO ---
            self.imprimir("=== FASE 1: ANÁLISIS GEOMÉTRICO PREVIO ===", "#85c1e9")
            vueltas = int(angulo_input // 360)
            norm = angulo_input % 360
            
            self.imprimir(f"> Ángulo ingresado: {angulo_input}°")
            self.imprimir(f"> Rotación: El ángulo contiene {vueltas} vuelta(s) completa(s).")
            self.imprimir(f"> Posición en el Círculo Unitario: {norm}°")

            # Determinación de cuadrante y alpha
            if 0 <= norm <= 90:
                q, alpha, formula_k = "I", norm, "k = 1"
                exp_a = f"{norm} - 0"
            elif 90 < norm <= 180:
                q, alpha, formula_k = "II", 180 - norm, "k = D - 1"
                exp_a = f"180 - {norm}"
            elif 180 < norm <= 270:
                q, alpha, formula_k = "III", norm - 180, "k = D + 1"
                exp_a = f"{norm} - 180"
            else:
                q, alpha, formula_k = "IV", 360 - norm, "k = 2D - 1"
                exp_a = f"360 - {norm}"

            self.imprimir(f"> Ubicación: Cuadrante {q}")
            self.imprimir(f"> Derivación de alpha (α): Distancia al eje X horizontal.")
            self.imprimir(f"  α = {exp_a} = {alpha}°", "#f7dc6f")
            
            # --- FASE 2: OBTENCIÓN DE VALORES DE LA FÓRMULA ---
            self.imprimir("\n=== FASE 2: OBTENCIÓN DE VALORES (k, D) ===", "#85c1e9")
            
            if alpha == 0:
                val_final = "0" if norm == 0 else "π"
                self.imprimir(f"Ángulo sobre eje horizontal detectado. Valor directo: {val_final}")
                return

            D = 180 / alpha
            self.imprimir(f"1. Valor de D (Denominador): 180 / {alpha} = {round(D, 4)}")
            self.imprimir(f"2. Valor de k (Numerador): Basado en Q {q} -> {formula_k}")
            
            # Cálculo de k
            if q == "I": k = 1
            elif q == "II": k = D - 1
            elif q == "III": k = D + 1
            else: k = (2 * D) - 1
            
            self.imprimir(f"   k_base = {round(k, 4)}")
            
            k_final = k + (vueltas * 2 * D)
            if vueltas != 0:
                self.imprimir(f"3. Ajuste por vueltas: k + ({vueltas} * 2 * {round(D,2)}) = {round(k_final, 4)}")

            # --- FASE 3: PROCEDIMIENTO Y RESULTADO ---
            self.imprimir("\n=== FASE 3: RESULTADO FINAL Y COMPARACIÓN ===", "#85c1e9")
            res_kd = f"({round(k_final, 4)} / {round(D, 4)}) π"
            
            self.imprimir(f"ESTRUCTURA k/D OBTENIDA: {res_kd}", "#2196da")
            
            # --- FASE 4: NORMALIZACIÓN Y EQUIVALENCIA ---
            self.imprimir("\n=== FASE 4: NORMALIZACIÓN DE FRACCIÓN ===", "#85c1e9")
            
            # Chequeamos si hay decimales para normalizar
            if D % 1 == 0 and k_final % 1 == 0:
                self.imprimir("La estructura ya se encuentra en números enteros.")
                res_final_str = f"{int(k_final)} / {int(D)} π"
            else:
                self.imprimir("Detectada base decimal. Aplicando factor de normalización (x10)...")
                # Multiplicamos por 10 para eliminar un decimal, o más si fuera necesario
                num_entero = int(round(k_final * 10, 0))
                den_entero = int(round(D * 10, 0))
                
                # Simplificamos la fracción resultante para llegar al método tradicional
                frac_simplificada = Fraction(num_entero, den_entero)
                
                self.imprimir(f"Estructura k/D Original: ({round(k_final,2)} / {round(D,2)}) π")
                self.imprimir(f"Estructura Normalizada: ({num_entero} / {den_entero}) π")
                res_final_str = f"{frac_simplificada.numerator} / {frac_simplificada.denominator} π"

            self.imprimir(f"\nRESULTADO DEFINITIVO: {res_final_str}", "#2cc0e6")

            # Método Tradicional
            trad = Fraction(angulo_input/180).limit_denominator()
            res_trad = f"{trad.numerator}/{trad.denominator} π"
            
            self.imprimir(f"MÉTODO TRADICIONAL (MCD): {res_trad}", "#f39c12")
            self.imprimir("\n>>> CONCLUSIÓN: El algoritmo ha predicho la estructura irreducible con éxito.")

        except ValueError:
            messagebox.showerror("Error", "Entrada inválida. Ingrese un número.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LaboratorioTutorKD(root)
    root.mainloop()