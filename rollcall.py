import bottle
import bottle_sqlite

app = bottle.Bottle()
plugin = bottle_sqlite.Plugin(dbfile='./rollcall.db')

app.install(plugin)


# CSS and bootstrap img

@app.route('/css/bootstrap.css')
def serve_bootcss():
    return bottle.static_file("bootstrap.css", root='./css')

@app.route('/img/<filename>')
def serve_image(filename):
    return bottle.static_file(filename, root='./img/')


def toggle(db, column, numid):
    # Toggle a boolean from 0 to 1 or 1 to 0
    #statusquery = db.execute('SELECT present from meeting where id=?', numid).fetchone()
    statusstr = 'SELECT %s from meeting where id=?' % column
    statusquery = db.execute(statusstr, [numid]).fetchone()
    status = statusquery
    print status
    if status[0] == 0:
        updatestr = 'UPDATE meeting SET %s=1 where id=?' % column
    elif status[0] == 1:
        updatestr = 'UPDATE meeting SET %s=0 where id=?' % column
    row = db.execute(updatestr, [numid])
    return


@app.route('/present/<idnum>')
def present(idnum, db):
    # Toggle a meeting's present/absent status
    toggle(db, "present", idnum)
    
    redirurl = "/show/" + str(idnum)
    bottle.redirect(redirurl)
    
    
@app.route('/')
def home(db):
    row = db.execute('SELECT * from meeting').fetchall()
    if row:
        return bottle.template('home', meetings=row)    
    return "Ack! We have encountered an error..."


@app.route('/show/done')
def all_done(db):
    meetings_present = db.execute('SELECT * from meeting where present=1').fetchall()
    meetings_absent = db.execute('SELECT * from meeting where present=0').fetchall()
    countquery = db.execute('SELECT count(*) from meeting').fetchone()
    count = countquery[0]
    present_count = len(meetings_present)
    absent_count = len(meetings_absent)
    # Calc percent present
    percentage = float(present_count) / float(count)
    percentage = percentage * 100
    percentage = int(percentage)
    
    if percentage > 50:
        quorum = "Quorum Present"
    else:
        quorum = "Quorum Absent"


    return bottle.template('done', quorum=quorum, percentage=percentage, present=present_count, absent=absent_count)    



@app.route('/show/<idnum>', method='POST')
def notes_submit(idnum, db):
    notes = bottle.request.forms.get('notes')
    update_notes = db.execute('UPDATE meeting set notes=? where id=?', [notes, idnum])
    redirurl = "/show/" + str(idnum)
    bottle.redirect(redirurl)    

@app.route('/show/<idnum>')
def show(idnum, db):


    row = db.execute('SELECT * from meeting where id=?', [idnum]).fetchone()

    # Set previous and next links
    if int(idnum) >= 1:
        prevlink = int(idnum) - 1
    
    # Need to find number of meetings to find the last link
    countquery = db.execute('SELECT count(*) from meeting').fetchone()
    count = countquery[0]
    print count
    
    if int(idnum) == count:
        nextlink = "done"
    else:
        nextlink = int(idnum) + 1
    
    
    if row:
        return bottle.template('showitem', meeting=row, prevlink=prevlink, nextlink=nextlink)
    return bottle.HTTPError(404, "Page not found")


bottle.debug(True)
bottle.run(app, host='localhost', port=9090, reloader=True)
