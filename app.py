from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet<h1/>
  <p>Browse through the links below to find your new furry friend:<p/> 
<ul>
<li><a href='/animals/dogs'>Dogs</a></li> 
<li><a href='/animals/cats'>cats </a> </li> 
<li><a href='/animals/rabbits'>rabbits</a></li> 
</ul>
  
  '''


@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}<h1/>'
  return html


# Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
# Detta för att säkerställa en korrekt uppstart av servern.
app.run(debug=True, host="0.0.0.0")
