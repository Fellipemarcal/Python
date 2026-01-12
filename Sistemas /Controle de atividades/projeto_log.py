import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

ARQ_DADOS = "dados.csv"
ARQ_LOGS = "logs.csv"
META = 100

# =====================================================
# UTILIDADES
# =====================================================

def calcular_indice(sep, conf, erros):
    return sep + conf - (erros * 2)

def status_cor(indice):
    if indice >= META:
        return "verde"
    elif indice >= META * 0.7:
        return "amarelo"
    return "vermelho"

def gerar_id():
    if not os.path.exists(ARQ_DADOS):
        return 1
    with open(ARQ_DADOS) as f:
        ids = [int(l[0]) for l in csv.reader(f) if l]
    return max(ids, default=0) + 1

def registrar_log(acao, detalhe):
    with open(ARQ_LOGS, "a", newline="") as f:
        csv.writer(f).writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            acao,
            detalhe
        ])

# =====================================================
# DADOS
# =====================================================

def carregar_dados():
    if not os.path.exists(ARQ_DADOS):
        return []
    with open(ARQ_DADOS) as f:
        return list(csv.reader(f))

def salvar_dados(dados):
    with open(ARQ_DADOS, "w", newline="") as f:
        csv.writer(f).writerows(dados)

def carregar_logs():
    if not os.path.exists(ARQ_LOGS):
        return []
    with open(ARQ_LOGS) as f:
        return list(csv.reader(f))[-50:]

# =====================================================
# CRUD
# =====================================================

def registrar():
    try:
        sep = int(entry_sep.get())
        conf = int(entry_conf.get())
        erros = int(entry_erros.get())
    except:
        messagebox.showerror("Erro", "Valores inválidos")
        return

    nome = entry_nome.get().strip()
    if not nome:
        messagebox.showerror("Erro", "Nome obrigatório")
        return

    indice = calcular_indice(sep, conf, erros)
    status = status_cor(indice)

    dados = carregar_dados()
    novo_id = gerar_id()

    dados.append([
        novo_id, nome, sep, conf, erros,
        indice, status,
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ])

    salvar_dados(dados)
    registrar_log("REGISTROU", f"{nome} (ID {novo_id})")
    limpar_form()
    atualizar_tudo()

def editar():
    if not entry_id.get():
        return

    dados = carregar_dados()
    for d in dados:
        if str(d[0]) == entry_id.get():
            d[1] = entry_nome.get()
            d[2] = entry_sep.get()
            d[3] = entry_conf.get()
            d[4] = entry_erros.get()
            d[5] = calcular_indice(int(d[2]), int(d[3]), int(d[4]))
            d[6] = status_cor(d[5])
            d[7] = datetime.now().strftime("%Y-%m-%d %H:%M")
            registrar_log("EDITOU", f"{d[1]} (ID {d[0]})")

    salvar_dados(dados)
    limpar_form()
    atualizar_tudo()

def excluir():
    if not entry_id.get():
        return
    if not messagebox.askyesno("Confirmação", "Deseja excluir este registro?"):
        return

    dados = carregar_dados()
    dados = [d for d in dados if str(d[0]) != entry_id.get()]
    salvar_dados(dados)

    registrar_log("EXCLUIU", f"ID {entry_id.get()}")
    limpar_form()
    atualizar_tudo()

# =====================================================
# LOGS (TELA SEPARADA)
# =====================================================

def abrir_logs():
    win = tk.Toplevel(root)
    win.title("📜 Histórico de Logs")
    win.geometry("800x300")

    tree = ttk.Treeview(win, columns=("Data", "Ação", "Detalhe"), show="headings")
    for c in ("Data", "Ação", "Detalhe"):
        tree.heading(c, text=c)
        tree.column(c, width=200 if c != "Detalhe" else 380)

    tree.pack(fill="both", expand=True)

    for l in carregar_logs():
        tree.insert("", "end", values=l)

# =====================================================
# FILTROS AVANÇADOS + EXPORTAÇÃO
# =====================================================

def abrir_filtros():
    win = tk.Toplevel(root)
    win.title("🔎 Filtros Avançados")
    win.geometry("950x520")

    resultados_filtrados = []

    frame = tk.Frame(win)
    frame.pack(pady=10)

    tk.Label(frame, text="Filtrar por Nome ou ID:").grid(row=0, column=0)
    entry_filtro = tk.Entry(frame, width=30)
    entry_filtro.grid(row=0, column=1, padx=5)

    lbl_resumo = tk.Label(win, font=("Arial", 10, "bold"))
    lbl_resumo.pack(pady=5)

    tree = ttk.Treeview(
        win,
        columns=("ID", "Nome", "Sep", "Conf", "Erros", "Índice", "Status", "Data"),
        show="headings"
    )

    for c in tree["columns"]:
        tree.heading(c, text=c)
        tree.column(c, width=100)

    tree.pack(fill="both", expand=True, padx=10)

    tree.tag_configure("verde", background="#c8f7c5")
    tree.tag_configure("amarelo", background="#fff3b0")
    tree.tag_configure("vermelho", background="#f7c5c5")

    def aplicar_filtro():
        nonlocal resultados_filtrados
        resultados_filtrados = []

        termo = entry_filtro.get().strip().lower()
        dados = carregar_dados()

        tree.delete(*tree.get_children())

        total_sep = total_conf = total_erros = total_indice = 0
        encontrados = 0

        for d in dados:
            if termo in d[1].lower() or termo == str(d[0]):
                resultados_filtrados.append(d)
                encontrados += 1
                total_sep += int(d[2])
                total_conf += int(d[3])
                total_erros += int(d[4])
                total_indice += int(d[5])

                tree.insert("", "end", values=d, tags=(d[6],))

        lbl_resumo.config(
            text=(
                f"Registros: {encontrados} | "
                f"Separação: {total_sep} | "
                f"Conferência: {total_conf} | "
                f"Erros: {total_erros} | "
                f"Índice Total: {total_indice}"
            )
        )

    def exportar_filtro_excel():
        if not resultados_filtrados:
            messagebox.showwarning("Aviso", "Nenhum dado filtrado.")
            return

        wb = Workbook()
        ws = wb.active
        ws.append(["ID", "Nome", "Separação", "Conferência", "Erros", "Índice"])

        total_sep = total_conf = total_erros = total_indice = 0

        for d in resultados_filtrados:
            ws.append(d[:6])
            total_sep += int(d[2])
            total_conf += int(d[3])
            total_erros += int(d[4])
            total_indice += int(d[5])

        ws.append([])
        ws.append(["TOTAL", "", total_sep, total_conf, total_erros, total_indice])

        chart = BarChart()
        data = Reference(ws, min_col=6, min_row=1, max_row=len(resultados_filtrados)+1)
        cats = Reference(ws, min_col=2, min_row=2, max_row=len(resultados_filtrados)+1)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        ws.add_chart(chart, "H2")

        nome = f"relatorio_filtro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        wb.save(nome)
        messagebox.showinfo("Sucesso", f"Arquivo gerado:\n{nome}")

    tk.Button(frame, text="Aplicar Filtro", command=aplicar_filtro).grid(row=0, column=2, padx=5)
    tk.Button(frame, text="📤 Exportar Excel", command=exportar_filtro_excel).grid(row=0, column=3, padx=5)

# =====================================================
# GRÁFICOS
# =====================================================

def atualizar_grafico():
    dados = carregar_dados()
    nomes = [d[1] for d in dados]
    indices = [int(d[5]) for d in dados]

    ax.clear()
    ax.bar(nomes, indices)
    ax.axhline(META, linestyle="--")
    ax.set_title("Desempenho Geral da Equipe")
    canvas.draw()

def grafico_individual():
    if not entry_id.get():
        return
    for d in carregar_dados():
        if str(d[0]) == entry_id.get():
            plt.figure()
            plt.bar(["Separação", "Conferência", "Erros"],
                    [int(d[2]), int(d[3]), int(d[4])])
            plt.title(f"Desempenho - {d[1]}")
            plt.show()

# =====================================================
# UI PRINCIPAL
# =====================================================

root = tk.Tk()
root.title("Gestão de Logística")

frame = tk.Frame(root)
frame.pack(pady=5)

labels = ["ID", "Nome", "Separação", "Conferência", "Erros"]
entries = []

for i, l in enumerate(labels):
    tk.Label(frame, text=l).grid(row=i, column=0)
    e = tk.Entry(frame, width=25)
    e.grid(row=i, column=1)
    entries.append(e)

entry_id, entry_nome, entry_sep, entry_conf, entry_erros = entries
entry_id.config(state="readonly")

tk.Button(frame, text="Registrar", command=registrar).grid(row=5, column=0)
tk.Button(frame, text="Editar", command=editar).grid(row=5, column=1)
tk.Button(frame, text="Excluir", command=excluir).grid(row=6, column=0)
tk.Button(frame, text="Gráfico Funcionário", command=grafico_individual).grid(row=6, column=1)
tk.Button(frame, text="📜 Logs", command=abrir_logs).grid(row=7, column=0)
'''tk.Button(frame, text="📊 Excel Geral", command=exportar_excel).grid(row=7, column=1)'''
tk.Button(frame, text="🔎 Filtros Avançados", command=abrir_filtros).grid(row=8, column=0, columnspan=2, pady=5)

tree = ttk.Treeview(
    root,
    columns=("ID", "Nome", "Sep", "Conf", "Erros", "Índice", "Status", "Data"),
    show="headings"
)
for c in tree["columns"]:
    tree.heading(c, text=c)
tree.pack(fill="both", expand=True)

tree.tag_configure("verde", background="#c8f7c5")
tree.tag_configure("amarelo", background="#fff3b0")
tree.tag_configure("vermelho", background="#f7c5c5")

def selecionar(event):
    item = tree.selection()
    if not item:
        return
    v = tree.item(item)["values"]

    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.insert(0, v[0])
    entry_id.config(state="readonly")

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, v[1])
    entry_sep.delete(0, tk.END)
    entry_sep.insert(0, v[2])
    entry_conf.delete(0, tk.END)
    entry_conf.insert(0, v[3])
    entry_erros.delete(0, tk.END)
    entry_erros.insert(0, v[4])

tree.bind("<<TreeviewSelect>>", selecionar)

fig, ax = plt.subplots(figsize=(6, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def atualizar_tudo():
    tree.delete(*tree.get_children())
    for d in carregar_dados():
        tree.insert("", "end", values=d, tags=(d[6],))
    atualizar_grafico()

def limpar_form():
    for e in [entry_id, entry_nome, entry_sep, entry_conf, entry_erros]:
        e.config(state="normal")
        e.delete(0, tk.END)
    entry_id.config(state="readonly")

atualizar_tudo()
root.mainloop()
