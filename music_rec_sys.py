import spotipy
import random
import webbrowser
import urllib.request
from spotipy.oauth2 import SpotifyClientCredentials
import pyttsx3
import playsound 
import speech_recognition as sr
from gtts import gTTS

#spotify
username='31eoapdgbljq5senrefpgrw7tecm'
client_id='d18d14b53e434114b1f7e2494a5cd9eb'
client_secret='526cbebf590143fa8957a18a910d4922'
redirect='http://google.com/'
oauth_object=spotipy.SpotifyOAuth(client_id,client_secret,redirect)
token_dict=oauth_object.get_cached_token()
token=token_dict['access_token']
spotify_object=spotipy.Spotify(auth=token)
user=spotify_object.current_user()
deviceID="613F4772-540B-44B2-A1BD-CCD058C114A3"
client_credentials_manager=SpotifyClientCredentials(client_id,client_secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def get_tracks(playlist_id):
    music_list=[]
    playlist=sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        music_track=item['track']
        music_list.append(music_track['name'])
    return music_list

#emotion or mood
#Keywords decalration
Happy = ("happy, good, love, nice, surprise, accidental, advantageous, appropriate, apt, heyo, auspicious, befitting, casual, convenient, correct, effective, efficacious, enviable, favorable, felicitous, fitting, fortunate, incidental, just, meet, nice, opportune, promising, proper, propitious, providential, right, satisfactory, seasonable, successful, suitable, timely, well-timed, jolly").split(", ")
Lucky = ("lucky, surprise, advantageous, bright, favorable, felicitous, fortunate, golden, halcyon, happy, hopeful, lucky, opportune, promising, propitious, prosperous, rosy, timely, well-timed").split(", ")
Sad = ("sad, no, die, not, bad, calamitous, dark, dejecting, deplorable, depressing, disastrous, discomposing, discouraging, disheartening, dismal, dispiriting, dreary, funereal, grave, grievous, hapless, heart-rending, joyless, lachrymose, lamentable, lugubrious, melancholic, miserable, moving, oppressive, pathetic, pitiable, pitiful, poignant, regrettable, saddening, serious, shabby, sorry, tear-jerking, tearful, tragic, unhappy, unsatisfactory, upsetting, wretched").split(", ")
Angry = ("angry, affronted, ugh, annoyed, antagonized, bitter, chafed, choleric, convulsed, cross, displeased, enraged, exacerbated, exasperated, ferocious, fierce, fiery, fuming, furious, galled, hateful, heated, hot, huffy, ill-tempered, impassioned, incensed, indignant, inflamed, infuriated, irascible, irate, ireful, irritable, irritated, maddened, nettled, offended, outraged, piqued, provoked, raging, resentful, riled, sore, splenetic, storming, sulky, sullen, tumultous/tumultuous, turbulent, uptight, vexed, wrathful").split(", ")
Tired = ("tired, annoy, ugh, bore, burn out, bush, collapse, crawl, debilitate, deject, depress, disgust, dishearten, dispirit, displease, distress, drain, droop, drop, enervate, ennui, exasperate, fag, fail, faint, fatigue, flag, fold, give out, go stale, grow weary, harass, irk, irritate, jade, nauseate, overburden, overstrain, overtax, overwork, pain, pall, peter out, poop out, prostrate, put to sleep, sap, sicken, sink, strain, tax, vex, weaken, wear, wear down, wear out, wilt, worry, yawn").split(", ")
Unhappy = ("tired, die, bleak, bleeding, ugh, blue, bummed out, cheerless, crestfallen, dejected, depressed, despondent, destroyed, disconsolate, dismal, dispirited, down and out, down in the mouth, down, downbeat, downcast, dragged, dreary, gloomy, grim, heavy-hearted, hurting, in a blue funk, in pain, in the dumps, let-down, long-faced, low, melancholy, mirthless, miserable, mournful, oppressive, put away, ripped, saddened, sorrowful, sorry, teary, troubled").split(", ") 
stressed = ("tired, die, stress, accent, ugh, belabor, dwell, feature, harp, headline, italicize, emphasis, emphatic, repeat, spot, spotlight, underline, underscore").split(", ")
pleasure = ("pleasure, surprise, love, amusement, bliss, comfort, contentment, delectation, diversion, ease, enjoyment, entertainment, felicity, flash*, fruition, game, gladness, gluttony, gratification, gusto, hobby, indulgence, joie de vivre, joy, joyride, kicks, luxury, primrose path, recreation, relish, revelry, satisfaction, seasoning, self-indulgence, solace, spice, thrill, titillation, turn-on, velvet, zest").split(", ")
#("").split(", ")


def ExactIn(array, item):
    for i in range(0,len(array)):
        if array[i] == item:
            return True
    return False

class Analysis():
    def GetMood(sentence):
        words = Analysis.GetWords(sentence)
        hs = 0 #Happy Score
        ss = 0 #Sad Score
        angs = 0 #Angry Score
        tirs = 0 #Tired Score
        #print(words)
        for word in words:
            word = word.lower()
            if Analysis.CFC(word,Happy) or Analysis.CFC(word,Lucky) or Analysis.CFC(word,pleasure):
                hs += 1
            if Analysis.CFC(word,Sad) or Analysis.CFC(word,stressed):
                ss += 1
            if Analysis.CFC(word,Angry):
                angs += 1
            if Analysis.CFC(word,Sad)or Analysis.CFC(word,Unhappy):
                tirs += 1
        total = hs + ss + angs + tirs
        hsp=ssp=angsp=tirsp=0
        if(hs!=0):
            hsp=int((hs/total) * 100)
        if(ss!=0):
            ssp=int((ss/total) * 100)
        if(angs!=0):
            angsp=int((angs/total) * 100)
        if(tirs!=0):
            tirsp=int((tirs/total) * 100)
        print("Happy Percentage: ",end="")
        print(hsp,end=" %\n")
        print("Sad Percentage: ",end="")
        print(ssp,end=" %\n")
        print("Angry Percentage: ",end="")
        print(angsp,end=" %\n")
        print("Tired Percentage: ",end="")
        print(tirsp,end=" %\n")
        if hsp>=50:
            playlist_id="37i9dQZF1EVJSvZp5AOML2"
        elif ssp>=50:
            playlist_id="37i9dQZF1EVKuMoAJjoTIw"
        elif angsp>=50:
            playlist_id="545DkYW699xQ4nBGGxFBoy"
        elif tirsp>50:
            playlist_id="37i9dQZF1EQncLwOalG3K7"
        else:
            playlist_id="3pXDL5EwoxDung1Gc2TArE"
        return playlist_id
    def CFC(word,array):
        #Wordform changing test
        if word in array:
            return True
        elif word.replace("ed","ing") in array:
            return True
        elif word.replace("ing","ed") in array:
            return True
        elif word.replace("ed","") in array:
            return True
        elif word.replace("ing","") in array:
            return True
        else:
            return False
    
    def GetWords(sentence):
        sentence = sentence.replace(", "," ")
        sentence = sentence.replace(". "," ")
        sentence = sentence.replace(","," ")
        sentence = sentence.replace(".","")
        sentence = sentence.replace('"',"")
        sentence = sentence.replace("'","")
        sentence = sentence.replace("?","")
        sentence = sentence.split(" ")
        return sentence

#converting text to audio
def speak(audio_inp):
    c=pyttsx3.init()
    newVoiceRate = 145
    c.setProperty('rate',newVoiceRate)
    voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    #voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM"
    c.setProperty('voice',voice_id )
    c.runAndWait()
    c.say(audio_inp)
    c.runAndWait()
    
#converting audio to text    
def audio():
    r=sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("speak now")
        aud=r.listen(source)
        var=""
    try:
        var=r.recognize_google(aud)
    except sr.UnknownValueError:
        #var="could not understand audio, would you try saying that again?"
        var="ok"
        text=audio()
    except sr.RequestError:
        var="Looks like, there is some problem with Speech Recognition"      
    return var
    
def main():
    speak(" hi how are you feeling right now?")
    text=audio()
    print(text)
    playlist_id=Analysis.GetMood(text)
    l=get_tracks(playlist_id)
    spo=random.choice(l)
    search_res=spotify_object.search(spo,1,0,"track")
    tracks_dict=search_res['tracks']
    tracks_items=tracks_dict['items']
    song=tracks_items[0]['external_urls']['spotify']
    webbrowser.open(song)
print("[info]Text Mood Analysis Engine Initialated.")
main()
