"""Adopt a pet application using Flask.

This Flask application allows users to browse and view information about different types of pets, including dogs, cats, and rabbits.
The application uses a separate helper.py file to store the pet data.

The application has the following routes:

- `/`: Displays the home page with links to the different types of pets.
- `/animals/<string:pet_type>`: Displays a list of all pets of the specified type.
- `/animals/<string:pet_type>/<int:pet_id>`: Displays the details of the specified pet.

The application is started by running the `app.run()` function.
"""

from flask import Flask

from helper import pets

app = Flask(__name__)


# Route to display the home page
@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet<h1/>
  <p>Browse through the links below to find your new furry friend:<p/> 
<ul>
<li><a href='/animals/dogs'>Dogs</a></li> 
<li><a href='/animals/cats'>Cats </a> </li> 
<li><a href='/animals/rabbits'>Rabbits</a></li> 
</ul>

  '''


# Route to display the list of pets based on pet type
@app.route('/animals/<string:pet_type>')
# This function displays a list of all pets of the specified type.
def animals(pet_type):
  html = f'<h1>List of {pet_type}<h1/>'
  html += '<ul>'
  for id, pet in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{id}">{pet["name"]}</a></li>'
  return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
# This function displays details about a specific pet.
def pet(pet_id, pet_type):
  """Display details about a specific pet.
  Args: 
      pet_id (int): The ID of the pet to display.
      pet_type (string): The type of pet to display.
  Returns: 
      A formatted string with the details of the specified pet.
  """
  list_pet_type = pets[pet_type]
  pet = list_pet_type[pet_id]
  return f'''
  <h1> {pet["name"]}</h1>

  <img src={pet["url"]} /> 

  <p>{pet["description"]}</p>

  <ul>
    <li>{pet["breed"]} </li>
    <li>{pet["age"]} </li>
  </ul>
  '''


# This line is important for starting the Flask server
app.run(debug=True, host="0.0.0.0")
