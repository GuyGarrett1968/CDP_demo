def header_layout():
    return '''
    <html>
    <title>Clinical Data Platform</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    
    <style>
    html,body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
    </style>
    <body class="w3-light-grey">
    '''

def topContainer_Layout():
    return '''<!-- Top container -->
    <div class="w3-bar w3-top w3-black w3-large" style="z-index:4">
    <button class="w3-bar-item w3-button w3-hide-large w3-hover-none w3-hover-text-light-grey" onclick="w3_open();"><i class="fa fa-bars"></i>  Menu</button>
    <span class="w3-bar-item w3-right">Clinical Data Platform <strong>~ AchieveIntelligence</strong></span>
    </div>'''


def sidebar_layout(role, username):

    if role == "Data Management":
        sections = '<a href="overview" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-eye fa-fw"></i>  Overview</a>'
        sections += '<a href="myStudies" class="w3-bar-item w3-button w3-padding"><i class="fa fa-notes-medical fa-fw"></i>  My Studies</a>'
        sections += '<a href="DMQueries" class="w3-bar-item w3-button w3-padding"><i class="fa fa-question-circle fa-fw"></i>  Query Management</a>'
        sections += '<a href="cdmtest" class="w3-bar-item w3-button w3-padding"><i class="fa fa-database fa-fw"></i>  Auto DI Demo</a>'
        sections += '<a href="cdmTEST_showdata" class="w3-bar-item w3-button w3-padding"><i class="fa fa-table fa-fw"></i>  Show Data</a>'
        sections += '<a href="configuration" class="w3-bar-item w3-button w3-padding"><i class="fa fa-wrench fa-fw"></i>  Configuration</a>'

    elif role == "Clinicians":
        sections = '<a href="overview" class="w3-bar-item w3-button w3-padding"><i class="fa fa-eye fa-fw"></i>  Overview</a>'
        sections += '<a href="myStudies" class="w3-bar-item w3-button w3-padding"><i class="fa fa-notes-medical fa-fw"></i>  My Studies</a>'
        sections += '<a href="designStudy" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-pencil fa-fw"></i>  Protocol Design</a>'
        sections += '<a href="designStudy" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-pencil fa-fw"></i>  eCRF</a>'
        sections += '<a href="configuration" class="w3-bar-item w3-button w3-padding"><i class="fa fa-wrench fa-fw"></i>  Configuration</a>'


    return '''
    <!-- Sidebar/menu -->
    <nav class="w3-sidebar w3-collapse w3-white w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
      <div class="w3-container w3-row">
        <div class="w3-col s4">
          <img src="https://www.w3schools.com/w3images/avatar2.png" class="w3-circle w3-margin-right" style="width:46px">
        </div>
        <div class="w3-col s8 w3-bar">
          <span>Welcome, <strong>''' + username + '''</strong></span><br>
          <a href="#" class="w3-bar-item w3-button"><i class="fa fa-envelope"></i></a>
          <a href="#" class="w3-bar-item w3-button"><i class="fa fa-user"></i></a>
          <a href="/" class="w3-bar-item w3-button"><i class="fa fa-cog"></i></a>
        </div>
      </div>
      <hr>
      <div class="w3-container">
        <h5>''' + role + ''' view</h5>
      </div>
      <div class="w3-bar-block">
        <a href="#" class="w3-bar-item w3-button w3-padding-16 w3-hide-large w3-dark-grey w3-hover-black" onclick="w3_close()" title="close menu"><i class="fa fa-remove fa-fw"></i>  Close Menu</a>
        ''' + sections + '''
      </div>
    </nav>

    <!-- Overlay effect when opening sidebar on small screens -->
    <div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>
    '''

def overview_layout():
    return '''
  <!-- !PAGE CONTENT! -->
  <div class="w3-main" style="margin-left:300px;margin-top:43px;">

    <!-- Header -->
    <header class="w3-container" style="padding-top:22px">
      <h5><b><i class="fa fa-dashboard"></i> My Dashboard</b></h5>
    </header>

    <div class="w3-row-padding w3-margin-bottom">
      <div class="w3-quarter">
        <div class="w3-container w3-red w3-padding-16">
          <div class="w3-left"><i class="fa fa-user-md w3-xxxlarge"></i></div>
          <div class="w3-right">
            <h3>21</h3>
          </div>
          <div class="w3-clear"></div>
          <h4>Queries</h4>
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-container w3-blue w3-padding-16">
          <div class="w3-left"><i class="fa fa-check-square-o w3-xxxlarge"></i></div>
          <div class="w3-right">
            <h3>12</h3>
          </div>
          <div class="w3-clear"></div>
          <h4>Resolved</h4>
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-container w3-teal w3-padding-16">
          <div class="w3-left"><i class="fa fa-heartbeat w3-xxxlarge"></i></div>
          <div class="w3-right">
            <h3>0</h3>
          </div>
          <div class="w3-clear"></div>
          <h4>Adverse Events</h4>
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-container w3-orange w3-text-white w3-padding-16">
          <div class="w3-left"><i class="fa fa-bar-chart w3-xxxlarge"></i></div>
          <div class="w3-right">
            <h3>5</h3>
          </div>
          <div class="w3-clear"></div>
          <h4>Reports</h4>
        </div>
      </div>
    </div>

    <div class="w3-panel">
      <div class="w3-row-padding" style="margin:0 -16px">
        <div class="w3-third">
              <p align="center">
          <h5>Dashboard</h5>
            <img src="/static/kpi1.jpg" style="width:45%" align="center" alt="Patient Recruitment">
            <img src="/static/kpi2.jpg" style="width:45%" align="center" alt="Study Completion">
            </p>
        </div>        <div class="w3-twothird">
          <h5>Workflow</h5>
          <table class="w3-table w3-striped w3-white">
            <tr>
              <td><i class="fa fa-user w3-text-blue w3-large"></i></td>
              <td>New patient visit.</td>
              <td><i>10 mins</i></td>
            </tr>
            <tr>
              <td><i class="fa fa-bell w3-text-red w3-large"></i></td>
              <td>Query: Patient Age violates protocol.</td>
              <td><i>15 mins</i></td>
            </tr>
            <tr>
              <td><i class="fa fa-user w3-text-yellow w3-large"></i></td>
              <td>New investigator launched.</td>
              <td><i>17 mins</i></td>
            </tr>
            <tr>
              <td><i class="fa fa-comment w3-text-blue w3-large"></i></td>
              <td>New informed consent agreed.</td>
              <td><i>25 mins</i></td>
            </tr>
            <tr>
              <td><i class="fa fa-user w3-text-blue w3-large"></i></td>
              <td>New patient visit.</td>
              <td><i>28 mins</i></td>
            </tr>
            <tr>
              <td><i class="fa fa-user w3-text-blue w3-large"></i></td>
              <td>New patient visit.</td>
              <td><i>35 mins</i></td>
            </tr>
          </table>
        </div>
      </div>
    </div>
    <hr>
    <div class="w3-container">
      <h5>Key Performance Measures</h5>
      <p>Study Completion</p>
      <div class="w3-grey">
        <div class="w3-container w3-center w3-padding w3-green" style="width:25%">+25%</div>
      </div>

      <p>Protocol Violations</p>
      <div class="w3-grey">
        <div class="w3-container w3-center w3-padding w3-orange" style="width:50%">50%</div>
      </div>

      <p>Query Management Delays</p>
      <div class="w3-grey">
        <div class="w3-container w3-center w3-padding w3-red" style="width:75%">75%</div>
      </div>
    </div>
    <hr>

    <div class="w3-container">
      <h5>Countries</h5>
      <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
        <tr>
          <td>United States</td>
          <td>65%</td>
        </tr>
        <tr>
          <td>UK</td>
          <td>15.7%</td>
        </tr>
        <tr>
          <td>Russia</td>
          <td>5.6%</td>
        </tr>
        <tr>
          <td>Spain</td>
          <td>2.1%</td>
        </tr>
        <tr>
          <td>India</td>
          <td>1.9%</td>
        </tr>
        <tr>
          <td>France</td>
          <td>1.5%</td>
        </tr>
      </table><br>
      <button class="w3-button w3-dark-grey">More Countries  <i class="fa fa-arrow-right"></i></button>
    </div>
    <hr>
    <div class="w3-container">
      <h5>Recent Users</h5>
      <ul class="w3-ul w3-card-4 w3-white">
        <li class="w3-padding-16">
          <img src="/w3images/avatar2.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
          <span class="w3-xlarge">Mike</span><br>
        </li>
        <li class="w3-padding-16">
          <img src="/w3images/avatar5.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
          <span class="w3-xlarge">Jill</span><br>
        </li>
        <li class="w3-padding-16">
          <img src="/w3images/avatar6.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
          <span class="w3-xlarge">Jane</span><br>
        </li>
      </ul>
    </div>
    <hr>

    <div class="w3-container">
      <h5>Recent Comments</h5>
      <div class="w3-row">
        <div class="w3-col m2 text-center">
          <img class="w3-circle" src="https://www.w3schools.com/w3images/avatar3.png" style="width:96px;height:96px">
        </div>
        <div class="w3-col m10 w3-container">
          <h4>John <span class="w3-opacity w3-medium">Sep 29, 2014, 9:12 PM</span></h4>
          <p>Keep up the GREAT work! I am cheering for you!! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p><br>
        </div>
      </div>

      <div class="w3-row">
        <div class="w3-col m2 text-center">
          <img class="w3-circle" src="/w3images/avatar1.png" style="width:96px;height:96px">
        </div>
        <div class="w3-col m10 w3-container">
          <h4>Bo <span class="w3-opacity w3-medium">Sep 28, 2014, 10:15 PM</span></h4>
          <p>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p><br>
        </div>
      </div>
    </div>
    <br>
    <div class="w3-container w3-dark-grey w3-padding-32">
      <div class="w3-row">
        <div class="w3-container w3-third">
          <h5 class="w3-bottombar w3-border-green">Demographic</h5>
          <p>Language</p>
          <p>Country</p>
          <p>City</p>
        </div>
        <div class="w3-container w3-third">
          <h5 class="w3-bottombar w3-border-red">System</h5>
          <p>Browser</p>
          <p>OS</p>
          <p>More</p>
        </div>
        <div class="w3-container w3-third">
          <h5 class="w3-bottombar w3-border-orange">Target</h5>
          <p>Users</p>
          <p>Active</p>
          <p>Geo</p>
          <p>Interests</p>
        </div>
      </div>
    </div>'''

def myStudies_layout(username):

    # list all the studies the user joined. Format for HTML table
    listStudies = "<form action = '/studyProperties'>"
    for study in glob.users[username][1]:
        listStudies += "<td>" + study + "</td>"
        listStudies += "<td>" + glob.studies[study][0] + "</td>"
        listStudies += "<td>" + glob.studies[study][1] + "</td>"
        listStudies += "<td><input type='submit' value='Open'/></form></td></tr></form>"

    # list of the other possible studies the user didn't join yet. Format for HTML table
    existingStudies = list(glob.studies.keys())
    listExistingStudies = ""
    for existingStudie in existingStudies:
        listExistingStudies += "<option value = '" + existingStudie + "' > " + existingStudie + "</option >"

    return '''
  <!-- !PAGE CONTENT! -->
  <div class="w3-main" style="margin-left:300px;margin-top:43px;">

    <!-- Header -->
    <header class="w3-container" style="padding-top:22px">
      <h5><b><i class="fa fa-dashboard"></i> My studies</b></h5>
    </header>
    
    <div class="w3-container">
      <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
      <tr>
        <th>Study name</th>
        <th>Therapeutical area</th>
        <th>Study type</th>
        <th>Properties</th>
      </tr><tr>
       ''' + listStudies + '''
      </table>
      <br><br>
      <form action="/joinStudy">
    
      <div class="w3-container">
      <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
        <tr>
          <td>Join an existing study</td>
          <td><select name="studyname" size="4" single>
            ''' + listExistingStudies + '''
        </select></td>
        <td><input type="submit"></td>
        </tr>
      </table><br>
    </form>
      
      '''

def designStudy_layout():
    return '''
  <!-- !PAGE CONTENT! -->
  <div class="w3-main" style="margin-left:300px;margin-top:43px;">

    <!-- Header -->
    <header class="w3-container" style="padding-top:22px">
      <h5><b><i class="fa fa-dashboard"></i> New study design (1/2)</b></h5>
    </header>

    <form action="/action_newstudy">
    
      <div class="w3-container">
      <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
        <tr>
          <td>Study name</td>
          <td><input name="studyname" type="text"></td>
        </tr>
        <tr>
          <td>Therapeutical area</td>
          <td><select name="therparea" size="4" single>
            <option value="cns">CNS</option>
            <option value="onco">Oncology</option>
            <option value="cs">Cardiovascular</option>
        </select></td>
        </tr>
        <tr>
          <td>Study type</td>
          <td><select name="studytemplate" size="4" single>
            <option value="p1">Phase 1</option>
            <option value="p2">Phase 2</option>
            <option value="p3">Phase 3</option>
        </select></td>
        </tr>
      </table><br>
      <input type="submit">
    </form>
    '''

def designStudy_phase2_layout(studyname, therparea, studytemplate):

    listVisits = ""
    for visit in glob.visits:
        listVisits += "<option value = 'visit'> " + visit +"</option>"

    return '''    
  <!-- !PAGE CONTENT! -->
  <div class="w3-main" style="margin-left:300px;margin-top:43px;">

    <!-- Header -->
    <header class="w3-container" style="padding-top:22px">
      <h5><b><i class="fa fa-dashboard"></i> New study design (2/2)</b></h5>
    </header>

    <div class="container">
    <p> Please review the following for the new study ''' + studyname + ''' (therapeutical area: ''' + therparea + ''', template:  ''' + studytemplate + ''')<p>
    
    <form action="/action_newstudy2">
    <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
    <tr>
        <th> </th>
        <th>Interventions</th>
        <th>From</th>
        <th>To</th>
        <th>Stages</th>
        <th></th>
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X" checked></td>
        <td><select name="visits">         
            <option value = 'ICF' selected>Informed Consent Form signed</option>
            <option value = 'ERC'>Eligility Review and Confirmation</option>
            <option value = 'MH'>Medical History</option>
            <option value = 'PE'>Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = "-28"></td>
        <td><input name="end"   type="text" value = "-1"></td>
        <td><select name="stages">         
            <option value = 'screening' selected>Screening</option>
            <option value = 'baseline'>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td><input type="button" onclick="properties" value="Properties"></td>
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X" checked></td>
        <td><select name="visits">         
            <option value = 'ICF' >Informed Consent Form signed</option>
            <option value = 'ERC' selected>Eligility Review and Confirmation</option>
            <option value = 'MH'>Medical History</option>
            <option value = 'PE'>Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = "-28"></td>
        <td><input name="end"   type="text" value = "-1"></td>
        <td><select name="stages">         
            <option value = 'screening' selected>Screening</option>
            <option value = 'baseline'>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td><input type="button" onclick="properties" value="Properties"></td>       
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X" checked></td>
        <td><select name="visits">         
            <option value = 'ICF'>Informed Consent Form signed</option>
            <option value = 'ERC'>Eligility Review and Confirmation</option>
            <option value = 'MH' selected>Medical History</option>
            <option value = 'PE'>Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = "-28"></td>
        <td><input name="end"   type="text" value = "-1"></td>
        <td><select name="stages">         
            <option value = 'screening' selected>Screening</option>
            <option value = 'baseline'>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Properties</button>
        </td>  
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X" checked></td>
        <td><select name="visits">         
            <option value = 'ICF'>Informed Consent Form signed</option>
            <option value = 'ERC'>Eligility Review and Confirmation</option>
            <option value = 'MH' >Medical History</option>
            <option value = 'PE' selected>Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = "-28"></td>
        <td><input name="end"   type="text" value = "-1"></td>
        <td><select name="stages">         
            <option value = 'screening' selected>Screening</option>
            <option value = 'baseline'>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td><input type="button" onclick="properties" value="Properties"></td>  
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X" checked></td>
        <td><select name="visits">         
            <option value = 'ICF'>Informed Consent Form signed</option>
            <option value = 'ERC'>Eligility Review and Confirmation</option>
            <option value = 'MH' >Medical History</option>
            <option value = 'PE' selected>Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = "1"></td>
        <td><input name="end"   type="text" value = "1"></td>        
        <td><select name="stages">         
            <option value = 'screening'>Screening</option>
            <option value = 'baseline' selected>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td><input type="button" onclick="properties" value="Properties"></td>
    </tr>
    <tr>
        <td><input type="checkbox" name="X" value="X"></td>
        <td><select name="visits">
            <option value = 'none' selected> </option>         
            <option value = 'ICF'>Informed Consent Form signed</option>
            <option value = 'ERC'>Eligility Review and Confirmation</option>
            <option value = 'MH' >Medical History</option>
            <option value = 'PE' >Physical Examination</option>
        </select></td> 
        <td><input name="start" type="text" value = ""></td>
        <td><input name="end"   type="text" value = ""></td>        
        <td><select name="stages">         
            <option value = 'none' selected> </option>
            <option value = 'screening'>Screening</option>
            <option value = 'baseline'>Baseline</option>
            <option value = 'p1'>Phase 1</option>
            <option value = 'p1'>Phase 2</option>
        </select></td> 
        <td><input type="button" onclick="properties" value="Properties"></td>
    </tr>
    
    </table><br><br>
    <input type="submit" value = "Build!">
    </form>

  <!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Medial History</h4>
        </div>
        <div class="modal-body">
            <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
                <tr>
                    <th>Field</th>
                    <th>Label</th>
                    <th>Type</th>
                    <th>Validation rules</th>
                    <th>Conformed DM field</th>
                </tr>
                <tr>
                    <td>Patient_No</td>
                    <td>Patient Number</td> 
                    <td>N</td>
                    <td>NumberOnlyUnique</td>
                    <td>Patient.Patient_PK</td> 
                </tr>
                <tr>
                    <td>Cond_Cd</td>
                    <td>Condition Code</td> 
                    <td>N</td>
                    <td>WHOCode</td>
                    <td>PatientMH.Cond_PK</td> 
                </tr>
                <tr>
                    <td>Cond_Dt</td>
                    <td>Condition Date</td> 
                    <td>N</td>
                    <td>ValidDate</td>
                    <td>N/A</td> 
                </tr> 
            </table>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-default" data-dismiss="modal">Save</button>
        </div>
      </div>
      
    </div>
  </div>
  '''

def dmQueries_layout():

   return '''
     <div class ="w3-main" style="margin-left:300px;margin-top:43px;">
     <header class ="w3-container" style="padding-top:22px" >
     <h5><b><i class ="fa fa-dashboard"></i> Queries Management</b></h5>
     </header>

     <div class ="w3-container">
     <form>
     <select name="studies">         
            <option value = 's1'>ACZ8885M</option>
            <option value = 's2'>BAF158U</option>
        </select></td> 
        <input type="submit" value = "OK">
    </div>
    </form>
    
    <br><br>
    <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
                <tr>
                    <th>Identified Query</th>
                    <th>Severity</th>
                    <th>Date Raised</th>
                    <th>Expected Fix</th>
                    <th></th>
                </tr>
                <tr>
                    <td>Patient DOB missing</td> 
                    <td>1</td>
                    <td>2018-02-01</td>
                    <td>2018-02-02</td> 
                    <td><input type="button" onclick="properties" value="Action"></td>
                </tr>
                <tr>
                    <td>BPM outside of parameters</td> 
                    <td>2</td>
                    <td>2018-03-01</td>
                    <td>2018-03-02</td> 
                    <td><input type="button" onclick="properties" value="Action"></td>
                </tr>                
            </table>

    '''

def cdmTEST_layout_showdata():
    dbfile = "db/db1.sq3"
    conn = sqlite3.connect(dbfile)
    cur = conn.cursor()

    # trial_dim
    cur.execute('select * from trial_dim')
    trial_dim = ""
    for row in cur:
        trial_dim += "<tr>"
        for field in str(row).split(","):
            trial_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        trial_dim += "</tr>"
    trial_dim += "</table>"

    # compound dim
    cur.execute('select * from compound_dim')
    compound_dim = ""
    for row in cur:
        compound_dim += "<tr>"
        for field in str(row).split(","):
            compound_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        compound_dim += "</tr>"
    compound_dim += "</table>"

    # Investigator_Dim
    cur.execute('select * from investigator_dim')
    investigator_dim = ""
    for row in cur:
        investigator_dim += "<tr>"
        for field in str(row).split(","):
            investigator_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        investigator_dim += "</tr>"
    investigator_dim += "</table>"

    # patient_dim
    cur.execute('select * from patient_dim')
    patient_dim = ""
    for row in cur:
        patient_dim += "<tr>"
        for field in str(row).split(","):
            patient_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        patient_dim += "</tr>"
    patient_dim += "</table>"

    # identity_dim
    cur.execute('select * from identity_dim')
    identity_dim = ""
    for row in cur:
        identity_dim += "<tr>"
        for field in str(row).split(","):
            identity_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        identity_dim += "</tr>"
    identity_dim += "</table>"

    # visit_dim
    cur.execute('select * from visit_dim')
    visit_dim = ""
    for row in cur:
        visit_dim += "<tr>"
        for field in str(row).split(","):
            visit_dim += "<td>" + field.strip('\'\"() ') + "</td>"
        visit_dim += "</tr>"
    visit_dim += "</table>"

    # visit_fact
    cur.execute('select * from visit_fact')
    visit_fact = ""
    for row in cur:
        visit_fact += "<tr>"
        for field in str(row).split(","):
            visit_fact += "<td>" + field.strip('\'\"() ') + "</td>"
        visit_fact += "</tr>"
    visit_fact += "</table>"

    return '''

        <div class ="w3-main" style="margin-left:300px;margin-top:43px;">
         <header class ="w3-container" style="padding-top:22px" >
         <h5><b><i class ="fa fa-dashboard"></i> CDM Test</b></h5>
         </header>

         <div class ="w3-container">
        <h2> TRIAl_DIM </h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Trial_key</th>,
                    <th>Compound_key</th>,
                    <th>TrialName</th>,
                    <th>RequiredPatients_Cnt</th>,
                    <th>RequiredVisits_Cnt</th>,
                    <th>RequiredWeeks_Cnt</th>,
                    <th>RequiredDosage</th>            
                    </tr>                
         ''' + trial_dim + '''  <br><br>    

        <h2> COMPOUND_DIM </h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Compound_key</th>,
                    <th>CompoundName</th>            
                    </tr>                
         ''' + compound_dim + '''  <br><br>        

        <h2> INVESTIGATOR_DIM </h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Investigator_key</th>,
                    <th>InvestigatorName</th>,
                    <th>InvestigatorAddress</th>,
                    <th>InvestigatorQualifications</th>        
                    </tr>                
         ''' + investigator_dim + '''  <br><br>           

        <h2> PATIENT_DIM </h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Patient_key</th>,
                    <th>Identity_key</th>,
                    <th>Birth_Dt</th>,
                    <th>Gender</th>,
                    <th>PatientHeight</th>        
                    </tr>                
         ''' + patient_dim + '''  <br><br>                

         <h2> IDENTITY_DIM</h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Identity_key</th>,
                    <th>IndividualName</th>,
                    <th>IndividualAddress</th>,
                    <th>GPName</th>,
                    <th>GPAddress</th>        
                    </tr>                
         ''' + identity_dim + '''  <br><br>        

         <h2> VISIT_DIM</h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Visit_key</th>,
                    <th>Visit_Dt</th>,
                    <th>SiteAddress</th>        
                    </tr>                
         ''' + visit_dim + '''  <br><br>       

         <h2> VISIT_FACT</h2>
         <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                    <tr>    
                    <th>Trial_key</th>,
                    <th>Investigator_key</th>,
                    <th>Compound_key</th>,
                    <th>Patient_key</th>,
                    <th>Visit_key</th>,
                    <th>BloodPressure</th>,
                    <th>Temperature</th>,
                    <th>PatientWeight</th>,
                    <th>Dosage</th>,
                    <th>DeliveryMethod</th>        
                    </tr>                
         ''' + visit_fact + '''  <br><br>         
    '''


def cdmTEST_layout():

    dbfile = "db/db1.sq3"
    conn = sqlite3.connect(dbfile)
    cur = conn.cursor()

    # visitview
    cur.execute('select * from visitview')
    visitview = ""
    for row in cur:
        visitview += "<tr>"
        for field in str(row).split(","):
            visitview += "<td>" + field.strip('\'\"() ') + "</td>"
        visitview += "</tr>"
    visitview += "</table>"

    cur.close()
    conn.close()

    return '''
    
    <div class ="w3-main" style="margin-left:300px;margin-top:43px;">
     <header class ="w3-container" style="padding-top:22px" >
     <h5><b><i class ="fa fa-dashboard"></i> CDM Test</b></h5>
     </header>

     <div class ="w3-container">
     <h2> VISIT_VIEW </h2>
     <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">     
                <tr>    
                <th>trialname</th>,
                <th>compoundName</th>,
                <th>birth_dt</th>,
                <th>gender</th>,
                <th>patientHeight</th>,
                <th>visit_key</th>,
                <th>visit_dt</th>,
                <th>BloodPressure</th>,
                <th>Temperature</th>,
                <th>PatientWeight</th>,
                <th>Dosage</th>,
                <th>DeliveryMethod</th>                
                </tr>                
     ''' + visitview + '''  <br><br>

    <br><br>     
    <form action="/cdmtest_step2">
        <input type="submit" value = "Add data - Step 2">
      <br>
    </form>
        <form action="/cdmtest_step3">
        <input type="submit" value = "Add data - Step 3">
      <br>
    </form>    
     
     '''

def footer_layout():
    return '''
    <!-- End page content -->
    </div>

    <script>
    // Get the Sidebar
    var mySidebar = document.getElementById("mySidebar");

    // Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");

    // Toggle between showing and hiding the sidebar, and add overlay effect
    function w3_open() {
        if (mySidebar.style.display === 'block') {
            mySidebar.style.display = 'none';
            overlayBg.style.display = "none";
        } else {
            mySidebar.style.display = 'block';
            overlayBg.style.display = "block";
        }
    }

    // Close the sidebar with the close button
    function w3_close() {
        mySidebar.style.display = "none";
        overlayBg.style.display = "none";
    }
    </script>

    </body>
    </html>'''


def configuration_layout():
    return '''
     <div class ="w3-main" style="margin-left:300px;margin-top:43px;">
     <header class ="w3-container" style="padding-top:22px" >
     <h5><b><i class ="fa fa-dashboard"></i> Configuration</b></h5>
     </header>

    <br><br>
    <table class="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
                <tr>
                    <th>Integration</th>
                    <th>Active</th>
                    <th>Method</th>
                </tr>
                <tr>
                    <td>Workflow</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Bizagi.ini</td>
                    </tr>
                <tr>
                <tr>
                    <td>Role-based Security</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//OneLogin.ini</td>
                    </tr>
                <tr>
                <tr>
                    <td>Single Sign-on</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//OneLogin.ini</td>
                    </tr>
                <tr>
                    <td>Audit Trail</td> 
                    <td><i class="fa fa-toggle-off w3-text-grey w3-large"></i></td>
                    <td></td>
                </tr>  
                <tr>
                    <td>Version Control</td> 
                    <td><i class="fa fa-toggle-off w3-text-grey w3-large"></i></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Check-in/Check-out</td> 
                    <td><i class="fa fa-toggle-off w3-text-grey w3-large"></i></td>
                    <td></td>
                </tr>                
                <tr>
                    <td>Query Identification</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Query Management</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Jira.ini</td>
                </tr>                
                <tr>
                    <td>Safety Reporting</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Sceptre.ini</td>
                </tr>          
                <tr>
                    <td>Automated Data Integration</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Data Provenance</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Data Visualization</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Spotfire.ini</td>
                </tr>                
                <tr>
                    <td>Metrics Dashboard</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Tableau.ini</td>
                </tr>                
                <tr>
                    <td>EDC Conversion</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Lab Data Conversion</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Other Data Conversion</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//SAS.ini</td>
                </tr>                
                <tr>
                    <td>Coding</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//MedidataCoder.ini</td>
                </tr>                
                <tr>
                    <td>Electronic Signatures</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//ToxKin.ini</td>
                </tr>                
                <tr>
                    <td>Data De-Identification</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>Cross Study-Analysis</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Databricks.ini</td>
                </tr>                
                <tr>
                    <td>User Interface</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Python.ini</td>
                </tr>                
                <tr>
                    <td>High Performance Computing</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//AmazonWebServices.ini</td>
                </tr>                
                <tr>
                    <td>Prioritisation & Load Balancing</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//AmazonWebServices.ini</td>
                </tr>                
                <tr>
                    <td>Metadata Repository</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Oracle.ini</td>
                </tr>                
                <tr>
                    <td>Related Operational Data Repository</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Oracle.ini</td>
                </tr>                
                <tr>
                    <td>Clinical Data Repository</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//Oracle.ini</td>
                </tr>                
                <tr>
                    <td>Script Repository</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//GitHub.ini</td>
                </tr>                
                <tr>
                    <td>Artefact Repository</td> 
                    <td><i class="fa fa-toggle-on w3-text-green w3-large"></i></td>
                    <td>//SAS.ini</td>
                </tr>                
            </table>

    '''
