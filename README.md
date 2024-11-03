# AmbiTECH

## TODO

- [ ] Adicionar o Django ao projeto.
- [ ] Refatorar o código para pegar o arquivo excel do banco de dados, não mais do github.
- [ ] Criar tela de login
- [ ] Criar tela com formulário incremental para o usuário adicionar o arquivo excel e escolher entre as opções disponíveis.
  - [ ] Criar componente para upload de arquivos excel.
  - [ ] Adicionar tabela com preview dos dados do arquivo excel.
  - [ ] Adicionar input para o usuário escolher o nome do arquivo que será gerado.
  - [ ] Mostrar as opções de laboratórios disponíveis e quantidade de valores orientadores.
  - [ ] Mostrar opções de valores de referência conforme escolha anterior, 2, 3 valores.
  - [ ] Mostrar opções de matriz e/ou cenário ambiental para cada valor orientador.
  - [ ] Botão para gerar analise.

---

### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at <http://localhost:8000>.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References

- [Docker's Python guide](https://docs.docker.com/language/python/)
