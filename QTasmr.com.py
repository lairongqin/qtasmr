#-*- coding:UTF-8 -*-
from flask import Flask, render_template, abort, redirect,url_for,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Video(index)-PC.html")


@app.route('/index')
def PC_index():
    return render_template("Video(index)-PC-new.html")


@app.route('/about')
def about():
    return render_template("About-QT-PC.html")


@app.route('/joinus')
def joinus():
    return render_template("Joinus.html")


@app.route('/linkus')
def linkus():
    return render_template("Linkus.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/aboutasmr')
def aboutasmr():
    return render_template("About-ASMR-PC.html")


@app.route('/help')
def help():
    return render_template("Help-PC.html")


@app.route('/FQ/<fqname>')  # 分区的路由设计
def FQ(fqname):
    choose = False
    arg = ""
    FQ = {"notaking": u'无人声区', "ear": u'掏耳舔耳', "hands": u'手势催眠', "whisper": u'私语闲聊', "tapping": u'敲击眠音',
          "massage": u'睡前按摩', "player": u'角色扮演'}
    FQM = {"notaking": u'  无人声，更纯粹的ASMR', "ear": u' 耳部按摩 Relaxing！', "hands": u' 摇摇晃摇，睡吧睡吧。',
           "whisper": u'让我们聊一点容易睡着的话题吧！', "tapping": u' 这样清脆的声音最舒服了！', "massage": u'  睡前来一次正宗的马杀鸡！',
           "player": u' 睡前，让我当你一会会的男（女）盆友吧！'}
    for i in FQ.keys():
        if fqname == i:
            choose = True
    if choose:
        return render_template('Video-FQ-PC.html', fqname=FQ[fqname], arg=FQM[fqname])
    else:
        abort(404)


@app.route("/Search-PC")
def search():
    searchkey = request.args.get('searchkey')
    return render_template("Search-PC.html",searchkey=searchkey)

# 以上为PC端的路由说明

@app.route('/mobile')
def Mobile_index():
    return render_template("new-mobile.html")


@app.route('/mobile/list')
def Mobile_list():
    return render_template("new-mobile-list-video.html")


@app.route('/mobile/search')
def Mobile_search():
    return render_template("new-mobile-search-video.html")


@app.route('/mobile/aboutlist')
def Mobile_Aboutlist():
    return render_template("new-mobile-about.html")


@app.route('/mobile/aboutqt')
def Mobile_aboutqt():
    return render_template("mobile-About-QT.html")


@app.route('/mobile/aboutasmr')
def Mobile_aboutASMR():
    return render_template("mobile-ASMR-About.html")


@app.route('/mobile/help')
def Mobile_help():
    return render_template("mobile-Help.html")


@app.route('/mobile/linkus')
def Mobile_linkus():
    return render_template("mobile-Linkus.html")


@app.route('/mobile/joinus')
def Mobile_joinus():
    return render_template("moblie-Joinus.html")

@app.route('/mobile/feedback')
def Mobile_feedback():
    return render_template("mobile-feedback.html")


@app.route('/mobile/FQ/<fqname>')
def Mobile_fq(fqname):
    choose = False
    FQ = {"notaking": u'无人声区', "ear": u'掏耳舔耳', "hands": u'手势催眠', "whisper": u'私语闲聊', "tapping": u'敲击眠音',
          "massage": u'睡前按摩', "player": u'角色扮演'}
    for i in FQ.keys():
        if fqname == i:
            choose = True
    if choose:
        return render_template('new-mobile-FQ.html', fqname=FQ[fqname])
    else:
        abort(404)


@app.errorhandler(404)
def undo404(e):
    return render_template("404-PC.html"), 404


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
