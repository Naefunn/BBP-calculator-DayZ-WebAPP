from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define materials needed for each building type
materials = {
    'Large Wall': {'nails': 20, 'planks': 11},
    'Large Door': {'nails': 30, 'planks': 15},
    'Small Door' : {'nails': 30, 'planks': 13},
    'Garage Door': {'nails': 22, 'planks': 12},
    'Large Floor': {'nails': 20, 'planks': 13},
    'Large Roof': {'nails': 20, 'planks': 13},
    'Foundation': {'nails': 20, 'planks': 8, 'logs': 2},
    # Add more building types as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    quantities = {
        'Large Wall': int(request.form.get('quantity_large_wall', 0)),
        'Large Door': int(request.form.get('quantity_large_door', 0)),
        'Small Door': int(request.form.get('quantity_small_door', 0)),
        'Garage Door': int(request.form.get('quantity_garage_door', 0)),
        'Large Floor': int(request.form.get('quantity_large_floor', 0)),
        'Large Roof': int(request.form.get('quantity_large_roof', 0)),
        'Foundation': int(request.form.get('quantity_foundation', 0)),
    }

    total_nails = 0
    total_planks = 0
    total_logs = 0

    for building_type, quantity in quantities.items():
        if building_type in materials:
            total_nails += materials[building_type]['nails'] * quantity
            total_planks += materials[building_type]['planks'] * quantity

            # Check if 'logs' is present in the material requirements
            if 'logs' in materials[building_type]:
                total_logs += materials[building_type]['logs'] * quantity
        else:
            print(f"Building type '{building_type}' not found in the materials dictionary.")

    result = {'nails': total_nails, 'planks': total_planks, 'logs': total_logs}

    return render_template('result.html', result=result)

if __name__ == '__main__':
    # Use the PORT environment variable if provided by Heroku, or default to 5000 for local development
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
