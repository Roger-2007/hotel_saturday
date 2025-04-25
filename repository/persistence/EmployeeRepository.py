class EmployeeRepository:

    def create_employee_repository(self,employee,db):
        query = "INSERT INTO employee (id, name , last_name,phone, email, password, rol) values (%s,%s,%s,%s,%s,%s,%s)"
        values = (employee.id,employee.name,employee.last_name,employee.phone,employee.email,employee.password,employee.rol)
        db.execute_query(query,values)

    def login_employee_repository(self,employee,db):
        query = "SELECT * FROM employee where email=%s and password=%s and status=1"
        values = (employee.email,employee.password)
        result = db.execute_query(query,values)
        return result

    def update_employee_repository(self,employee,db):
        query = "update employee set name=%s,last_name=%s,phone=%s,email=%s,password=%s,rol=%s where id=%s and status=1"
        values = (employee.name,employee.last_name,employee.phone,employee.email,employee.password,employee.origin,employee.occupation,employee.id)
        db.execute_query(query,values)

    def all_employee_repository(self,db):
        query = "SELECT * FROM employee"
        results = db.execute_query(query)
        return results

    def disable_employee_repository(self,employee,db):
        query = "UPDATE employee set status=0 where id=%s"
        values = (employee.id,)
        db.execute_query(query,values)

    def delete_employee_repository(self,employee,db):
        query = "delete from employee where id=%s"
        values = (employee.id,)
        db.execute_query(query,values)