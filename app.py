from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

# Charge les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Tes credentials Twilio
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Reçoit et répond aux messages WhatsApp"""
    
    # Récupère le message et le numéro de l'envoyeur
    incoming_msg = request.values.get('Body', '').lower().strip()
    sender = request.values.get('From')
    
    # Crée la réponse
    resp = MessagingResponse()
    
    # ============ LOGIQUE DU BOT ============
    
    if 'bonjour' in incoming_msg or 'salut' in incoming_msg or 'hi' in incoming_msg:
        resp.message('Bonjour ! 👋 Bienvenue !\n\nTapez "menu" pour voir nos options.')
    
    elif 'menu' in incoming_msg:
        resp.message('''📋 MENU DE NOTRE RESTAURANT:

1️⃣ Pizza Margherita - 5000 FCFA
2️⃣ Burger Cheese - 3500 FCFA
3️⃣ Pâtes Carbonara - 4500 FCFA
4️⃣ Jus Frais - 1500 FCFA

Tapez le numéro de votre choix (1, 2, 3 ou 4)''')
    
    elif '1' in incoming_msg:
        resp.message('🍕 Vous avez choisi Pizza Margherita (5000 FCFA)\n\nTapez "oui" pour commander ou "menu" pour revenir.')
    
    elif '2' in incoming_msg:
        resp.message('🍔 Vous avez choisi Burger Cheese (3500 FCFA)\n\nTapez "oui" pour commander ou "menu" pour revenir.')
    
    elif '3' in incoming_msg:
        resp.message('🍝 Vous avez choisi Pâtes Carbonara (4500 FCFA)\n\nTapez "oui" pour commander ou "menu" pour revenir.')
    
    elif '4' in incoming_msg:
        resp.message('🥤 Vous avez choisi Jus Frais (1500 FCFA)\n\nTapez "oui" pour commander ou "menu" pour revenir.')
    
    elif 'oui' in incoming_msg:
        resp.message('✅ Commande confirmée !\n\n📍 Livraison en 30 minutes\n💰 Paiement à la livraison\n\nMerci pour votre commande ! 🙏')
    
    elif 'aide' in incoming_msg or 'help' in incoming_msg:
        resp.message('📞 AIDE:\n\nTapez:\n"menu" - voir nos produits\n"bonjour" - salutation\n\nLe bot répond 24/7 !')
    
    else:
        resp.message('Sorry, je n\'ai pas compris. 🤔\n\nTapez "menu" pour voir nos options ou "aide" pour l\'aide.')
    
    # =======================================
    
    return str(resp)

@app.route('/test', methods=['GET'])
def test():
    """Route de test pour vérifier que le serveur fonctionne"""
    return '''
    <h1>✅ Bot WhatsApp Cameroun en ligne !</h1>
    <p>Envoie un message à: +14155238886</p>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
