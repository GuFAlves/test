from flask import Flask, jsonify
from datetime import datetime
from pathlib import Path
import os

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "automacao_demo.log"

LOG_DIR.mkdir(exist_ok=True)


def registrar_log(mensagem: str, nivel: str = "INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] [{nivel}] {mensagem}\n"
    with LOG_FILE.open("a", encoding="utf-8") as arquivo:
        arquivo.write(linha)


@app.get("/")
def home():
    return jsonify({
        "nome": "automacao-demo-portalrpa",
        "status": "ok",
        "mensagem": "Automação de teste do PortalRPA ativa."
    })


@app.get("/health")
def health():
    registrar_log("Requisição em /health", "INFO")
    return jsonify({
        "status": "RUNNING",
        "servico": "automacao-demo-portalrpa",
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.get("/run")
def executar_tarefa():
    registrar_log("Iniciando execução da automação", "INFO")

    etapas = [
        "validando ambiente",
        "consultando dados de origem",
        "processando registros",
        "gravando resultado final"
    ]

    for etapa in etapas:
        registrar_log(f"Etapa: {etapa}", "INFO")

    registrar_log("Execução concluída com sucesso", "SUCCESS")

    return jsonify({
        "status": "OK",
        "automacao": "automacao-demo-portalrpa",
        "etapas": etapas,
        "ultima_execucao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.get("/status")
def status():
    registrar_log("Consulta de status solicitada", "INFO")
    return jsonify({
        "status": "RUNNING",
        "nome": "automacao-demo-portalrpa",
        "ultima_verificacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    registrar_log("Aplicação iniciada", "INFO")
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
