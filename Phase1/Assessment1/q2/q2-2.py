from q2-2-database import Database


with Database('q2-2.db') as db:
    db.create_table('Docters')
    db.create_table('Patients')
    db.ass_column('Doctors', 'Doctor_name')
    db.ass_column('Doctors', 'Patient')
    db.ass_column('Patients', 'Patient_name')
    db.ass_column('Patients', 'Doctor')