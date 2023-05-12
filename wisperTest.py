import pyaudio
import speech_recognition as sr
import os

# マイクを使用する準備をする
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)

# 音声認識モデルをロードする
recognizer = sr.Recognizer()
recognizer.add_source(stream)

# 音声を聞き、テキストに変換する
i = 1
while True:
    # 音声を聞く
    frames = stream.read(4096)
    # テキストに変換する
    transcript = recognizer.recognize_google(frames)
    # Ctrl+Cが押されたらループを終了する
    if transcript == "":
        break

    # 音声をファイルに保存する
    with open("output_" + str(i) + ".txt", "w") as f:
        f.write(transcript)

    i += 1

    # 既に保存されているファイルを確認する
    for f in os.listdir("./"):
        if f.startswith("output_"):
            i = int(f[7:-4]) + 1

# マイクと音声認識モデルを閉じる
stream.close()
pa.terminate()
