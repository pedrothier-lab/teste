import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# CALCULADORA DE RESISTOR
# Interface baseada no exemplo enviado.
# ============================================================

CORES = {
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

}


def formatar(valor):
    if valor >= 1_000_000:
        return f"{valor / 1_000_000:g} MΩ"
    if valor >= 1_000:
        return f"{valor / 1_000:g} kΩ"
    return f"{valor:g} Ω"


class App:
    def __init__(self, janela):
        self.janela = janela

        janela.title("Calculadora de Resistor")
        janela.geometry("730x600")
        janela.resizable(False, False)
        janela.configure(bg="#eaf2f5")

        self.modo = tk.StringVar(value="cores")
        self.valor = tk.StringVar()

        self.criar_estilos()
        self.criar_interface()

    def criar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TCombobox",
            fieldbackground="#deddd8",
            background="#deddd8",
            foreground="#222222",
            padding=3
        )

        estilo.configure(
            "Calcular.TButton",
            background="#38a89b",
            foreground="white",
            font=("Arial", 11, "bold"),
            padding=(9, 7)
        )

        estilo.map(
            "Calcular.TButton",
            background=[
                ("active", "#2f9489"),
                ("pressed", "#287e74")
            ]
        )

    def criar_interface(self):
        # Título externo da janela
        tk.Label(
            self.janela,
            text="Calculadora de Resistor",
            bg="#eaf2f5",
            fg="#23384b",
            font=("Arial", 20, "bold"),
            anchor="w"
        ).place(x=28, y=25)

        # Área branca principal
        painel = tk.Frame(
            self.janela,
            bg="white",
            highlightbackground="#e0e5e8",
            highlightthickness=1
        )
        painel.place(x=28, y=88, width=674, height=508)

        # Pergunta
        tk.Label(
            painel,
            text="Como deseja informar o resistor?",
            bg="white",
            fg="#24384b",
            font=("Arial", 11, "bold")
        ).place(x=20, y=20)

        # Radio: valor
        tk.Radiobutton(
            painel,
            text="Valor da resistência",
            variable=self.modo,
            value="valor",
            command=self.mudar_modo,
            bg="white",
            activebackground="white",
            font=("Arial", 10),
            cursor="hand2"
        ).place(x=20, y=51)

        # Radio: cores
        tk.Radiobutton(
            painel,
            text="Cores do resistor",
            variable=self.modo,
            value="cores",
            command=self.mudar_modo,
            bg="white",
            activebackground="white",
            font=("Arial", 10),
            cursor="hand2"
        ).place(x=190, y=51)

        # Área dos controles
        self.area_cores = tk.Frame(painel, bg="white")
        self.area_cores.place(x=20, y=96, width=634, height=78)

        nomes = [
            ("Banda 1:", "banda1", 0),
            ("Banda 2:", "banda2", 160),
            ("Multiplicador:", "multiplicador", 320),
            ("Tolerância:", "tolerancia", 480)
        ]

        self.combos = {}

        for texto, nome, x in nomes:
            tk.Label(
                self.area_cores,
                text=texto,
                bg="white",
                fg="#334655",
                font=("Arial", 10)
            ).place(x=x, y=0)

            combo = ttk.Combobox(
                self.area_cores,
                state="readonly",
                style="TCombobox",
                width=14
            )

            if nome in ("banda1", "banda2"):
                combo["values"] = list(CORES.keys())
            elif nome == "multiplicador":
                combo["values"] = list(MULTIPLICADORES.keys())
            else:
                combo["values"] = list(TOLERANCIAS.keys())

            combo.place(x=x, y=25, width=142, height=32)
            self.combos[nome] = combo

        # Campo de valor (fica escondido no modo cores)
        self.area_valor = tk.Frame(painel, bg="white")

        tk.Label(
            self.area_valor,
            text="Valor da resistência (Ω):",
            bg="white",
            fg="#334655",
            font=("Arial", 10)
        ).pack(anchor="w")

        tk.Entry(
            self.area_valor,
            textvariable=self.valor,
            font=("Arial", 11),
            relief="solid",
            bd=1
        ).pack(fill="x", pady=(6, 0), ipady=5)

        # Botão
        ttk.Button(
            painel,
            text="Calcular resistência",
            style="Calcular.TButton",
            command=self.calcular,
            cursor="hand2"
        ).place(x=20, y=185, width=162, height=39)

        # Mensagem
        self.mensagem = tk.Label(
            painel,
            text="Digite o valor da resistência ou selecione as cores.",
            bg="white",
            fg="#142a3d",
            font=("Arial", 10, "bold"),
            anchor="w"
        )
        self.mensagem.place(x=20, y=242)

        # Caixa de resultado
        self.resultado = tk.Text(
            painel,
            bg="#fafbfc",
            fg="#777777",
            font=("Arial", 11),
            relief="solid",
            bd=1,
            wrap="word",
            padx=15,
            pady=12
        )
        self.resultado.place(x=20, y=278, width=634, height=190)

        self.mostrar("Aguarde a seleção do modo")

    def mudar_modo(self):
        if self.modo.get() == "cores":
            self.area_valor.place_forget()
            self.area_cores.place(x=20, y=96, width=634, height=78)
            self.mensagem.config(
                text="Digite o valor da resistência ou selecione as cores."
            )
        else:
            self.area_cores.place_forget()
            self.area_valor.place(x=20, y=96, width=634, height=78)
            self.mensagem.config(
                text="Digite o valor da resistência."
            )

        self.mostrar("Aguarde a seleção do modo")

    def mostrar(self, texto):
        self.resultado.config(state="normal")
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)
        self.resultado.config(state="disabled")

    def calcular(self):
        try:
            if self.modo.get() == "cores":
                self.calcular_cores()
            else:
                self.calcular_valor()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def calcular_cores(self):
        b1 = self.combos["banda1"].get()
        b2 = self.combos["banda2"].get()
        mult = self.combos["multiplicador"].get()
        tol = self.combos["tolerancia"].get()

        if not all((b1, b2, mult, tol)):
            raise ValueError("Selecione todas as opções do resistor.")

        resistencia = (
            (CORES[b1] * 10 + CORES[b2])
            * MULTIPLICADORES[mult]
        )

        tolerancia = TOLERANCIAS[tol]
        minimo = resistencia * (1 - tolerancia / 100)
        maximo = resistencia * (1 + tolerancia / 100)

        texto = (
            f"Resistência: {formatar(resistencia)}\n\n"
            f"Tolerância: ±{tolerancia:g}%\n"
            f"Valor mínimo: {formatar(minimo)}\n"
            f"Valor máximo: {formatar(maximo)}"
        )

        self.mostrar(texto)

    def calcular_valor(self):
        entrada = self.valor.get().strip().replace(",", ".")

        if not entrada:
            raise ValueError("Digite o valor da resistência.")

        try:
            resistencia = float(entrada)
        except ValueError:
            raise ValueError("Digite um número válido.")

        if resistencia <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        # Procura duas algarismos significativos.
        expoente = 0
        numero = resistencia

        while numero >= 100:
            numero /= 10
            expoente += 1

        while numero < 10:
            numero *= 10
            expoente -= 1

        primeiro = int(numero)
        segundo = int(round((numero - primeiro) * 10))

        if segundo == 10:
            primeiro += 1
            segundo = 0
            expoente += 1

        multiplicador = 10 ** expoente

        if primeiro not in range(10) or segundo not in range(10):
            raise ValueError("Não foi possível converter o valor.")

        cor1 = next(c for c, v in CORES.items() if v == primeiro)
        cor2 = next(c for c, v in CORES.items() if v == segundo)

        cor_mult = None
        for cor, valor in MULTIPLICADORES.items():
            if valor == multiplicador:
                cor_mult = cor
                break

        if cor_mult is None:
            raise ValueError(
                "Esse valor não corresponde a um multiplicador padrão."
            )

        texto = (
            f"Valor: {formatar(resistencia)}\n\n"
            f"Banda 1: {cor1}\n"
            f"Banda 2: {cor2}\n"
            f"Multiplicador: {cor_mult}"
        )

        self.mostrar(texto)


if __name__ == "__main__":
    janela = tk.Tk()
    App(janela)
    janela.mainloop()
