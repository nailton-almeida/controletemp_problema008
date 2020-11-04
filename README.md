# Sistema Gerenciador de Controle de Temperatura

Neste repositório estão todos os arquivos necessários para a implementação de um dashboard para controle de temperatura de um cofre.

<br />

## Estrutura do código

Abaixo segue estrutura dos diretórios e arquivos da aplicação.


```bash
< ROOT pasta front-end >
   |
   |-- app/                                      # Pasta com todos os elementos gráficos da aplicação
   |    |-- home/                                # Demais áreas do sistema
   |    |-- base/                                # Área de login do sistema
   |         |-- static/
   |         |    |-- <css, JS, images>          # CSS, Javascripts 
   |         |
   |         |-- templates/                      # Páginas HTML
   |              |
   |              |-- includes/                  # Menu lateral
   |              |    |-- navigation.html       
   |              |    |-- sidebar.html          
   |              |    |-- footer.html           
   |              |    |-- scripts.html          
   |              |
   |              |-- layouts/                  
   |              |    |-- base-fullscreen.html  
   |              |    |-- base.html             
   |              |
   |              |-- accounts/                  
   |                   |-- login.html            
   |                   |-- register.html         
   |
   |-- termometro_file.py                        # Publica dados através do protocolo MQTT
   |-- environment_state.py                      # Realiza controle de temperatura
   |-- gerenciador.py                            # Lê os dados no broker MQTT
   |-- gera_graficos.py                          # Função cria os gráficos do sistema
   |
   |-- .env                                      # Inject Configuration via Environment
   |-- config.py                                 # Configurações inicias Flask
   |-- run.py                                    # Inicia a aplicação aplicação
   |
   |-- ************************************************************************
```

<br />

