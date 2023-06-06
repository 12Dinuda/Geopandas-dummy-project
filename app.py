from flask import Flask, render_template, request
import folium
import geopandas as gpd

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        button_value = request.form.get('button')
        if button_value == 'on':
            # Set display_map to True if button value is 'on'
            display_map = True
        else:
            # Set display_map to False if button value is not 'on'
            display_map = False
        return render_template('dummy_map.html', display_map=display_map)
    else:
        # Render the index.html template for GET requests
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
