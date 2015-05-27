def get_or_abort(model, object_id, code=404):
	result = model.query.get(object_id)
	return result or abort(code)

def theme_detail(theme_id):
	theme = get_or_abort(Theme, theme_id)
	return render_template('theme_detail.html', theme=theme)
	