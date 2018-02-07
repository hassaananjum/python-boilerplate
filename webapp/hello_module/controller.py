from flask import Blueprint, request, render_template, session, redirect, Response
import ModuleClass

module = Blueprint('Module', 
	__name__, 
	url_prefix='/hello',
	static_folder='static',
	template_folder='templates'
)

@module.route('/', methods=['GET', 'POST'])
def index():
	message = ModuleClass.main();
	return render_template(
		'index.html', 
		title="Hello", 
		message=message
	)