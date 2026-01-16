# database.py is the bridge between app.py and the database
# Open SQLITe connection
# Return cursors
# Commit changes
# Holds the add/ retrieve / update functions for each table

import sqlite3

DB_NAME = "health_rivals.db"

# com is the live connection to the database file (How python talks to SQL)
# Connection Helper
def get_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    # This allows us to access the columns by name
    conn.row_factory = sqlite3.Row
    return conn

# User Management (Person)
def add_person(User_ID, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday, Challenge_ID):
    conn = get_connection()
    # Pen that writes SQL commands to the database
    cursor = conn.cursor()
    
    # Insert row into Person table
    cursor.execute("""
          INSERT INTO Person (User_ID, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday, Challenge_ID)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (User_ID, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday, Challenge_ID))

    # save changes and close connection
    conn.commit()
    conn.close()
    
def retrieve_person(User_ID):
    conn = get_connection()
    # Pen that writes SQL commands to the database
    cursor = conn.cursor()
    
    # Insert row into Person table
    cursor.execute("""
         SELECT User_ID, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday
         FROM Person
         WHERE User_ID = ?
    """, (User_ID,))

    # Fetch one row from the result set
    person = cursor.fetchone()
    conn.close()
    # Return the person as a dictionary or None if not found
    return dict(person) if person else None


def update_person(User_ID, Email, FName, Middle_Initial, Lname, Height, Birthday):
    conn = get_connection()
    # Pen that writes SQL commands to the database
    cursor = conn.cursor()
    
    # Insert row into Person table
    cursor.execute("""
          UPDATE Person
          SET Email = ?,
          FName = ?,
          Middle_Initial = ?,
          LName = ?,
          Height = ?,
          Birthday = ?
          WHERE User_ID = ?
    """, (Email, FName, Middle_Initial, Lname, Height, Birthday, User_ID))

    # save changes and close connection
    conn.commit()
    conn.close()

# Activity Log
def add_activities(Activities_ID, Calories_Burned, Activities_Hours, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            INSERT INTO Activities (Activities_ID, Calories_Burned, Activities_Hours, DL_ID)
            VALUES (?, ?, ?, ?)
    """, (Activities_ID, Calories_Burned, Activities_Hours, DL_ID))
    
    conn.commit()
    conn.close()
    
def add_activities_type(Activities_ID, ATypes):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          INSERT INTO Activities_Type (Activities_ID, ATypes)
          VALUES (?, ?)
    """, (Activities_ID, ATypes))
    
    conn.commit()
    conn.close()

def retrieve_activities(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          SELECT Activities_ID, Calories_Burned, Activities_Hours, DL_ID
          FROM Activities
          WHERE DL_ID = ?
    """, (DL_ID,))
    
    activities = cursor.fetchone()
    conn.close()
    return dict(activities) if activities else None    
    
def retrieve_activities_type(Activities_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          SELECT Activities_ID, ATypes
          FROM Activities_Type
          WHERE Activities_ID = ?
    """, (Activities_ID,))
    
    activities_type = cursor.fetchone()
    conn.close()
    return dict(activities_type) if activities_type else None

def update_activities(DL_ID, Calories_Burned, Activities_Hours):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE Activities
          SET Calories_Burned = ?,
              Activities_Hours = ?
          WHERE DL_ID = ?
    """, (Calories_Burned, Activities_Hours, DL_ID))

    conn.commit()
    conn.close()

def update_activities_type(Activities_ID, ATypes):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE Activities_Type
          SET ATypes = ?
          WHERE Activities_ID = ?
    """, (ATypes, Activities_ID))

    conn.commit()
    conn.close()
    
# Meal Log
def add_meal_log(MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            INSERT INTO Meal_Log (MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID))
    
    conn.commit()
    conn.close()

def add_meal_breakfast(MealLog_ID, MLBreakfast):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO MealLog_Breakfast (MealLog_ID, MLBreakfast)
            VALUES (?, ?)
    """, (MealLog_ID, MLBreakfast))
    
    conn.commit()
    conn.close()
    
def add_meal_lunch(MealLog_ID, MLLunch):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            INSERT INTO MealLog_Lunch (MealLog_ID, MLLunch)
            VALUES (?, ?)
    """, (MealLog_ID, MLLunch))
    
    conn.commit()
    conn.close()

def add_meal_dinner(MealLog_ID, MLDinner):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           INSERT INTO MealLog_Dinner (MealLog_ID, MLDinner)
           VALUES (?, ?)
    """, (MealLog_ID, MLDinner))
    
    conn.commit()
    conn.close()

def add_meal_snack(MealLog_ID, MLSnack):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           INSERT INTO MealLog_Snack (MealLog_ID, MLSnack)
           VALUES (?, ?)
    """, (MealLog_ID, MLSnack))
    
    conn.commit()
    conn.close()

def retrieve_meal_log(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID
         FROM Meal_Log
         WHERE DL_ID = ?
    """, (DL_ID,))
    
    meal_log = cursor.fetchone()
    conn.close()
    return dict(meal_log) if meal_log else None

def retrieve_meal_breakfast(MealLog_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT MealLog_ID, MLBreakfast
         FROM MealLog_Breakfast
         WHERE MealLog_ID = ?
    """, (MealLog_ID,))
    
    meal_breakfast = cursor.fetchone()
    conn.close()
    return dict(meal_breakfast) if meal_breakfast else None

def retrieve_meal_lunch(MealLog_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT MealLog_ID, MLLunch
         FROM MealLog_Lunch
         WHERE MealLog_ID = ?
    """, (MealLog_ID,))
    
    meal_lunch = cursor.fetchone()
    conn.close()
    return dict(meal_lunch) if meal_lunch else None

def retrieve_meal_dinner(MealLog_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT MealLog_ID, MLDinner
         FROM MealLog_Dinner
         WHERE MealLog_ID = ?
    """, (MealLog_ID,))
    
    meal_dinner = cursor.fetchone()
    conn.close()
    return dict(meal_dinner) if meal_dinner else None

def retrieve_meal_snack(MealLog_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT MealLog_ID, MLSnack
         FROM MealLog_Snack
         WHERE MealLog_ID = ?
    """, (MealLog_ID,))
    
    meal_snack = cursor.fetchone()
    conn.close()
    return dict(meal_snack) if meal_snack else None

def update_meal_log(DL_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE Meal_Log
          SET Calories_Goal = ?,
          Protein = ?,
          Fat = ?,
          Carbs = ?,
          Calories_Amount = ?
          WHERE DL_ID = ?
    """, (Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID))

    conn.commit()
    conn.close()
    
def update_meal_breakfast(MealLog_ID, MLBreakfast):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE MealLog_Breakfast
          SET MLBreakfast = ?
          WHERE MealLog_ID = ?
    """, (MLBreakfast, MealLog_ID))

    conn.commit()
    conn.close()
    
def update_meal_lunch(MealLog_ID, MLLunch):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE MealLog_Lunch
          SET MLLunch = ?
          WHERE MealLog_ID = ?         
    """, (MLLunch, MealLog_ID))

    conn.commit()
    conn.close()

def update_meal_dinner(MealLog_ID, MLDinner):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE MealLog_Dinner
          SET MLDinner = ?
          WHERE MealLog_ID = ?
    """, (MLDinner, MealLog_ID))

    conn.commit()
    conn.close()

def update_meal_snack(MealLog_ID, MLSnack):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE MealLog_Snack
          SET MLSnack = ?
          WHERE MealLog_ID = ?
    """, (MLSnack, MealLog_ID))

    conn.commit()
    conn.close()

# Goals Management
def add_goals(Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          INSERT INTO Goals (Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID)
          VALUES (?, ?, ?, ?, ?)
    """, (Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID))

    conn.commit()
    conn.close()


def retrieve_user_goal(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID
           FROM Goals
           WHERE DL_ID = ?
    """, (DL_ID,))
    
    user_goals = cursor.fetchone()
    conn.close()
    return dict(user_goals) if user_goals else None

def update_goals(DL_ID, Daily_goal, Monthly_goal, Yearly_goal):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          UPDATE Goals
          SET Daily_goal = ?,
              Monthly_goal = ?,
              Yearly_goal = ?
          WHERE DL_ID = ?
    """, (Daily_goal, Monthly_goal, Yearly_goal, DL_ID))

    conn.commit()
    conn.close()
    
# friend Management
def add_friend_info(Friend_ID, Login_Status, PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Friend (Friend_ID, Login_Status, PU_ID)
        VALUES (?, ?, ?)
    """, (Friend_ID, Login_Status, PU_ID))

    conn.commit()
    conn.close()

def add_friend_stats(Friend_ID, FStats):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          INSERT INTO Friend_Stats (Friend_ID, FStats)
          VALUES (?, ?)
    """, (Friend_ID, FStats))

    conn.commit()
    conn.close()

def retrieve_friend_info(PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Friend_ID, Login_Status
           FROM Friend
           WHERE PU_ID = ?
    """, (PU_ID,))
    
    friend_info = cursor.fetchone()
    conn.close()
    return dict(friend_info) if friend_info else None

def retrieve_friend_stats(Friend_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Friend_ID, FStats
           FROM Friend_Stats
           WHERE Friend_ID = ?
    """, (Friend_ID,))
    
    friend_stats = cursor.fetchone()
    conn.close()
    return dict(friend_stats) if friend_stats else None

    # challenge Management
def add_challenge(Challenge_ID, Daily_Challenge, Challenge_Complete, DailyRivals_Credit, Special_Challenge):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Challenges (Challenge_ID, Daily_Challenge, Challenge_Complete, DailyRivals_Credit, Special_Challenge)
        VALUES (?, ?, ?, ?, ?)
    """, (Challenge_ID, Daily_Challenge, Challenge_Complete, DailyRivals_Credit, Special_Challenge))

    conn.commit()
    conn.close()

    
def retrieve_challenge(Challenge_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Challenge_ID, Daily_Challenge, Challenge_Complete, DailyRivals_Credit, Special_Challenge
           FROM Challenges
           WHERE Challenge_ID = ?
    """, (Challenge_ID,))
    
    challenge = cursor.fetchone()
    conn.close()
    return dict(challenge) if challenge else None


def update_challenges_completion(Challenge_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Challenges
        SET Challenge_Complete = TRUE
        WHERE Challenge_ID = ?
    """, (Challenge_ID,))

    conn.commit()
    conn.close()
    
def apply_challenge_credit():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           UPDATE Person
           SET Credit = Credit + (
            SELECT DailyRivals_Credit
            FROM Challenges
            WHERE Challenges.Challenge_ID = Person.Challenge_ID
                AND Challenge_Complete = TRUE
           )
           WHERE EXISTS (
            SELECT 1
            FROM Challenges
            WHERE Challenges.Challenge_ID = Person.Challenge_ID
                AND Challenge_Complete = TRUE
           )
    """)
    
    conn.commit()
    conn.close()
    

# device management

def add_device(Device_ID, Phone, Smart_watch, Implanted_chip, PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Device (Device_ID, Phone, Smart_watch, Implanted_chip, PU_ID)
        VALUES (?, ?, ?, ?, ?)
    """, (Device_ID, Phone, Smart_watch, Implanted_chip, PU_ID))
    
    conn.commit()
    conn.close()

def retrieve_device(PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Device_ID, Phone, Smart_watch, Implanted_chip, PU_ID
           FROM Device
           WHERE PU_ID = ?
    """, (PU_ID,))

    device = cursor.fetchone()
    conn.close()
    return dict(device) if device else None

def update_devices(PU_ID, Phone, Smart_watch, Implanted_chip):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Device
        SET Phone = ?,
            Smart_watch = ?,
            Implanted_chip = ?
        WHERE PU_ID = ?
    """, (Phone, Smart_watch, Implanted_chip, PU_ID))

    conn.commit()
    conn.close()

# health metric tracking

def add_person_steps(Step_ID, Step_Goal, Total_Steps, Daily_Steps, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Steps (Step_ID, Step_Goal, Total_Steps, Daily_Steps, DL_ID)
        VALUES (?, ?, ?, ?, ?)
    """, (Step_ID, Step_Goal, Total_Steps, Daily_Steps, DL_ID))
    
    conn.commit()
    conn.close()

def retrieve_steps(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
         SELECT Step_ID, Step_Goal, Total_Steps, Daily_Steps, DL_ID
         FROM Steps
         WHERE DL_ID = ?
    """, (DL_ID,))
    
    steps = cursor.fetchone()
    conn.close()
    return dict(steps) if steps else None

def add_person_weight(Weight_ID, Total_Weight, Weight_Gain, Weight_Loss, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            INSERT INTO Weight (Weight_ID, Total_Weight, Weight_Gain, Weight_Loss, DL_ID)
            VALUES (?, ?, ?, ?, ?)
    """, (Weight_ID, Total_Weight, Weight_Gain, Weight_Loss, DL_ID))
    
    conn.commit()
    conn.close()
    
def retrieve_person_weight(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
           SELECT Weight_ID, Total_Weight, Weight_Gain, Weight_Loss, DL_ID
           FROM Weight
           WHERE DL_ID = ?
    """, (DL_ID,))
    
    weight = cursor.fetchone()
    conn.close()
    return dict(weight) if weight else None


def add_person_sleep(SleepHour_ID, Sleep_Quality, Hours_Slept, Sleep_Pattern, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Sleep_Hours (SleepHour_ID, Sleep_Quality, Hours_Slept, Sleep_Pattern, DL_ID)
        VALUES (?, ?, ?, ?, ?)
    """, (SleepHour_ID, Sleep_Quality, Hours_Slept, Sleep_Pattern, DL_ID))
    
    conn.commit()
    conn.close()
    
def retrieve_person_sleep(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT SleepHour_ID, Sleep_Quality, Hours_Slept, Sleep_Pattern, DL_ID
        FROM Sleep_Hours
        WHERE DL_ID = ?
    """, (DL_ID,))
    
    sleep = cursor.fetchone()
    conn.close()
    return dict(sleep) if sleep else None


def add_person_bloodpressure(Blood_ID, Blood_Status, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            INSERT INTO Blood_Pressure (Blood_ID, Blood_Status, DL_ID)
            VALUES (?, ?, ?)
    """, (Blood_ID, Blood_Status, DL_ID))
    
    conn.commit()
    conn.close()
    
def retrieve_person_bloodpressure(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Blood_ID, Blood_Status, DL_ID
        FROM Blood_Pressure
        WHERE DL_ID = ?
    """, (DL_ID,))
    
    bloodpressure = cursor.fetchone()
    conn.close()
    return dict(bloodpressure) if bloodpressure else None

# medication log

def add_medication(Medication_ID, Medication_Time, Dosage, DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
       INSERT INTO Medication (Medication_ID, Medication_Time, Dosage, DL_ID)
       VALUES (?, ?, ?, ?)
    """, (Medication_ID, Medication_Time, Dosage, DL_ID))
    
    conn.commit()
    conn.close()

def retrieve_medication(DL_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Medication_ID, Medication_Time, Dosage, DL_ID
        FROM Medication
        WHERE DL_ID = ?
    """, (DL_ID,))
    
    medication = cursor.fetchone()
    conn.close()
    return dict(medication) if medication else None

def update_medication(DL_ID, Medication_Time, Dosage):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
            UPDATE Medication
            SET Medication_Time = ?,
                Dosage = ?
            WHERE DL_ID = ?
        """, (Medication_Time, Dosage, DL_ID))

    conn.commit()
    conn.close()

# medical log

def add_medical_record(Medical_ID, Past_surgeries, Past_Medication, PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
       INSERT INTO Medical_Record (Medical_ID, Past_surgeries, Past_Medication, PU_ID)
        VALUES (?, ?, ?, ?)
    """, (Medical_ID, Past_surgeries, Past_Medication, PU_ID))
    
    conn.commit()
    conn.close()

def retrieve_medical_record(PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Medical_ID, Past_surgeries, Past_Medication, PU_ID
        FROM Medical_Record
        WHERE PU_ID = ?
    """, (PU_ID,))
    
    record = cursor.fetchone()
    conn.close()
    return dict(record) if record else None

def update_medical_record(PU_ID, Medical_ID, Past_surgeries, Past_Medication):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Medical_Record
        SET Past_surgeries = ?,
         Past_Medication = ?
        WHERE PU_ID = ? AND Medical_ID = ?
        """, (Past_surgeries, Past_Medication, PU_ID, Medical_ID))

    conn.commit()
    conn.close()

def add_medical_record_allegies(Medical_ID, MRAllegies):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
       INSERT INTO Medical_Record_Allegies (Medical_ID, MRAllegies)
       VALUES (?, ?)
    """, (Medical_ID, MRAllegies))

    conn.commit()
    conn.close()
    
def retrieve_medical_record_allegies(Medical_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Medical_ID, MRAllegies
        FROM Medical_Record_Allegies
        WHERE Medical_ID = ?
    """, (Medical_ID,))
    
    allegies = cursor.fetchone()
    conn.close()
    return dict(allegies) if allegies else None

def update_medical_record_allegies(Medical_ID, MRAllegies):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Medical_Record_Allegies
        SET MRAllegies = ?
        WHERE Medical_ID = ?
        """, (MRAllegies, Medical_ID))

    conn.commit()
    conn.close()


def add_medical_disease(Medical_ID, MRDiseases):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
       INSERT INTO Medical_Record_Diseases (Medical_ID, MRDiseases)
        VALUES (?, ?)
    """, (Medical_ID, MRDiseases))
    
    conn.commit()
    conn.close()

def retrieve_medical_disease(Medical_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Medical_ID, MRDiseases
        FROM Medical_Record_Diseases
        WHERE Medical_ID = ?
    """, (Medical_ID,))
    
    disease = cursor.fetchone()
    conn.close()
    return dict(disease) if disease else None

def update_medical_disease(Medical_ID, MRDiseases):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Medical_Record_Diseases
        SET MRDiseases = ?
        WHERE Medical_ID = ?
        """, (MRDiseases, Medical_ID))

    conn.commit()
    conn.close()
    
def add_medical_disabilities(Medical_ID, MRDisabilities):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          INSERT INTO Medical_Record_Disabilities (Medical_ID, MRDisabilities)
          VALUES (?, ?)
    """, (Medical_ID, MRDisabilities))
    
    conn.commit()
    conn.close()
    
def retrieve_medical_disabilities(Medical_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Medical_ID, MRDisabilities
        FROM Medical_Record_Disabilities
        WHERE Medical_ID = ?
    """, (Medical_ID,))
    
    disabilities = cursor.fetchone()
    conn.close()
    return dict(disabilities) if disabilities else None

def update_medical_disabilities(Medical_ID, MRDisabilities):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE Medical_Record_Disabilities
        SET MRDisabilities = ?
        WHERE Medical_ID = ?
    """, (MRDisabilities, Medical_ID))

    conn.commit()
    conn.close()

# daily logging

def add_daily_log(Log_ID, Log_Date, PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          INSERT INTO Daily_Log (Log_ID, Log_Date, PU_ID)
          VALUES (?, ?, ?)
    """, (Log_ID, Log_Date, PU_ID))

    conn.commit()
    conn.close()
    
def retrieve_daily_log(PU_ID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
          SELECT Log_ID, Log_Date, PU_ID
          FROM Daily_Log
          WHERE PU_ID = ?
    """, (PU_ID,))
    
    result = cursor.fetchone()
    conn.close()
    
    return dict(result) if result else None
