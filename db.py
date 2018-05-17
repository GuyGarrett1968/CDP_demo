def create_tables():
    cur.execute('''CREATE TABLE trial_dim
                        (Trial_key int,
                        Compound_key int,
                        TrialName string,
                        RequiredPatients_Cnt int,
                        RequiredVisits_Cnt int,
                        RequiredWeeks_Cnt int,
                        RequiredDosage string) ''')

    cur.execute(''' CREATE TABLE compound_dim
                        (Compound_key int,
                        CompoundName string) ''')

    cur.execute(''' CREATE TABLE Investigator_Dim
                        (Investigator_key int,
                         InvestigatorName string,
                         InvestigatorAddress string,
                         InvestigatorQualifications string) ''')

    cur.execute(''' CREATE TABLE patient_dim
                        (Patient_key int,
                         Identity_key int,
                         Birth_Dt date,
                         Gender string,
                         PatientHeight int) ''')

    cur.execute(''' CREATE TABLE identity_dim
                        (Identity_key int,
                         IndividualName string,
                         IndividualAddress string,
                         GPName string,
                         GPAddress string) ''')

    cur.execute(''' CREATE TABLE visit_dim
                        (Visit_key int,
                         Visit_Dt date,
                         SiteAddress string) ''')

    cur.execute(''' CREATE TABLE visit_fact
                        (Trial_key int,
                         Investigator_key int,
                         Compound_key int,
                         Patient_key int,
                         Visit_key int,
                         BloodPressure string,
                         Temperature int,
                         PatientWeight int,
                         Dosage string,
                         DeliveryMethod string)  ''')

    cur.execute(''' CREATE TABLE NCD_Ex1
                        (Trial_key int,
                         Investigator_key int,
                         Compound_key int,
                         Patient_key int,
                         Visit_key int,
                         IOP string)  ''')

    conn.commit()

def addstep_1():

    cur.execute(''' INSERT INTO trial_dim VALUES (1, 1, "Compound 123 twice weekly for 12 weeks at 25mg", 100, 24, 12, "25mg"), 
                                                 (2, 1, "Myracle Dose Escalation", 50, 12, 6, "12mg")               ''')

    cur.execute(''' insert into compound_dim values (1, "Compound 123"), (2, "Compound 987") ''')

    cur.execute(''' insert into investigator_dim values (1, "Robert Smith", "Main Street Springfield NJ USA", "MD"),
                                                        (2, "Sally Jones",  "New Road Horsham Sussex UK",     "GP") ''')

    cur.execute(''' insert into patient_dim values (1, 9001, "1975-08-03", "F", 165),
                                                   (2, 9002, "1968-05-31", "M", 175) ''')

    cur.execute(''' insert into identity_dim values (9001, "Sarah Brown", "Avenue Lane Springfield NJ USA", "Fred Black", "Lane Avenue Srpingfield NJ USA"),
                                                    (9002, "Steve White", "North Drive Horsham Sussex UK", "Daisy Green", "East Close Horsham Sussex UK") ''')

    cur.execute(''' insert into visit_dim values (1, "01-01-2017", "123 Cresent Avenue") ''')

    cur.execute(''' insert into visit_fact values (1, 1, 1, 1, 1, "120/80", 37, 160, "25mg", "Injection"),
                                                  (1, 1, 1, 2, 1, "125/75", 36, 150, "20mg", "Injection") ''')

    cur.execute(''' insert into NCD_Ex1 values (1, 1, 1, 1, 1, "15 mmHg"),
                                               (1, 1, 1, 2, 1, "18 mmHg"),
                                               (1, 1, 1, 1, 2, "17 mmHg"),
                                               (1, 1, 1, 2, 2, "19 mmHg") 
                ''')


    conn.commit()

def addstep_2():

    cur.execute(''' insert into visit_dim values (2, "01-02-2017", "123 Crescent Avenue") ''')

    cur.execute(''' insert into visit_fact values (1, 1, 1, 1, 2, "120/80", 37, 180, "25mg", "Injection"),
                                                   (1, 1, 1, 2, 2, "125/75", 36, 140, "20mg", "Injection") ''')

    conn.commit()

def addstep_3():

    cur.execute(''' INSERT INTO trial_dim VALUES (3, 2, "987 via pill", 100, 12, 52, "0.25mg")  ''')


    cur.execute(''' INSERT INTO patient_dim VALUES (3, 9003, "24/06/1954", "F", 170),
                                                    (4,9004,"10/04/2994","M",180)       ''')

    cur.execute(''' insert into identity_dim values (9003, "Dave Smith", "Close Boulevard Docktown CA USA", "Jeff Plum", "Avenue Lane Docktown CA USA"),
                                                    (9004, "Daphne Jones", "Greenleaf Cul-De-Sac Eveshame Worcs UK", "Derek Mustard", "High Street Evesham Worcs UK") ''')

    cur.execute(''' insert into visit_dim values (3, "01-03-2017", "456 Road Lane") ''')


    cur.execute(''' insert into visit_fact values (3, 2, 2, 3, 3, "130/75", 36, 200, "0.25mg", "Pill"),
                                                   (3, 2, 2, 4, 3, "110/85", 35, 140, "0.25mg", "Pill") ''')

    conn.commit()

def mergedata():

    cur.execute('''  DROP TABLE IF EXISTS visitview ''')
    conn.commit()

    cur.execute(''' CREATE TABLE visitview as SELECT
                        trial_dim.trialname,
                        compound_dim.compoundName,
                        patient_dim.birth_dt,
                        patient_dim.gender,
                        patient_dim.patientHeight,
                        visit_dim.visit_key,
                        visit_dim.visit_dt,
                        visit_fact.BloodPressure,
                        visit_fact.Temperature,
                        visit_fact.PatientWeight,
                        visit_fact.Dosage,
                        visit_fact.DeliveryMethod
                    FROM  trial_dim as trial_dim,
                          visit_fact as visit_fact,
                          visit_dim as visit_dim,
                          patient_dim as patient_dim,
                          compound_dim as compound_dim,
                          investigator_dim as investigator_dim
                    WHERE (trial_dim.trial_key               = visit_fact.trial_key AND
                           visit_dim.visit_key               = visit_fact.visit_key AND
                           patient_dim.patient_key           = visit_fact.patient_key AND
                           compound_dim.compound_key         = visit_fact.compound_key AND
                           investigator_dim.investigator_key = visit_fact.investigator_key) ''')
    conn.commit()

create_tables()
addstep_1()
#addstep_2()
#addstep_3()
mergedata()