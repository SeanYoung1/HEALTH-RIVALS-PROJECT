textPRAGMA foreign_keys = ON;

CREATE TABLE Challenges (
    Challenge_ID        INTEGER         PRIMARY KEY,
    Daily_Challenge     TEXT            NOT NULL,
    Challenge_Complete  INTEGER         NOT NULL DEFAULT 0
                                        CHECK (Challenge_Complete IN (0, 1)),
    DailyRivals_Credit  INTEGER         NOT NULL,
    Special_Challenge   TEXT            NOT NULL,
);

CREATE TABLE Person (
    User_ID             INTEGER         PRIMARY KEY,
    Email               TEXT            NOT NULL
                                        CHECK (Email LIKE '%_@__%.__%'),
    Credit              INTEGER         NOT NULL DEFAULT 0 CHECK (Credit >= 0),
    Fname               TEXT            NOT NULL CHECK(LENGTH(Fname) > 0),
    Middle_Initial      TEXT,
    Lname               TEXT            NOT NULL CHECK(LENGTH(Lname) > 0),
    Height              REAL            NOT NULL CHECK (Height >= 0),
    Birthday            DATE            NOT NULL,
    Challenge_ID        INTEGER         NOT NULL,
    FOREIGN KEY (Challenge_ID) REFERENCES Challenges(Challenge_ID) ON DELETE CASCADE,
    UNIQUE (Email),
);

CREATE TABLE Friend (
    Friend_ID           INTEGER   PRIMARY KEY,
    Login_Status        INTEGER   NOT NULL DEFAULT 0
                        CHECK (Login_Status IN (0, 1)),
    PU_ID               INTEGER   NOT NULL,
    FOREIGN KEY (PU_ID) REFERENCES Person(User_ID) ON DELETE CASCADE
);

CREATE TABLE Friend_Stats (
    Friend_ID           INTEGER         NOT NULL,
    FStats              TEXT            NOT NULL CHECK (length(FStats) > 0),
    PRIMARY KEY (Friend_ID, FStats),
    FOREIGN KEY (Friend_ID) REFERENCES Friend(Friend_ID) ON DELETE CASCADE      
);

CREATE TABLE Device (
    Device_ID           INTEGER   PRIMARY KEY,
    Phone               INTEGER   NOT NULL DEFAULT 0
                        CHECK (Phone IN (0, 1)),
    Smart_watch         INTEGER   NOT NULL DEFAULT 0,
                        CHECK (Smart_watch IN (0, 1)),
    Implanted_chip      INTEGER   NOT NULL DEFAULT 0
                        CHECK (Implanted_chip IN (0, 1)),
    PU_ID               INTEGER   NOT NULL,
    FOREIGN KEY (PU_ID) REFERENCES Person(User_ID) ON DELETE CASCADE        
);

CREATE TABLE Medical_Record (
    Medical_ID          INTEGER   PRIMARY KEY,
    Past_surgeries      TEXT,
    Past_Medication     TEXT,
    PU_ID               INTEGER   NOT NULL,
    FOREIGN KEY (PU_ID) REFERENCES Person(User_ID) ON DELETE CASCADE       
);

CREATE TABLE Medical_Record_Allegies (
    Medical_ID          INTEGER   NOT NULL,
    MRAllegies          TEXT      NOT NULL CHECK (length(MRAllegies) > 0),
    PRIMARY KEY (Medical_ID, MRAllegies),
    FOREIGN KEY (Medical_ID) REFERENCES Medical_Record(Medical_ID) ON DELETE CASCADE
);

CREATE TABLE Medical_Record_Diseases (
    Medical_ID          INTEGER   NOT NULL,
    MRDiseases          TEXT      NOT NULL CHECK (length(MRDiseases) > 0),
    PRIMARY KEY (Medical_ID, MRDiseases),
    FOREIGN KEY (Medical_ID) REFERENCES Medical_Record(Medical_ID) ON DELETE CASCADE
);

CREATE TABLE Medical_Record_Disabilities (
    Medical_ID          INTEGER   NOT NULL,
    MRDisabilities      TEXT      NOT NULL CHECK (length(MRDisabilities) > 0),
    PRIMARY KEY (Medical_ID, MRDisabilities),
    FOREIGN KEY (Medical_ID) REFERENCES Medical_Record(Medical_ID)
);

CREATE TABLE Daily_Log (
    Log_ID              INTEGER   PRIMARY KEY,
    Log_Date            TEXT      NOT NULL,
    PU_ID               INTEGER   NOT NULL,
    UNIQUE (Log_Date, PU_ID),
    FOREIGN KEY (PU_ID) REFERENCES Person(User_ID) ON DELETE CASCADE
);

CREATE TABLE Blood_Pressure (
    Blood_ID            INTEGER   PRIMARY KEY,
    Blood_Status        INTEGER   CHECK (Blood_Status >= 0 AND Blood_Status <= 300),
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE
);

CREATE TABLE Sleep_Hours (
    SleepHour_ID        INTEGER   PRIMARY KEY,
    Sleep_Quality       INTEGER   CHECK (Sleep_Quality >= 0 AND Sleep_Quality <= 10),
    Hours_Slept         REAL      CHECK (Hours_Slept >= 0 and Hours_Slept <= 24.0),
    Sleep_Pattern       TEXT,
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE            
);

CREATE TABLE Weight (
    Weight_ID           INTEGER   PRIMARY KEY,
    Total_Weight        INTEGER   CHECK (Total_Weight >= 0 AND Total_Weight <= 500),
    Weight_Gain         INTEGER   DEFAULT 0,
    Weight_Loss         INTEGER   DEFAULT 0,
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE
);

CREATE TABLE Goals (
    Goal_ID             INTEGER   PRIMARY KEY,
    Daily_goal          TEXT,
    Monthly_goal        TEXT,
    Yearly_goal         TEXT,
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE
);

CREATE TABLE Challenges_Display (
    Display_ID          INTEGER   PRIMARY KEY,
    Challenge_ID        INTEGER   NOT NULL,
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE,
    FOREIGN KEY (Challenge_ID) REFERENCES Challenges(Challenge_ID) ON DELETE CASCADE
);

CREATE TABLE Medication (
    Medication_ID       INTEGER   PRIMARY KEY,
    Medication_Time     TEXT,
    Dosage              INTEGER   CHECK (Dosage >= 0 AND Dosage <= 1000),
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE,
);

CREATE TABLE Steps (
    Step_ID             INTEGER   PRIMARY KEY,
    Step_Goal           INTEGER   DEFAULT 0 CHECK (Step_Goal >= 0),
    Total_Steps         INTEGER   DEFAULT 0 CHECK (Total_Steps >= 0),
    Daily_Steps         INTEGER   DEFAULT 0 CHECK (Daily_Steps >= 0),
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE
);

CREATE TABLE Activities (
    Activities_ID       INTEGER   PRIMARY KEY,
    Calories_Burned     INTEGER   DEFAULT 0 CHECK (Calories_Burned >= 0),
    Activities_Hours    REAL      DEFAULT 0 CHECK (Activities_Hours >= 0.0),
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE,        
);

CREATE TABLE Activities_Type (
    Activities_ID       INTEGER   NOT NULL,
    ATypes              TEXT      NOT NULL CHECK (length(ATypes) > 0),
    PRIMARY KEY (Activities_ID, ATypes),
    FOREIGN KEY (Activities_ID) REFERENCES Activities(Activities_ID) ON DELETE CASCADE
);

CREATE TABLE Meal_Log (
    MealLog_ID          INTEGER   PRIMARY KEY,
    Calories_Goal       INTEGER   DEFAULT 2000 CHECK (Calories_Goal >= 0),
    Protein             INTEGER   DEFAULT 0 CHECK (Protein >= 0),
    Fat                 INTEGER   DEFAULT 0 CHECK (Fat >= 0),
    Carbs               INTEGER   DEFAULT 0 CHECK (Carbs >= 0),
    Calories_Amount     INTEGER   DEFAULT 0 CHECK (Calories_Amount >= 0),
    DL_ID               INTEGER   NOT NULL,
    FOREIGN KEY (DL_ID) REFERENCES Daily_Log(Log_ID) ON DELETE CASCADE,
);

CREATE TABLE MealLog_Breakfast (
    MealLog_ID          INTEGER   NOT NULL,
    MLBreakfast         TEXT      NOT NULL CHECK (length(MLBreakfast) > 0),
    PRIMARY KEY (MealLog_ID, MLBreakfast),
    FOREIGN KEY (MealLog_ID) REFERENCES Meal_Log(MealLog_ID) ON DELETE CASCADE
);

CREATE TABLE MealLog_Lunch (
    MealLog_ID          INTEGER   NOT NULL,
    MLLunch             TEXT      NOT NULL CHECK (length(MLLunch) > 0),
    PRIMARY KEY (MealLog_ID, MLLunch),
    FOREIGN KEY (MealLog_ID) REFERENCES Meal_Log(MealLog_ID) ON DELETE CASCADE
);

CREATE TABLE MealLog_Dinner (
    MealLog_ID          INTEGER   NOT NULL,
    MLDinner            TEXT      NOT NULL CHECK (length(MLDinner) > 0),
    PRIMARY KEY (MealLog_ID, MLDinner),
    FOREIGN KEY (MealLog_ID) REFERENCES Meal_Log(MealLog_ID) ON DELETE CASCADE
);

CREATE TABLE MealLog_Snack (
    MealLog_ID          INTEGER   NOT NULL,
    MLSnack             TEXT      NOT NULL CHECK (length(MLSnack) > 0),
    PRIMARY KEY (MealLog_ID, MLSnack),
    FOREIGN KEY (MealLog_ID) REFERENCES Meal_Log(MealLog_ID) ON DELETE CASCADE
);
