from bottle import Bottle, run, template, request
from pymodbus.client import ModbusTcpClient

# Configuration EDW-100
EDW_IP = "192.168.191.100"
EDW_PORT = 502
client = ModbusTcpClient(host=EDW_IP, port=EDW_PORT)

# Initialisation de l'application Bottle
app = Bottle()

# Page principale avec boutons
@app.route('/')
def home():
    return template('''
        <html>
        <head>
            <title>Contrôle de la Barrière</title>
            <style>
                button { font-size: 20px; margin: 10px; padding: 15px; }
                #response { margin-top: 20px; font-size: 18px; color: green; }
            </style>
        </head>
        <body>
            <h1>Contrôle de la Barrière</h1>
            <button onclick="sendCommand(0)">Ouvrir</button>
            <button onclick="sendCommand(1)">Fermer</button>
            <button onclick="sendCommand(2)">Arrêter</button>
            <div id="response"></div> <!-- Div pour afficher la réponse -->
            <script>
                function sendCommand(value) {
                    fetch('/command', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: 'state=' + value
                    }).then(response => response.text()).then(function(text) {
                        document.getElementById('response').innerText = text; // Afficher la réponse ici
                    });
                }
            </script>
        </body>
        </html>
    ''')

# Route pour envoyer les commandes à l'EDW-100
@app.post('/command')
def send_command():
    coil_address = int(request.forms.get('state'))
    response = client.write_coil(address=coil_address, value=True, slave=65)
    if response.isError():
        return "Erreur lors de l'envoi de la commande."
    return f"Commande envoyée avec succès : {coil_address}"

# Lancer le serveur Bottle
if __name__ == "__main__":
    run(app, host='192.168.190.26', port=5000, debug=True)