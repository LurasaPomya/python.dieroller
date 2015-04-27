from flask import Flask
import diefunctions

application = Flask(__name__)

@application.route('/')
def hello():
    return "<center>Hello</center>"

@application.route('/decroll/d6/<int:count>')
def roll6(count):
    if count > 100:
        return "Too many! Lower your count"
    else:
        results = diefunctions.roll(6,count)
        return "Rolled {}d6 for a total of {} \n".format(count,results[1]) 

@application.route('/decroll/<toroll>')
def rollvariable(toroll):
    toroll = toroll.split('d')
    count = int(toroll[0])
    sides = int(toroll[1])
    if count > 100:
        return "Too many! Lower your count"
    elif sides > 100:
        return "How many sides do you think I'm made of! Lower it!"
    else:
        results = diefunctions.roll(sides,count)
        return "You rolled {}d{} for a total of {} \n".format(count,sides,results[1])

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    application.debug = False
