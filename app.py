from flask import Flask, request, url_for, redirect, render_template

from pytube import YouTube  
import pafy 
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return render_template("index.html")

@app.route('/result',methods=['GET', 'POST'])
def result():
    if(request.method == "POST"):
        try:
            data = [str(x) for x in request.form.values()]
            print(data)
            yt_link = data[0]
            directory = data[1]
            if(data[2] == "audio") :
                video = pafy.new(yt_link)
                bestaudio = video.getbestaudio(preftype='m4a')
                bestaudio.download(filepath=directory)
                return render_template("index.html",issue = "Audio Download Success")
            else:
                getVideo = YouTube( yt_link)
                videoStream = getVideo.streams.first()
                videoStream.download(directory)
                return render_template("index.html",issue = "Video Download Success")
        except:    
            return render_template("index.html",issue = "There seems to be an error")


       
 
        
   
       
      
    
  

if __name__ == '__main__':
    app.run(debug=True)
