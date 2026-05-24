from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

team_members = [
    {
        "id": 1,
        "name": "Alex Rivers",
        "role": "Senior Developer",
        "available": True,
        "avatar": "https://i.pravatar.cc/150?img=1"
    },
    {
        "id": 2,
        "name": "Samantha Chen",
        "role": "UX Designer",
        "available": False,
        "avatar": "https://i.pravatar.cc/150?img=2"
    },
    {
        "id": 3,
        "name": "Jordan Taylor",
        "role": "Project Manager",
        "available": True,
        "avatar": "https://i.pravatar.cc/150?img=3"
    },
    {
        "id": 4,
        "name": "Maria Garcia",
        "role": "Marketing Lead",
        "available": False,
        "avatar": "https://i.pravatar.cc/150?img=4"
    }
]

@app.route('/')
def home():
    return render_template('index.html', members=team_members)

@app.route('/toggle/<int:user_id>', methods=['POST'])
def toggle(user_id):
    for member in team_members:
        if member['id'] == user_id:
            member['available'] = not member['available']
            return jsonify({
                "success": True,
                "available": member['available']
            })

    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)