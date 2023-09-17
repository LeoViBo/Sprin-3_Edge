# Sprin-3_Edge
---- Grupo - International Business of FIAP (IBF):

RM92699 - Arielly Gleice Geovana de Oliveira
RM97673 - Tulio Damaceno de Resende
RM551869 - Fabrizio Maia Apparicio
RM551684 - Victor Miguel Gouveia Asfur
RM551715 - Leonardo Viotti Bonini

---- Explicação do Projeto

Nosso projeto é usar uma válvula que, quando instalada em um cano, detecta o fluxo de água que está passando pelo cano, e depois informa para um aplicativo para o usuário o quanto de água esta sendo gasta. Para simularmos o projeto usamos potenciometros para servir de fluxo de água e usamos o LCD como uma forma de verificar pelo hardware a fluxo de água como um health check assim como luzes led que ligam e desligam o projeto por meio de um botão, funcionando quando precionado.

Para nossa arquitetura IoT seria o arduino com um módulo de bluetooth que se conecta a celulares onde temos um aplicativo que irá se conectar com as vávlulas permitindo a transferencia de dados para passar o fluxo de água e abrir e fechar a válvula. Além de outras informações mostradas somente no aplicativo como o nome da valvula, em que parte da casa está instalada e em que tipo de imovel está instalado, residencia, comercial, industrial, etc... para que em outra parte da aplicação seja feito um cálculo que estipula o valor da conta de água. Para melhor entendimento coloquei um arquivo em .py onde fizemos a simulação dessa aplicação.

Para a versão final do nosso produto precisamos ter o sensor de água, o módulo de bluetooth do arduino, luzes led (para checar funcionamento), e o arduino uno além de um aplicativo que irá receber, mostrar e computar os dados para o usuário ver.

Para testar a aplicação em pyhton (arquivo 'Aplicacao.py') basta abrir o arquivo no pycharm e dar start. Para testar o projeto é preciso reproduzi-lo no simulid ou com as peças (com o link abaixo do tinkercad mas com o código disponibilizado no git) e importar o projeto 'Sprint 3 - Arquivo do node-red.json' para o node-red, e colocar corretamente a porta que está conectada no arduino. (Aviso: ter mais de um flow ao mesmo tempo pode causar problemas a aplicação)

Link do Tinkercad: https://www.tinkercad.com/things/1VEjGuj8NL9-projeto-final/editel?sharecode=xxMTsl_60qvQOiNnMGz9cqCO0B9_iPVfIEiUiCgyoBk

---- Link da apresentação

Youtube: 

---- Dados do node

Inclui no RAR o arquivo do node, mas segue aqui em texto

[
    {
        "id": "e22e59af75800901",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "bc609e598bcbd17a",
        "type": "serial in",
        "z": "e22e59af75800901",
        "name": "",
        "serial": "14a631cf4e51746a",
        "x": 50,
        "y": 280,
        "wires": [
            [
                "6a38303229b4a73d"
            ]
        ]
    },
    {
        "id": "6a38303229b4a73d",
        "type": "json",
        "z": "e22e59af75800901",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 210,
        "y": 280,
        "wires": [
            [
                "be3eafd97ed2da37",
                "58fb485ade419d23"
            ]
        ]
    },
    {
        "id": "7f1cfc0f87f8bc88",
        "type": "ui_gauge",
        "z": "e22e59af75800901",
        "name": "",
        "group": "4fe8948ab89c3ecc",
        "order": 2,
        "width": 0,
        "height": 0,
        "gtype": "wave",
        "title": "Fluxo da água na valvula 1",
        "label": "ml",
        "format": "{{value}}",
        "min": 0,
        "max": "10000000",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "diff": false,
        "className": "",
        "x": 660,
        "y": 280,
        "wires": []
    },
    {
        "id": "be3eafd97ed2da37",
        "type": "change",
        "z": "e22e59af75800901",
        "name": "",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.volumeTotal",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 400,
        "y": 280,
        "wires": [
            [
                "7f1cfc0f87f8bc88"
            ]
        ]
    },
    {
        "id": "58fb485ade419d23",
        "type": "debug",
        "z": "e22e59af75800901",
        "name": "debug 1",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 380,
        "y": 220,
        "wires": []
    },
    {
        "id": "14a631cf4e51746a",
        "type": "serial-port",
        "serialport": "COM5",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "waitfor": "",
        "dtr": "none",
        "rts": "none",
        "cts": "none",
        "dsr": "none",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": "",
        "responsetimeout": "10000"
    },
    {
        "id": "4fe8948ab89c3ecc",
        "type": "ui_group",
        "name": "Volume de água",
        "tab": "63cd4ad5688b6cb7",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "63cd4ad5688b6cb7",
        "type": "ui_tab",
        "name": "Sprint3",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
