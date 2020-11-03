# Descoberta Automática de Servidor
Implementação de descoberta automática de servidor usando python e rpyc, nos conformes do solicitado pelo professor da disciplina de sistemas distribuídos.


Os arquivos `client.py` e `server.py` foram criados à partir do código apresentado nos slides, enquanto o arquivo `directory_server.py` foi desenvolvido à partir dos conceitos apresentados e do próprio `server.py`. O projeto completo implementa como exemplo uma funcionalidade de cálculo de Índice de Massa Corporal, à partir das entradas do usuário, usando RPC.


O arquivo `client.py` implementa um cliente que, a princípio, usa o servidor de diretórios para descobrir o endereço ip e porta de um servidor de aplicação, do qual, a princípio, só se tem o nome. Em seguida, o cliente recebe a entrada do usuário e envia os valores para o servidor. Ao receber o valor do IMC do servidor, exibe o resultado da análise do valor para o usuário.


O arquivo `server.py` implementa o servidor que faz os cálculos de IMC quando solititado pelo cliente. O servidor também tem a capacidade de se registrar no servidor de diretório e de remover seu registro.


O arquivo `directory_server.py` implementa o servidor de diretório, que permite que um cliente descubra o nome e porta do servidor que oferece os serviços buscados e permite que um servidor se registre e apague seus registros no servidor de diretórios via RPC.


Por fim, o arquivo `const.py` armazena as constantes utilizadas por todos os programas: endereço ip do servidor de diretório, porta do servidor de diretório, nome do servidor de aplicação e porta do servidor de aplicação. Os demais arquivos presentes devem servir para auxílio geral.

## Instruções:
Para executar o projeto, abrir uma janela de terminal no diretório onde foi feita a clonagem deste repositório e executar:

```
$ python3 -m venv ./.venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
```
Isso criará o ambiente virtual python, o ativará e instalará os requisitos no ambiente virtual. Em seguida, abrir o arquivo `const.py` e inserir o endereço ip do servidor de diretórios entre as aspas na primeira linha. Os outros campos permitem alterar, respectivamente, a porta usada pelo servidor de diretório, o nome usado pelo servidor de aplicação e a porta usada pelo servidor de aplicação. Feito isso, executar um dos três módulos pretendidos, usando:
```
$ python3 client.py
$ python3 server.py
$ python3 directory_server.py
```
Vale ressaltar que a execução do `server.py` requer que uma instância do `directory_server.py` esteja sendo executada, e que a execução do `client.py` requer uma instância em execução de ambos, `directory_server.py` e `server.py`.