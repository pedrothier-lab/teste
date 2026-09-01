
import tkinter as tk
from tkinter import ttk, messagebox




CORES = {
    "Preto": "#000000",
    "Marrom": "#8B4513",
    "Vermelho": "#FF0000",
    "Laranja": "#FF8C00",
    "Amarelo": "#FFD700",
    "Verde": "#008000",
    "Azul": "#0000FF",
    "Violeta": "#8A2BE2",
    "Cinza": "#808080",
    "Branco": "#FFFFFF"
}

DIGITOS = {
    "Preto": 0,
    "Marrom": 1,
    "Vermelho": 2,
    "Laranja": 3,
    "Amarelo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Cinza": 8,
    "Branco": 9
}

MULTIPLICADORES = {
    "Preto": 1,
    "Marrom": 10,
    "Vermelho": 100,
    "Laranja": 1_000,
    "Amarelo": 10_000,
    "Verde": 100_000,
    "Azul": 1_000_000,
    "Violeta": 10_000_000,
    "Cinza": 100_000_000,
    "Branco": 1_000_000_000
}

TOLERANCIAS = {
    "Marrom": 1,
    "Vermelho": 2,
    "Verde": 0.5,
    "Azul": 0.25,
    "Violeta": 0.1,
    "Cinza": 0.05,
    "Dourado": 5,
    "Prateado": 10
}

CORES_DIGITOS = list(DIGITOS.keys())
CORES_TOLERANCIA = list(TOLERANCIAS.keys())


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def formatar_resistencia(valor):
    """
    Converte o valor para uma representação amigável:
    Ω, kΩ ou MΩ.
    """
    if valor >= 1_000_000:
        numero = valor / 1_000_000
        return f"{numero:g} MΩ"

    elif valor >= 1_000:
        numero = valor / 1_000
        return f"{numero:g} kΩ"

    else:
        return f"{valor:g} Ω"


def encontrar_cor_multiplicador(multiplicador):
    """
    Encontra a cor correspondente ao multiplicador.
    """
    for cor, valor in MULTIPLICADORES.items():
        if valor == multiplicador:
            return cor

    return None


def calcular_resistencia(cor1, cor2, cor3):
    """
    Calcula a resistência a partir das três primeiras faixas.
    """
    primeiro = DIGITOS[cor1]
    segundo = DIGITOS[cor2]
    multiplicador = MULTIPLICADORES[cor3]

    valor = (primeiro * 10 + segundo) * multiplicador
    return valor


def calcular_cores(valor):
    """
    Recebe o valor da resistência e retorna as três cores
    das faixas de valor.

    Exemplo:
    3300 -> Laranja, Laranja, Vermelho
    """
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    # Precisamos representar o valor usando:
    # dois dígitos significativos + multiplicador.
    for multiplicador in sorted(MULTIPLICADORES.values()):
        base = valor / multiplicador

        # Procuramos uma representação com exatamente
        # dois dígitos significativos inteiros.
        if base >= 10 and base <= 99 and base == int(base):
            base = int(base)

            primeiro = base // 10
            segundo = base % 10

            cor1 = next(c for c, v in DIGITOS.items() if v == primeiro)
            cor2 = next(c for c, v in DIGITOS.items() if v == segundo)
            cor3 = encontrar_cor_multiplicador(multiplicador)

            if cor3 is not None:
                return cor1, cor2, cor3

    raise ValueError(
        "Valor não representável com 4 faixas "
        "(2 dígitos + multiplicador)."
    )


# ============================================================
# CLASSE PRINCIPAL
# ============================================================

class SAPZApp:

    def __init__(self, root):
        self.root = root

        self.root.title("SAPZ - Calculadora de Códigos de Cores de Resistores")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        self.modo = tk.StringVar(value="cores")

        self.criar_interface()

        self.atualizar_modo()


    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="SAPZ - Calculadora de Resistores",
            font=("Arial", 22, "bold"),
            fg="#17365D"
        )
        titulo.pack(pady=(15, 5))

        subtitulo = tk.Label(
            self.root,
            text="Código de cores de resistores - 4 faixas",
            font=("Arial", 11)
        )
        subtitulo.pack(pady=(0, 15))


        # ----------------------------------------------------
        # ESCOLHA DO MODO
        # ----------------------------------------------------

        frame_modo = tk.LabelFrame(
            self.root,
            text="Modo de operação",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        frame_modo.pack(fill="x", padx=30, pady=5)

        tk.Radiobutton(
            frame_modo,
            text="Cores → Valor",
            variable=self.modo,
            value="cores",
            command=self.atualizar_modo,
            font=("Arial", 11)
        ).pack(side="left", padx=30)

        tk.Radiobutton(
            frame_modo,
            text="Valor → Cores",
            variable=self.modo,
            value="valor",
            command=self.atualizar_modo,
            font=("Arial", 11)
        ).pack(side="left", padx=30)


        # ----------------------------------------------------
        # ÁREA DE CONTEÚDO
        # ----------------------------------------------------

        self.frame_conteudo = tk.Frame(self.root)
        self.frame_conteudo.pack(fill="x", padx=30, pady=15)


        # ====================================================
        # MODO CORES -> VALOR
        # ====================================================

        self.frame_cores = tk.LabelFrame(
            self.frame_conteudo,
            text="Entrada de cores → valor do resistor",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=15
        )

        # Faixa 1
        tk.Label(
            self.frame_cores,
            text="1ª faixa:"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="e")

        self.combo_cor1 = ttk.Combobox(
            self.frame_cores,
            values=CORES_DIGITOS,
            state="readonly",
            width=18
        )
        self.combo_cor1.set("Marrom")
        self.combo_cor1.grid(row=0, column=1, padx=10, pady=8)

        # Faixa 2
        tk.Label(
            self.frame_cores,
            text="2ª faixa:"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="e")

        self.combo_cor2 = ttk.Combobox(
            self.frame_cores,
            values=CORES_DIGITOS,
            state="readonly",
            width=18
        )
        self.combo_cor2.set("Preto")
        self.combo_cor2.grid(row=1, column=1, padx=10, pady=8)

        # Faixa 3
        tk.Label(
            self.frame_cores,
            text="Multiplicador:"
        ).grid(row=2, column=0, padx=10, pady=8, sticky="e")

        self.combo_cor3 = ttk.Combobox(
            self.frame_cores,
            values=CORES_DIGITOS,
            state="readonly",
            width=18
        )
        self.combo_cor3.set("Vermelho")
        self.combo_cor3.grid(row=2, column=1, padx=10, pady=8)

        # Tolerância
        tk.Label(
            self.frame_cores,
            text="Tolerância:"
        ).grid(row=3, column=0, padx=10, pady=8, sticky="e")

        self.combo_tol_cores = ttk.Combobox(
            self.frame_cores,
            values=CORES_TOLERANCIA,
            state="readonly",
            width=18
        )
        self.combo_tol_cores.set("Dourado")
        self.combo_tol_cores.grid(row=3, column=1, padx=10, pady=8)

        # Resultado
        self.label_resultado_cores = tk.Label(
            self.frame_cores,
            text="Resistência: 1 kΩ ± 5%",
            font=("Arial", 16, "bold"),
            fg="#006400"
        )
        self.label_resultado_cores.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=20
        )

        # Eventos
        self.combo_cor1.bind("<<ComboboxSelected>>", self.atualizar_cores_valor)
        self.combo_cor2.bind("<<ComboboxSelected>>", self.atualizar_cores_valor)
        self.combo_cor3.bind("<<ComboboxSelected>>", self.atualizar_cores_valor)
        self.combo_tol_cores.bind("<<ComboboxSelected>>", self.atualizar_cores_valor)


        # ====================================================
        # MODO VALOR -> CORES
        # ====================================================

        self.frame_valor = tk.LabelFrame(
            self.frame_conteudo,
            text="Entrada de valor → cores do resistor",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=15
        )

        tk.Label(
            self.frame_valor,
            text="Valor da resistência:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.entry_valor = tk.Entry(
            self.frame_valor,
            width=20,
            font=("Arial", 12)
        )
        self.entry_valor.grid(row=0, column=1, padx=10, pady=10)
        self.entry_valor.insert(0, "3300")

        tk.Label(
            self.frame_valor,
            text="Ω"
        ).grid(row=0, column=2, padx=5)

        tk.Label(
            self.frame_valor,
            text="Tolerância:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.combo_tol_valor = ttk.Combobox(
            self.frame_valor,
            values=CORES_TOLERANCIA,
            state="readonly",
            width=18
        )
        self.combo_tol_valor.set("Dourado")
        self.combo_tol_valor.grid(row=1, column=1, padx=10, pady=10)

        self.btn_calcular = tk.Button(
            self.frame_valor,
            text="Calcular cores",
            command=self.calcular_valor_cores,
            bg="#17365D",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=5
        )
        self.btn_calcular.grid(
            row=2,
            column=0,
            columnspan=3,
            pady=15
        )

        self.label_resultado_valor = tk.Label(
            self.frame_valor,
            text="Digite um valor para calcular.",
            font=("Arial", 16, "bold"),
            fg="#006400"
        )
        self.label_resultado_valor.grid(
            row=3,
            column=0,
            columnspan=3,
            pady=15
        )

        self.entry_valor.bind(
            "<Return>",
            lambda event: self.calcular_valor_cores()
        )

        self.combo_tol_valor.bind(
            "<<ComboboxSelected>>",
            lambda event: self.calcular_valor_cores()
        )


        # ----------------------------------------------------
        # ÁREA DO RESISTOR
        # ----------------------------------------------------

        self.frame_resistor = tk.LabelFrame(
            self.root,
            text="Representação visual",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=20
        )
        self.frame_resistor.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        self.canvas = tk.Canvas(
            self.frame_resistor,
            width=780,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()


        # Texto explicativo
        self.label_info = tk.Label(
            self.root,
            text="Selecione um modo para começar.",
            font=("Arial", 10),
            fg="#555555"
        )
        self.label_info.pack(pady=(0, 10))


    # ========================================================
    # MUDAR MODO
    # ========================================================

    def atualizar_modo(self):

        if self.modo.get() == "cores":

            self.frame_valor.pack_forget()
            self.frame_cores.pack(fill="x")

            self.label_info.config(
                text="Selecione as quatro faixas para calcular o valor."
            )

            self.atualizar_cores_valor()

        else:

            self.frame_cores.pack_forget()
            self.frame_valor.pack(fill="x")

            self.label_info.config(
                text="Informe o valor da resistência para descobrir as cores."
            )

            self.calcular_valor_cores()


    # ========================================================
    # CORES -> VALOR
    # ========================================================

    def atualizar_cores_valor(self, event=None):

        cor1 = self.combo_cor1.get()
        cor2 = self.combo_cor2.get()
        cor3 = self.combo_cor3.get()
        tolerancia_cor = self.combo_tol_cores.get()

        try:
            valor = calcular_resistencia(cor1, cor2, cor3)
            tolerancia = TOLERANCIAS[tolerancia_cor]

            texto = (
                f"Resistência: {formatar_resistencia(valor)} "
                f"± {tolerancia:g}%"
            )

            self.label_resultado_cores.config(text=texto)

            self.desenhar_resistor(
                [cor1, cor2, cor3, tolerancia_cor]
            )

        except Exception as erro:
            self.label_resultado_cores.config(
                text=f"Erro: {erro}"
            )


    # ========================================================
    # VALOR -> CORES
    # ========================================================

    def calcular_valor_cores(self):

        texto = self.entry_valor.get().strip()

        try:
            valor = float(texto)

            cor1, cor2, cor3 = calcular_cores(valor)

            tolerancia_cor = self.combo_tol_valor.get()
            tolerancia = TOLERANCIAS[tolerancia_cor]

            texto_resultado = (
                f"{formatar_resistencia(valor)} → "
                f"{cor1}, {cor2}, {cor3}, {tolerancia_cor} "
                f"(± {tolerancia:g}%)"
            )

            self.label_resultado_valor.config(
                text=texto_resultado
            )

            self.desenhar_resistor(
                [cor1, cor2, cor3, tolerancia_cor]
            )

        except ValueError as erro:

            self.label_resultado_valor.config(
                text="Valor inválido."
            )

            # Desenha o resistor apenas com cores padrão
            self.desenhar_resistor(
                ["Marrom", "Preto", "Vermelho", "Dourado"]
            )


    # ========================================================
    # DESENHAR RESISTOR
    # ========================================================

    def desenhar_resistor(self, cores):

        self.canvas.delete("all")

        # Coordenadas
        centro_y = 125

        inicio = 100
        fim = 680

        corpo_inicio = 230
        corpo_fim = 550

        # ----------------------------------------------------
        # Fios
        # ----------------------------------------------------

        self.canvas.create_line(
            inicio,
            centro_y,
            corpo_inicio,
            centro_y,
            fill="#555555",
            width=6
        )

        self.canvas.create_line(
            corpo_fim,
            centro_y,
            fim,
            centro_y,
            fill="#555555",
            width=6
        )

        # ----------------------------------------------------
        # Corpo do resistor
        # ----------------------------------------------------

        self.canvas.create_polygon(
            corpo_inicio,
            centro_y - 55,
            corpo_inicio + 35,
            centro_y - 75,
            corpo_fim - 35,
            centro_y - 75,
            corpo_fim,
            centro_y - 55,
            corpo_fim,
            centro_y + 55,
            corpo_fim - 35,
            centro_y + 75,
            corpo_inicio + 35,
            centro_y + 75,
            corpo_inicio,
            centro_y + 55,
            fill="#D9B382",
            outline="#8B6F47",
            width=2
        )

        # ----------------------------------------------------
        # Faixas
        # ----------------------------------------------------

        larguras = [30, 30, 30, 30]

        posicoes = [
            300,
            370,
            440,
            500
        ]

        for i, cor in enumerate(cores):

            x = posicoes[i]
            largura = larguras[i]

            self.canvas.create_rectangle(
                x,
                centro_y - 75,
                x + largura,
                centro_y + 75,
                fill=CORES[cor],
                outline="#333333",
                width=1
            )



        nomes = [
            "1ª",
            "2ª",
            "3ª",
            "Tol."
        ]

        for i, texto in enumerate(nomes):

            x = posicoes[i] + larguras[i] / 2

            cor_texto = "white"

            if cores[i] in ["Amarelo", "Branco"]:
                cor_texto = "black"

            self.canvas.create_text(
                x,
                centro_y + 100,
                text=texto,
                font=("Arial", 10, "bold"),
                fill="#333333"
            )

  

        legenda = "   |   ".join(
            f"{i + 1}: {cor}"
            for i, cor in enumerate(cores)
        )

        self.canvas.create_text(
            390,
            30,
            text=legenda,
            font=("Arial", 11, "bold"),
            fill="#333333"
        )




if __name__ == "__main__":

    root = tk.Tk()

    app = SAPZApp(root)

    root.mainloop()