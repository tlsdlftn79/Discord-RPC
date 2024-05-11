import tkinter as tk
from tkinter import ttk
from pypresence import Presence
import time
import threading
import json  # JSON 데이터를 다루기 위해 추가

def update_rpc(client_id, state, details, button1_label, button1_url, button2_label, button2_url, large_image_key, small_image_key):
    rpc = Presence(client_id)
    rpc.connect()
    rpc.update(state=state,
               details=details,
               buttons=[{"label": button1_label, "url": button1_url},
                        {"label": button2_label, "url": button2_url}],
               large_image=large_image_key,  # 대형 이미지 키 추가
               small_image=small_image_key)  # 작은 이미지 키 추가
    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        rpc.close()

def start_rpc():
    client_id = client_id_entry.get()
    state = state_entry.get()
    details = details_entry.get()
    button1_label = button1_label_entry.get()
    button1_url = button1_url_entry.get()
    button2_label = button2_label_entry.get()
    button2_url = button2_url_entry.get()
    large_image_key = large_image_key_entry.get()  # 대형 이미지 키 입력 받기
    small_image_key = small_image_key_entry.get()  # 작은 이미지 키 입력 받기
    
    threading.Thread(target=update_rpc, args=(client_id, state, details, button1_label, button1_url, button2_label, button2_url, large_image_key, small_image_key), daemon=True).start()

def save_settings():
    settings = {
        "client_id": client_id_entry.get(),
        "state": state_entry.get(),
        "details": details_entry.get(),
        "button1_label": button1_label_entry.get(),
        "button1_url": button1_url_entry.get(),
        "button2_label": button2_label_entry.get(),
        "button2_url": button2_url_entry.get(),
        "large_image_key": large_image_key_entry.get(),  # 대형 이미지 키 저장
        "small_image_key": small_image_key_entry.get()  # 작은 이미지 키 저장
    }
    with open('rpc_settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    try:
        with open('rpc_settings.json', 'r') as f:
            settings = json.load(f)
            client_id_entry.delete(0, tk.END)
            client_id_entry.insert(0, settings['client_id'])
            state_entry.delete(0, tk.END)
            state_entry.insert(0, settings['state'])
            details_entry.delete(0, tk.END)
            details_entry.insert(0, settings['details'])
            button1_label_entry.delete(0, tk.END)
            button1_label_entry.insert(0, settings['button1_label'])
            button1_url_entry.delete(0, tk.END)
            button1_url_entry.insert(0, settings['button1_url'])
            button2_label_entry.delete(0, tk.END)
            button2_label_entry.insert(0, settings['button2_label'])
            button2_url_entry.delete(0, tk.END)
            button2_url_entry.insert(0, settings['button2_url'])
            large_image_key_entry.delete(0, tk.END)  # 대형 이미지 키 불러오기
            large_image_key_entry.insert(0, settings['large_image_key'])
            small_image_key_entry.delete(0, tk.END)  # 작은 이미지 키 불러오기
            small_image_key_entry.insert(0, settings['small_image_key'])
    except FileNotFoundError:
        print("설정 파일을 찾을 수 없습니다.")

app = tk.Tk()
app.title('Discord RPC 설정')

app.geometry('300x270')

tk.Label(app, text='클라이언트 ID 입력:').grid(row=0, column=0, sticky='w')
client_id_entry = tk.Entry(app)
client_id_entry.grid(row=0, column=1)

tk.Label(app, text='제목:').grid(row=1, column=0, sticky='w')
state_entry = tk.Entry(app)
state_entry.grid(row=1, column=1)

tk.Label(app, text='상세한 정보:').grid(row=2, column=0, sticky='w')
details_entry = tk.Entry(app)
details_entry.grid(row=2, column=1)

tk.Label(app, text='유튜브 채널:').grid(row=3, column=0, sticky='w')
button1_label_entry = tk.Entry(app)
button1_label_entry.grid(row=3, column=1)

tk.Label(app, text='유튜브 채널 주소:').grid(row=4, column=0, sticky='w')
button1_url_entry = tk.Entry(app)
button1_url_entry.grid(row=4, column=1)

tk.Label(app, text='치지직:').grid(row=5, column=0, sticky='w')
button2_label_entry = tk.Entry(app)
button2_label_entry.grid(row=5, column=1)

tk.Label(app, text='치지직 채널 주소:').grid(row=6, column=0, sticky='w')
button2_url_entry = tk.Entry(app)
button2_url_entry.grid(row=6, column=1)

tk.Label(app, text='대형 이미지 키:').grid(row=7, column=0, sticky='w')
large_image_key_entry = tk.Entry(app)
large_image_key_entry.grid(row=7, column=1)

tk.Label(app, text='작은 이미지 키:').grid(row=8, column=0, sticky='w')
small_image_key_entry = tk.Entry(app)
small_image_key_entry.grid(row=8, column=1)

# 'RPC 시작' 버튼의 row를 9로 변경
ttk.Button(app, text='RPC 시작', command=start_rpc).grid(row=9, column=0, columnspan=2)
# '설정 저장' 버튼의 row를 10으로 변경
ttk.Button(app, text='설정 저장', command=save_settings).grid(row=10, column=0, columnspan=2)
# '설정 불러오기' 버튼의 row를 11로 변경
ttk.Button(app, text='설정 불러오기', command=load_settings).grid(row=11, column=0, columnspan=2)

app.mainloop()

