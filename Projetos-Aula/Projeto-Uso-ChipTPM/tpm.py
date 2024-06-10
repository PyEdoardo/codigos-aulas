from tpm2_pytss import *
import sys

# Inicialize a conexão com o TPM
with TctiLdr("device") as tcti:
    esys_ctx = ESAPI(tcti)

    try:
        # Solicitar números aleatórios do TPM
        random_bytes = esys_ctx.GetRandom(16)  # Gere 16 bytes de dados aleatórios
        print("Random bytes:", random_bytes)
    except TPM2_Error as e:
        print(f"Falha ao gerar números aleatórios: {e}", file=sys.stderr)