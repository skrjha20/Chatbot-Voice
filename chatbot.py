from nltk.corpus import stopwords
from mssqldb import fetch_data
from plot_graph import plot_graph


stop_words = set(stopwords.words('english'))
actual_type = ['actual']
query_day = ['today', 'yesterday','last','year', '2018']
plan_type = ['plan', 'planned', 'plant', 'land']
product = ['crude', 'oil', 'lean', 'raw', 'sales', 'injection', 'lng', 'sulphur',
           'condensate', 'c3', 'agp', 'c4', 'c5', 'plus', 'propylene', 'lpg',
           'naptha','naphtha', 'gasoline', 'jet', 'a1', 'gasoil', 'gas','fuel', 'ethylene',
           'polyethylene', 'polypropylene','logos','rockers', 'rojas', 'rogers', 'rogers',
           'ragas','ragas','rockers', 'rock', 'brent','wta','wt','wti','murban']


def question_to_text(query):
    text_list = list(query.split(' '))
    clean_words = [w for w in text_list if not w in stop_words]
    reply = get_answer(clean_words)
    return reply


def get_answer(clean_words):
    product = get_product(clean_words)
    if product == "Unable to identify product name, please specify product name":
        return ("Unable to identify product name, please specify product name")

    req_day = get_date(clean_words)
    if req_day == "Unable to identify the required day for query":
        return ("Unable to identify the required day for query")

    if  product in ['brent crude','wti crude','brent crude wti crude', 'murban'] and (req_day == "last year" or req_day == "2018"):
        return plot_graph(product, req_day)

    actual_planned = get_actual_planned(clean_words)
    if actual_planned == "Unable to identify actual or planned, please specify again":
        return ("Unable to identify actual or planned, please specify again")

    outcome = fetch_data(product, actual_planned, req_day)
    return return_reply(outcome, product, actual_planned, req_day)

def get_product(clean_words):
    prod = []
    for i in range(len(clean_words)):
        if clean_words[i] in product:
            prod.append(clean_words[i])
    prod = " ".join(str(x) for x in prod)
    if len(prod) == 0:
        prod = "Unable to identify product name, please specify product name"
    return prod

def get_actual_planned(clean_words):
    actual_planned = ''
    for i in range(len(clean_words)):
        if clean_words[i] in actual_type:
            actual_planned = "actual"
        if clean_words[i] in plan_type:
            actual_planned = "planned"
    if actual_planned == '':
        actual_planned = "Unable to identify actual or planned, please specify again"
    return actual_planned


def get_date(clean_words):
    req_day = []
    for i in range(len(clean_words)):
        if clean_words[i] in query_day:
            req_day.append(clean_words[i])
    req_day= " ".join(str(x) for x in req_day)
    if req_day == '':
        req_day = "Unable to identify the required day for query"
    return req_day


def return_reply(outcome, product, actual_planned, req_day):
    if outcome == None:
        return( "We don't have data for the query, Please ask question again")

    elif product == "crude oil":
        product = "Crude oil"
        unit  = "Million Barrels"
    elif product == "lean":
        product = "Lean Gas"
        unit  = "Million standard cubic"

    elif product == "condensate":
        product = "Condensate"
        unit  = "Million Barrels"

    elif product in ('logos','rockers', 'Rockers','Rock','ragas','Ragas','rogers','Rogers', 'rojas'):
        product = "Raw Gas"
        unit = "Million standard cubic"

    elif product == "injection":
        product = "Injection Gas"
        unit = "Million standard cubic"

    elif product == "sales":
        product = "Sales Gas"
        unit = "Million standard cubic"

    elif product == "sulphur":
        product = "Sulphur"
        unit = "Tons"
    elif product in ('A1','jet A1','jet'):
        product = "Jet A1"
        unit = "Tons"
    else:
        unit = "Tons"

    return("The " + actual_planned +" production of " + product +" was "+ str(outcome) + " " + unit + " " + req_day)
