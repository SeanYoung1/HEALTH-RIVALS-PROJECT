/* ============================================================
   File: queries.sql
   Project: Health & Fitness Tracking System
   Author: ______________________
   Date: ________________________

   Description:
   This file contains SQL queries that implement each
   functional requirement defined in the project report.
   Each query is labeled and commented according to the
   corresponding functional requirement.
   ============================================================ */


/* ============================================================
   FUNCTIONAL REQUIREMENT 1 – User Management
   Description:
   Store, retrieve, and update user profile information.
   ============================================================ */

-- Create a new user account
INSERT INTO Person (user_id, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday)
VALUES (:user_id, :Email, 0, :FName, :Middle_Initial, :Lname, :Height. :Birthday );

-- Retrieve user profile information
SELECT user_id, Email, Credit, FName, Middle_Initial, Lname, Height, Birthday
FROM Person
WHERE user_id = :user_id;


-- Update user profile information
UPDATE Person
SET Email = :Email,
    FName = :Fname,
    Middle_Initial = :Middle_Initial,
    LName = :Lname,
    Height = :Height,
    Birthday = :Birthday
WHERE user_id = :user_id;


/* ============================================================
   FUNCTIONAL REQUIREMENT 2 – ACTIVITY Logging
   Description:
   Update and retrieve their activities on specific dates.
   ============================================================ */

-- Log a activity session
INSERT INTO Activities (Activities_ID, Calories_Burned, Activites_Hour, DL_ID)
VALUES (:Activities_ID, :Calories_Burned, :Activites_Hours, :DL_ID);

-- Log a activity type 
INSERT INTO Actitivities_Type (Activities_ID, ATypes)
VALUES (:Activities_ID, :ATypes)


-- Retrieve activity session for a specific log
SELECT Activities_ID, Calories_Burned, Activites_Hour, DL_ID
FROM Activities
WHERE DL_ID = :DL_ID;

-- Retrieve activity type from a specific activity session
SELECT Activities_ID, ATypes
FROM Activities_Type
WHERE Activities_ID = :Activities_ID;


-- Update activity information for a specific log
UPDATE Activities
SET Calories_Burned = :Calories_Burned,
    Activites_Hour = :Activites_Hour,
WHERE DL_ID = :DL_ID;

-- Update activity type for a specific activity
UPDATE Activities_Type
SET ATypes = :ATypes
WHERE DL_ID = :DL_ID;

/* ============================================================
   FUNCTIONAL REQUIREMENT 3 – Meal Logging
   Description:
   Record and analyze nutrition and meal intake.
   ============================================================ */

-- Log a meal
INSERT INTO Meal_Log (MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount DL_ID)
VALUES (:MealLog_ID, :Calories_Goal, :Protein, ,:Fat:, Carbs, :Calories_Amount, :DL_IDs);

-- Log a Breakfast
INSERT INTO MealLog_Breakfast (MealLog_ID, MLBreakfast)
VALUES (:MealLog_ID, :MLBreakfast);

-- Log a Lunch
INSERT INTO MealLog_Lunch (MealLog_ID, MealLog_Lunch)
VALUES (:MealLog_ID, :MLLunch);

-- Log a Dinner
INSERT INTO MealLog_Dinner (MealLog_ID, MealLog_Dinner)
VALUES (:MealLog_ID, :MLDinner);

-- Log a Snack
INSERT INTO MealLog_Snack (MealLog_ID, MealLog_Snack)
VALUES (:MealLog_ID, :MLSnack);


-- Retrieve eated stuff at specific dates
SELECT MealLog_ID, Calories_Goal, Protein, Fat, Carbs, Calories_Amount, DL_ID
FROM Meal_Log
WHERE DL_ID = :DL_ID

-- Retrieve a day's breakfast
SELECT MealLog_ID, MLBreakfast
FROM MealLog_Breakfast
WHERE MealLog_ID = :MealLog_ID

-- Retrieve a day's lunch
SELECT MealLog_ID, MLLunch
FROM MealLog_Lunch
WHERE MealLog_ID = :MealLog_ID

-- Retrieve a day's dinner
SELECT MealLog_Dinner, MLDinner
FROM MealLog_Dinner
WHERE MealLog_ID = :MealLog_ID

-- Retrieve a day's snack
SELECT MealLog_Snack, MLSnack
FROM MealLog_Snack
WHERE MealLog_ID = :MealLog_ID

-- Update meal macros and calories
UPDATE Meal_Log
SET Calories_Goal = :Calories_Goal,
    Protein = :Protein,
    Fat = :Fat,
    Carbs = :Carbs,
    Calories_Amount = :Calories_Amount,
WHERE DL_ID = :DL_ID

-- Update meal breakfast
UPDATE MealLog_Breakfast
SET MLBreakfast = :MLBreakfast,
WHERE MealLog_ID = :MealLog_ID

-- Update meal lunch
UPDATE MealLog_Lunch
SET MLLunch = :MLLunch,
WHERE MealLog_ID = :MealLog_ID

-- Update meal dinner
UPDATE MealLog_Dinner
SET MLDinner = :MLDinner,
WHERE MealLog_ID = :MealLog_ID

-- Update meal snack
UPDATE MealLog_Snack
SET MLSnack = :MLSnack,
WHERE MealLog_ID = :MealLog_ID


/* ============================================================
   FUNCTIONAL REQUIREMENT 4 – Goals Management
   Description:
   Log, view, and update fitness goals.
   ============================================================ */

-- log a user goal
INSERT INTO Goals (Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID)
VALUES (:Goal_ID, :Daily_goal, :Monthly_goal, :Yearly_goal, :DL_ID);


-- view user goals
SELECT Goal_ID, Daily_goal, Monthly_goal, Yearly_goal, DL_ID
FROM Goals
WHERE DL_ID = :DL_ID;


-- Update goals
UPDATE Goals
SET Daily_goal = :Daily_goal,
    Monthly_goal = :Monthly_goal,
    Yearly_goal = :Yearly_goal
WHERE Goal_ID = :Goal_ID


/* ============================================================
   FUNCTIONAL REQUIREMENT 5 – Social Interactions
   Description:
   Manage friends and view friends’ activity.
   ============================================================ */

-- log friend information
INSERT INTO Friends (Friend_ID, Login_Status, PU_ID)
VALUES (:Friend_ID, :Login_Status, :PU_ID);

-- log friend stats
INSERT INTO Friend_Stats (Friend_ID, FStats)
VALUES (:Friend_ID, :FStats);


-- View friends information
SELECT Friend_ID, Login_Status
FROM Friend
WHERE PU_ID = :PU_ID;

-- View friends stats
SELECT Friend_ID, FStats
FROM Friend_Stats
WHERE Friend_ID = :Friend_ID


/* ============================================================
   FUNCTIONAL REQUIREMENT 6 – Challenges
   Description:
   Join challenges, track points
   ============================================================ */


CHECK (challenge_complete = TRUE), then DailyRivals_Credit += User_ID.Credit


-- FR6-A: Join a challenge
INSERT INTO ChallengeParticipants (challenge_id, user_id, points)
VALUES (:challenge_id, :user_id, 0);

-- FR6-B: View challenge leaderboard
SELECT user_id, points
FROM ChallengeParticipants
WHERE challenge_id = :challenge_id
ORDER BY points DESC;


/* ============================================================
   FUNCTIONAL REQUIREMENT 7 – Device Integration (Stored Data)
   Description:
   Store and retrieve health data imported from wearable devices.
   ============================================================ */

-- FR7: Retrieve device-imported health data
SELECT metric_type, metric_value, recorded_date
FROM HealthMetrics
WHERE user_id = :user_id
  AND source = 'Device';


/* ============================================================
   FUNCTIONAL REQUIREMENT 8 – Health Metric Tracking
   Description:
   Log and retrieve health metrics such as steps, heart rate,
   sleep, and blood pressure.
   ============================================================ */

-- FR8-A: Log health metrics
INSERT INTO HealthMetrics (
    metric_id, user_id, metric_type,
    metric_value, recorded_date
)
VALUES (
    :metric_id, :user_id, :metric_type,
    :metric_value, :recorded_date
);

-- FR8-B: Retrieve health metrics by date
SELECT metric_type, metric_value
FROM HealthMetrics
WHERE user_id = :user_id
  AND recorded_date = :recorded_date;


/* ============================================================
   FUNCTIONAL REQUIREMENT 9 – Health History Logging
   Description:
   View historical health data organized by date.
   ============================================================ */

-- FR9: Retrieve health history ordered by date
SELECT recorded_date, metric_type, metric_value
FROM HealthMetrics
WHERE user_id = :user_id
ORDER BY recorded_date;


/* ============================================================
   END OF FILE
   ============================================================ */


