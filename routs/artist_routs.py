
def artistrouts(app):

    @app.route('/artist_dashbord', methods=['GET' , 'POST'])
    def artist_dashbord():
        return "artist dashbord template"
