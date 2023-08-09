import PyPDF2
import re
import string
from io import BytesIO

def parse_pdf(file_stream):
    # Open pdf file

    # Read file
    pdfReader = PyPDF2.PdfReader(file_stream)

    num_pages = len(pdfReader.pages)

    # Initialize a count for the number of pages
    count = 0

    # Initialize a text empty etring variable
    text = ""

    # Extract text from every page on the file
    for count in range(num_pages):
        pageObj = pdfReader.pages[count]
        extracted_text= pageObj.extract_text()

        # If the extracted text is empty, skip
        if extracted_text.strip:
            text += extracted_text

    # Convert all strings to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+','',text)

    # Remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))

    if not text.strip():
        return None


    # Create dictionary with industrial and system engineering key terms by area
    terms = {'SDE':['software','developer','c','c++','java','python',
                                'shell', 'database','scripting','php','node','javascript','systems','algorithm',
                                'data','performance','quality',
                                'sql','mongodb','mysql','networks','iit','iiit','nit',
                                'programming','production','git','bitbucket'],
            'Research Analyst':['research','analytical','conceptual','problem solving','high quality','reliable solutions',
                                'acquisition', 'cross platform','analysis','interpretation','documentation','report','ieee',
                                'publish','conference','paper'],
            'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                    'machinery','maintenance','manufacture','line balancing','oee','operations',
                                    'operations research','optimization','overall equipment effectiveness',
                                    'pfmea','process','process mapping','production','resources','safety',
                                    'stoppage','value stream mapping','utilization'],
            'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                            'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                            'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                            'third party logistics','transport','transportation','traffic','supply chain',
                            'vendor','warehouse','wip','work in progress'],
            'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                                'finance','kanban','leader','leadership','management','milestones','planning',
                                'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
            'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                            'coding','data','database','data mining','data science','deep learning','hadoop',
                            'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                            'predictive','programming','python','r','sql','tableau','text mining',
                            'visualuzation'],
            'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                        'health care','health','hospital','human factors','medical','near misses',
                        'patient','reporting system'],
            'Content Writing':['Bloggers','Social','Media','Posts','Copy','writing','SEO','experience','knowledge', 'sales','product','media','professional','publication','newsletters','Writing','tonality',
                        'Word','PowerPoint','Excel'],
              	
            'Marketing':['business consultant','business plan',' purchase',' branding',' advertising',' remodeling',' and marketing',' increasing monthly sales','social media','followers','marketing campaigns','email','print',' digital',' outdoor','social media', 
                  'Crafted concept content for journal ads',' direct mail campaigns','blogs','Achieved','Executed','Promoted','Analyzed','Generated','Researched','Captured','Implemented','Spearheaded','Designed','Increased','Tracked','Developed','Initiated','Utilized'],
              
            'Teaching':['Classroom management','Elementary or secondary education','Special education','Student-centered instruction','Parent involvement','interactive learning','Curriculum development',
			'Learning/instructional styles','Cooperative learning','Differentiated instruction','Distance learning','Behavior analysis/management','Lesson planning','Hands-on learning','Discipline management/strategies',
			'Educational assessment','Individual learning plan/individualized educational plans (IEP)','Teaching methodologies','Instructional technology','Developmental levels','Student advocate','Classroom instruction'],
		    
            'Security Analyst':['Testing','Web','Application','Security','Vulnerability','Assessment','Cybersecurity','Ethical','Hacking','Network Security','Information Security','Application Security','Burp','Suite','Linux','Security','Metasploit','Malware',
            'Analysis','Programming','Incident','Response']}


    # Initializie score counters for each area
    sde=0
    research=0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    healthcare = 0
    content=0
    marketing=0
    teaching=0
    security=0

    # Create an empty list where the scores will be stored
    scores = []

    # Obtain the scores for each area
    for area in terms.keys():
        if area == 'SDE':
            for word in terms[area]:
                if word in text:
                    sde +=1
            scores.append(sde)
                
        elif area == 'Research Analyst':
            for word in terms[area]:
                if word in text:
                    research +=1
            scores.append(research)
                    
        elif area == 'Operations management':
            for word in terms[area]:
                if word in text:
                    operations +=1
            scores.append(operations)
            
        elif area == 'Supply chain':
            for word in terms[area]:
                if word in text:
                    supplychain +=1
            scores.append(supplychain)
            
        elif area == 'Project management':
            for word in terms[area]:
                if word in text:
                    project +=1
            scores.append(project)
            
        elif area == 'Data analytics':
            for word in terms[area]:
                if word in text:
                    data +=1
            scores.append(data)
    
        elif area == 'Healthcare':
            for word in terms[area]:
                if word in text:
                    healthcare +=1
            scores.append(healthcare)

        elif area == 'Content Writing':
            for word in terms[area]:
                if word in text:
                    content +=1
            scores.append(content)

        elif area == 'Marketing':
            for word in terms[area]:
                if word in text:
                    marketing +=1
            scores.append(marketing)

        elif area == 'Teaching':
            for word in terms[area]:
                if word in text:
                    teaching +=1
            scores.append(teaching)

        else:
            for word in terms[area]:
                if word in text:
                    security +=1
            scores.append(security)
    return scores