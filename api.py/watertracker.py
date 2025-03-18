from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_water_intake(weight, age, activity_level):
    """
    Calculate the recommended daily water intake based on the user's weight, age, and activity level.
    
    :param weight: Weight of the user in pounds.
    :param age: Age of the user in years.
    :param activity_level: Activity level of the user as a number (1 for sedentary, 2 for moderate, 3 for active).
    :return: Recommended daily water intake in gallons.
    """
    # Convert weight from pounds to kilograms
    weight_kg = weight * 0.453592
    
    # Basic water intake based on weight (in liters)
    water_intake_liters = weight_kg * 0.033  # 33 ml per kg of body weight
    
    # Adjust based on activity level
    if activity_level == 1:  # Sedentary
        water_intake_liters *= 1.0  # No increase for sedentary people
    elif activity_level == 2:  # Moderate
        water_intake_liters *= 1.2  # 20% increase for moderate activity
    elif activity_level == 3:  # Active
        water_intake_liters *= 1.4  # 40% increase for active people
    
    # Adjust based on age (e.g., older adults may need more water)
    if age > 60:
        water_intake_liters *= 1.1  # Increase for older adults
    
    # Convert liters to gallons
    water_intake_gallons = water_intake_liters * 0.264172
    
    return round(water_intake_gallons, 2)

@app.route('/calculate_water_intake', methods=['POST'])
def get_water_intake():
    try:
        # Get user input from JSON
        data = request.get_json()
        weight = data.get('weight')  # Weight in pounds
        age = data.get('age')
        activity_level = data.get('activity_level')  # Numeric (1, 2, or 3)
        
        # Validate input
        if weight is None or age is None or activity_level not in [1, 2, 3]:
            return jsonify({"error": "Invalid input. Please provide 'weight', 'age', and 'activity_level' as numbers (1, 2, or 3)."}), 400
        
        # Call the function to calculate water intake
        daily_intake = calculate_water_intake(weight, age, activity_level)
        
        # Return the result as a JSON response
        return jsonify({"recommended_water_intake": daily_intake, "unit": "gallons"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
