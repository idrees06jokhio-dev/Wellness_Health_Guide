# Importing Flask
from flask import Flask, request
# Importing Render Template For Rendering
from flask import render_template 
# Imprting Symptom and Suggester Program
import Symptom
import Suggester

# For Static Folder Accessing
app = Flask(__name__, static_url_path='/static')

# Linking HomePage
@app.route('/')
def home():
    return render_template('index.html')

# Linking Symptom Page
@app.route('/symptoms')
def symptoms():
    is_first_time = Symptom.is_first_time()
    return render_template('symptoms.html', is_first_time=is_first_time)

# Linking Suggester Page
@app.route('/suggester')
def suggester():
    return render_template('suggester.html')

# Linking About Page
@app.route('/about')
def about():
    return render_template('about.html')


# For Input In Symptom Page
@app.route("/s1", methods = ['POST'])
def s1():

	# Taking Input
	if request.method == 'POST':
		a = str(request.form['fn section'])
		b = str(request.form['sn section'])
		c = str(request.form['tn section'])       
		d = str(request.form['fon section'])
		
		# Check if this is first time (models need training)
		is_first_time = Symptom.is_first_time()
		
		# Calling Symptoms() from Symptom
		Sym = Symptom.Symptoms(a,b,c,d)

		# Displaying Input
		return render_template('symptoms.html', 
							 results = "Predicted Disease :: {}".format(Sym),
							 is_first_time = is_first_time)
	
	else:
		return render_template('symptoms.html')

# For Input In Suggester Page		
@app.route("/s2", methods = ['POST'])
def s2():

	# Taking Input
	if request.method == 'POST':
		a = str(request.form['n section'])
		# Calling Suggesters() from Suggester
		Sugg = Suggester.Suggesters(a)
		# html_table = Sugg.replace('\n', '\n')		

		# Displaying Input
		return render_template('suggester.html', results = Sugg)
	else:
		return render_template('suggester.html')		


# For running the page again and again without restarting

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 3000))
    # Force host to 0.0.0.0 for Render deployment
    host = '0.0.0.0' if os.environ.get('PORT') else 'localhost'
    app.run(host=host, port=port, debug=True)