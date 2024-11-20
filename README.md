# Automação de Upload de Blacklist/Whitelist

Este projeto é uma automação que utiliza Python e Selenium para realizar o upload de um arquivo CSV no sistema de importação da plataforma [SIV]. O script faz alterações nos CPFs do arquivo e realiza o upload de acordo com as configurações definidas.

## **Funcionalidades**
- Modificar os CPFs no arquivo CSV antes do upload.
- Acessar a plataforma SIV TradeApp e realizar o login automaticamente.
- Selecionar o tipo de importação (BLACK-WHITE-LIST).
- Enviar o arquivo atualizado para a plataforma.
- Confirmar a importação com um clique automatizado.

## **Pré-requisitos**
1. **Python**: Certifique-se de ter o Python 3.8 ou superior instalado.
2. **Pacotes Necessários**:
   - `selenium`
   - `python-dotenv`
3. **WebDriver**: Baixe e configure o ChromeDriver compatível com sua versão do Google Chrome. Disponível em: [ChromeDriver](https://sites.google.com/chromium.org/driver/).

## **Configuração**
### 1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```plaintext
TRADEAPP_USERNAME=seu_usuario
TRADEAPP_PASSWORD=sua_senha
```

**Nota:** Adicione o arquivo `.env` ao `.gitignore` para não expor credenciais sensíveis.

### 4. Verifique o arquivo CSV
Certifique-se de que o arquivo `black_list.csv` está localizado no caminho definido no script.

---

## **Uso**
Execute o script para realizar a automação:

```bash
python black_list.py
```

### Etapas realizadas:
1. O script solicita um CPF para substituir os valores no arquivo CSV.
2. Faz login na plataforma SIV TradeApp.
3. Seleciona o tipo de importação (BLACK-WHITE-LIST).
4. Faz o upload do arquivo atualizado.
5. Confirma a importação automaticamente.

---

## **Atenção**
- Verifique a compatibilidade do ChromeDriver com a sua versão do Google Chrome.
- O campo `CPF` no arquivo CSV deve estar configurado corretamente como texto.
- O script utiliza seletores dinâmicos para identificar elementos na plataforma. Caso a estrutura do site seja alterada, ajustes poderão ser necessários.

---

## **Licença**
Este projeto é de uso pessoal e não deve ser utilizado para fins comerciais sem autorização.

---

## **Contribuições**
Sinta-se à vontade para contribuir com melhorias para este projeto! Abra uma issue ou envie um pull request.

---

## **Contato**
Para dúvidas ou suporte, entre em contato com Gabriel Galdino (mailto:gabrielcgaldiino@gmail.com).🚀
```
