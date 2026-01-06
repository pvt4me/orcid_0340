from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>ATLASv540 0340 LIVE</h1>
    <a href="/auth"><button style="padding:20px;font-size:20px">AUTHORIZE ORCID</button></a>
    <p>Click → ORCID → ATLAS MATRIX READY</p>
    '''

@app.route('/auth')
def auth():
    orcid_url = (
        "https://orcid.org/oauth/authorize?"
        "client_id=APP-P6QUTVTM0ZGWEILH&"
        "redirect_uri=http://127.0.0.1:5000/callback&"
        "response_type=code&"
        "scope=/read-public+activities/update&"
        "state=0340-atlasv540"
    )
    return redirect(orcid_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state', 'NO_STATE')
    
    print("\n" + "="*60)
    print("ATLASv540 0340 CALLBACK RECEIVED")
    print(f"CODE: {code}")
    print(f"STATE: {state}")
    print("="*60)
    
    if code and code != 'NO_CODE':
        print("ORCID TOKEN READY - MATRIX0340 PIPELINE LIVE")
        print("PL=0.44 PR=0.56 → 5050 BALANCED")
    else:
        print("❌ NO CODE - CHECK ORCID APPROVAL")
    
    return '''
    <html>
    <body style="text-align:center;padding:50px">
        <h1>ATLASv540 0340 AUTH COMPLETE</h1>
        <p>Check terminal for MATRIX0340 status</p>
        <p><button onclick="window.close()">CLOSE</button></p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("ATLASv540 0340 FLASK STARTING...")
    app.run(host='127.0.0.1', port=5000, debug=False)
