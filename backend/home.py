from fastapi.responses import HTMLResponse


def home():
    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>MacrosBD</title>
</head>

<body>
    <header>
        <nav>
            <a href="index.html">Home</a>
        </nav>
    </header>

    <main>
        <div>
            <h1>Bem vindo ao MacrosDB</h1>
            <p>Este aplicativo reúne informações sobre os macronutrientes dos alimentos que você ingere no dia a dia. Se quiser saber um pouco mais sobre sua nutrição diária, sinta-se a vontade para pesquisar no nosso banco de dados.</p>
        </div>
        <section>
            <table border="1">
                <tr>
                    <th>Nome</th>
                    <th>Proteínas</th>
                    <th>Carboidratos</th>
                    <th>Gorduras</th>
                </tr>

                <tr>
                    <td>Batata</td>
                    <td>10</td>
                    <td>20</td>
                    <td>30</td>
                </tr>

                <tr>
                    <td>Carne</td>
                    <td>20</td>
                    <td>1</td>
                    <td>34</td>
                </tr>
            </table>
        </section>

        <div>
            <button>Pesquisar</button>
            <button>Inserir alimento</button>
        </div>
    </main>


    <footer>
        <p>Para mais informações acesse: http://127.0.0.1:8000/docs</p>
    </footer>
</body>
</html>
"""
    return HTMLResponse(html)