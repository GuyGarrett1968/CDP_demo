import cherrypy
import pandas as pd
import requests
import sqlite3
import os


class Glob(object):

    def __init__(self):
        # for demo purposes
        self.roles = ["Data manager", "Clinician"]

        self.users = {}
        self.users["Nicolas"] = [self.roles[0], ["ACZ8885M", "BAF158U"]]
        self.users["Guy"] = [self.roles[1], ["AIN710A"]]

        self.studies = {}
        self.studies["AIN710A"] = ["Oncology", "Phase 2"]
        self.studies["ACZ8885M"] = ["CNS", "Phase 1 Dose Escalation"]
        self.studies["BAF158U"] = ["Cardiovascular", "Phase 3"]

        self.studytemplate = {}
        self.studytemplate["Phase 1 Dose Escalation"] = ["Informed Consent signed", [-28 ,-1], "Screening"]

        self.domainProperties  = {}

        self.visits = ["Informed Consent Form signed", "Eligility Review and Confirmation" ,"Medical History", "Physical Examination" ]
        self.stages = ["Screening", "Baseline", "Phase 1", "Phase 2", "Discharge"]

def loadComponents(company):
    # Read Client Configuration file
    exec(open('components.py').read(), globals())

    cl = ComponentsList()
    dataframe = cl.df[cl.df["company"] == company]

    moduleNames = pd.concat([dataframe['library']]).unique()

    # Import relevant files
    for moduleName in moduleNames:
        exec(open(moduleName).read(), globals())


class WebCDP(object):
    # HTTP request objects

    def index(self):
        return '''
            <form action ="/login" method = GET>
                <h4> Please enter your credentials</h4>
                <table>
                    <tr><td>Name</td><td><input name = "username"></td> </tr>
                    <tr><td>Password</td><td><input type="password" name="userpwd"></td></tr>
                </table>
                <input type=submit class="button" value="Login">
            </form>'''
    index.exposed = True

    def login(self, username, userpwd):

        self.username = username

        if username not in glob.users:
           html_code = "Unregistered user"
        else:
            if username == "Nicolas":
                self.role="Data Management"
            elif username == "Guy":
                self.role="Clinicians"

        # build welcome page
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += overview_layout()
        html_code += footer_layout()

        return html_code

    login.exposed = True

    # Build welcome page
    def overview(self):
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += overview_layout()
        html_code += footer_layout()
        return html_code
    overview.exposed = True

    # List all the studies the user joined already
    def myStudies(self):
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += myStudies_layout(self.username)
        html_code += footer_layout()
        return html_code
    myStudies.exposed = True

    # User action from /MyStudies page: join an existing study
    def joinStudy(self, studyname):

        # back end
        self.studyname = studyname
        tmp = glob.users[self.username][1]
        tmp.append(self.studyname)
        glob.users[self.username] = [glob.users[self.username][0], tmp]

        # Front end
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += myStudies_layout(self.username)
        html_code += footer_layout()
        return html_code
    joinStudy.exposed = True

    # New study design. First step (study name, thp area, template)
    def designStudy(self):
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += designStudy_layout()
        html_code += footer_layout()
        return html_code
    designStudy.exposed = True

    # New study design. Second step (study properties)
    def action_newstudy(self, studyname, therparea, studytemplate):
        # back end
        self.studyname = studyname
        self.therparea = therparea
        self.studytemplate = studytemplate

        # front end
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += designStudy_phase2_layout (self.studyname, self.therparea, self.studytemplate)
        html_code += footer_layout()
        return html_code
    action_newstudy.exposed = True

    def action_newstudy2(self, visits, start, end, stages, X):
        # back end

        # front end
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += "OK !"
        html_code += footer_layout()
        return html_code
    action_newstudy2.exposed = True

    def DMQueries(self):
        # back end

        # front end
        html_code  = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += dmQueries_layout()
        html_code += footer_layout()
        return html_code
    DMQueries.exposed = True

    def cdmtest(self):

        html_code = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += cdmTEST_layout()
        html_code += footer_layout()

        return html_code
    cdmtest.exposed = True

    def cdmtest_step2(self):

        dbfile = "db/db1.sq3"
        conn = sqlite3.connect(dbfile)
        cur = conn.cursor()

        cur.execute(''' insert into visit_dim values (2, "01-02-2017", "123 Crescent Avenue") ''')

        cur.execute(''' insert into visit_fact values (1, 1, 1, 1, 2, "120/80", 37, 180, "25mg", "Injection"),
                                                       (1, 1, 1, 2, 2, "125/75", 36, 140, "20mg", "Injection") ''')

        conn.commit()

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
                                   investigator_dim.investigator_key = visit_fact.investigator_key) ''')
        conn.commit()

        cur.close()
        conn.close()

        return self.cdmtest()

    cdmtest_step2.exposed = True

    def cdmtest_step3(self):


        dbfile = "db/db1.sq3"
        conn = sqlite3.connect(dbfile)
        cur = conn.cursor()


        cur.execute(''' INSERT INTO trial_dim VALUES (3, 2, "987 via pill", 100, 12, 52, "0.25mg")  ''')

        cur.execute(''' INSERT INTO patient_dim VALUES (3, 9003, 7693, "F", 170),
                                                        (4,9004,6073,"M",180)       ''')

        cur.execute(''' insert into visit_dim values (3, "01-03-2017", "456 Road Lane") ''')

        cur.execute(''' insert into visit_fact values (3, 2, 2, 3, 3, "130/75", 36, 200, "0.25mg", "Pill"),
                                                       (3, 2, 2, 4, 3, "110/85", 35, 140, "0.25mg", "Pill") ''')

        conn.commit()

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
                                   investigator_dim.investigator_key = visit_fact.investigator_key) ''')
        conn.commit()

        cur.close()
        conn.close()

        return self.cdmtest()

    cdmtest_step3.exposed = True

    def cdmTEST_showdata(self):

        html_code = header_layout()
        html_code += topContainer_Layout()
        html_code += sidebar_layout(self.role, self.username)
        html_code += cdmTEST_layout_showdata()
        html_code += footer_layout()

        return html_code
    cdmTEST_showdata.exposed = True

# Global objects
glob = Glob()

# Load components
loadComponents(company="Roche")

# load HTML modules
exec(open('HTML_modules.py').read(), globals())

# delete SQ3 file, start fresh
dbfile = "db/db1.sq3"
if os.path.isfile(dbfile):
    os.remove(dbfile)

# Create SQL table and data
conn = sqlite3.connect(dbfile)
cur = conn.cursor()
exec(open('db.py').read(), globals())
cur.close()
conn.close()

# run web server
cherrypy.engine.exit()
cherrypy.quickstart(WebCDP(), config="webserver.conf")

