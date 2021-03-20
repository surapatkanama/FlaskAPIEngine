from project import app
from project.models.entity.employee import db, InfoModel
from flask import Flask, request, jsonify

@app.route('/insertEmp',methods=['POST', 'GET'])
def insertEmployee():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_emp = InfoModel(
                id=data['id']
            ,create_by=data['create_by'] 
            ,create_date=data['create_date'] 
            ,user_name=data['user_name'] 
            ,position=data['position'])
            db.session.add(new_emp)
            db.session.commit()
            return {"message": f"car {new_emp.user_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    return "insertEmployee"