import psycopg2 as banco
import datetime

def viewNoticiasReportagem():
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()

    cursor.execute(
        "select * from vw_noticia_reportagem"
    )
    retorno: list = cursor.fetchall()
    cursor.close()
    conexao.close()
    return retorno



def inserirCategoria(*titulos):
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()
    for titulo in titulos:
        cursor.execute(
            f"INSERT INTO categoria (titulo) values (%s)", (titulo,)
        )
    conexao.commit()
    cursor.close()
    conexao.close()
    
def atualizarCategoria(id: int, titulo: str):
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE categoria SET titulo = %s WHERE codigo = %s", (titulo, id,)
    )
    conexao.commit()

    cursor.close()
    conexao.close()

def pegarCategorias():
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT titulo FROM categoria"
    )
    retorno: list = cursor.fetchall()
    cursor.close()
    conexao.close()
    return retorno
    
def pegarCategoria(nome: str):
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM categoria c WHERE c.titulo like %s", (f'%{nome}',)
    )
    retorno: list = cursor.fetchall()
    cursor.close()
    conexao.close()
    return retorno

def apagarCategoria(id: int):
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM categoria WHERE codigo = %s", (id,)
    )
    conexao.commit()

    cursor.close()
    conexao.close()


def inserirNoticia(nome: str, descricao: str, codigo_noticia: int):
    conexao = banco.connect(
        user="postgres.rglddhvexqcriqanscut",
        password="G8jkBZ3eW2msTDiD",
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=5432,
        dbname="postgres"
    )
    cursor = conexao.cursor()
    cursor.execute(
        f"INSERT INTO noticia (nome, descricao, data_criacao, codigo_categoria) values (%s, %s, %s, %d)", (nome, descricao, datetime.time())
    )
    conexao.commit()
    cursor.close()
    conexao.close()

#inserirCategoria(input("Digite a Categoria"))
#atualizarCategoria(1, "Reportagem 2")
print(pegarCategorias())
#apagarCategoria(1)

print(pegarCategoria("Reportagem"))
print(viewNoticiasReportagem())








