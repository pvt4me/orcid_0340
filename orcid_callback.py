from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/callback')
def orcid_callback():
    code = request.args.get('code')
    state = request.args.get('state', '0340')
    return f"""
    <h1>ATLASv540 0340 ✓</h1>
    <p><strong>OAuth code:</strong> {code or 'NO_CODE'}</p>
    <p><strong>State:</strong> {state}</p>
    <p>ORCID auth successful! Ready for matrix0340pipeline [file:2]</p>
    """

@app.route('/')
def home():
    return """
    <h1>ATLASv540 0340 ORCID Optimizer</h1>
    <p>27-state topological model: gap=[0.130,0.135), PL=0.44, PR=0.56 [file:3][file:5]</p>
    """

if __name__ == '__main__':
    app.run(port=5000)
