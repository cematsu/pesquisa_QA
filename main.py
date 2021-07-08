import json

import behave2cucumber
from behave.__main__ import main as behave_main

################## GERAR REPORT EM HTML #############################
code = behave_main(["features/", "-t~@ignore", '-k', '-o', 'reports/cucumber-behave.html', '-f', 'behave_html_formatter:HTMLFormatter'])


################## GERAR CUCUMBER REPORT PARA PIPELINE #############################

# code = behave_main(["features/", "-t~@ignore", '-k', '-o', 'reports/cucumber-behave.html', '-f', 'json'])
# code = behave_main(["features/", "-t~@ignore", '-k', '-o', 'reports/cucumber-behave.html', '-f', 'behave_html_formatter:HTMLFormatter'])
# cucumber_json = behave2cucumber.convert(json.load(open("reports/cucumber-behave.json")))
# with open('reports/cucumber-behave.json', 'w') as report:
#     report.write(json.dumps(cucumber_json))
#     report.flush()

exit(code)
