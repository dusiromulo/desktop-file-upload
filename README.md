# Desktop File Upload

Aplicações de desktop (testada apenas em windows) e backend com autenticação e uploads de arquivos.


## Setup para execução

Python 3.7.4 64 bit (Intel) on win32 (https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe)<br /> 
Windows 10 - 64 bit


## Instalação

Abra um prompt de comandos e caminhe até a pasta clonada (ou baixada e descomprimida) e execute os comandos:<br /> 
`pip install -r requirements.txt`


## Configuração e Execução

Para conseguir se autenticar na aplicação Desktop, é preciso criar um usuário na área administrativa de nosso backend.<br /> 

Considerando que você está na raíz deste projeto, abra o diretório file_upload_app:<br /> 
`cd file_upload_app`

Faça as migrações da aplicação e depois crie um usuário administrador:<br /> 
`python manage.py makemigrations`<br /> 
`python manage.py migrate`<br /> 
`python manage.py createsuperuser`<br /> 


Inicie o servidor:<br /> 
`python manage.py runserver 8000` 

Para criar um usuário que faz login na aplicação desktop, entre na área administrativa (http://localhost:8000/admin/) após iniciar o servidor com as credenciais criadas acima.

Após realizar login na área administrativa navegue até usuários e crie um usuário.<br /> 
Pronto, você já tem tudo para realizar uploads!

Para iniciar a aplicação desktop, caminhe até o diretório file_upload_desktop na raíz deste projeto.<br /> 
`cd ../file_upload_desktop`

E inicie a aplicação:<br /> 
`python run.py`

