from telethon import TelegramClient, events, sync,utils
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time,os,random,csv,sys
r= "\u001b[31;1m"
a= "\u001b[32m"
y = "\u001b[33;1m"
b="\u001b[34;1m"
m="\u001b[35;1m"
c="\u001b[36;1m"
clear = lambda:os.system('clear')
inf = (y+'TELEGRAM'+a+'  '+a+'MEMBER'+b+'  '+'PRO'+y+'  '+m+'VERSI'+c+' '+m+'2022'+c)
el=0
def Sleep(timE):
    try:
        time.sleep(timE)
    except KeyboardInterrupt:
        print(r+" KeyboardInterrupt , ........")
def info():
    print("")
    print("")
    print(inf)
    print("")
    print("")
clear()
info()
def ospath():
    o=int(input(b+" Berapa Banyak Akun Yang Akan Anda Gunakan ? : "))
    for po in range(o):
        if os.path.isfile('API_AKUN.txt'):
            with open('API_AKUN.txt', 'r') as f:
                data = f.readlines()
            v=int(len(data)/2)
            z=v
        else:
            z=0
        api_id= input(b+' Masukkan API ID {}: '.format(z+1))
        api_hash= input('Masukkan API Hash {}: '.format(z+1))
        with open('API_AKUN.txt', 'a') as f:
            f.write(api_id+'\n'+api_hash+'\n')
        client = TelegramClient("Daeng{}".format(z), api_id, api_hash)
        client.start()
        Sleep(1)
        clear()
        info()
        client.disconnect()
if os.path.isfile('API_AKUN.txt'):
    xc=input(b+" Anda Ingin Melanjutkan Sesi Terakhir "+a+" (y/n) ? ")
    if xc=='y':
        cy=input(" Anda Ingin Menambah Akun Lagi "+a+" (y/n) ? ")
        if cy=='y':
            ospath()
        else:
            pass
    else:
        cv=input(" Anda Ingin Menghapus Sesi Terakhir "+a+" (y/n) ? ")
        if cv=='y':
            with open('API_AKUN.txt', 'r') as f:
                data = f.readlines()
            v=int((len(data))/2)
            con=input(r+" Anda Ingin Menghapus Semua File Sesi Terakhir "+a+" (y/n) ? ")
            if con in ['', 'n']:
                print(m+" Keluar Sekarang "+'\n'+a+"Tidak Ada File Yang DiHapus ! ")
                sys.exit(1)
            elif con=='y':
                print(r+ " Semua File Terhapus")
                Sleep(1)
                for d in range(v-1):
                    os.remove("Daeng{}.session".format(d))
                os.remove('API_AKUN.txt')          
            ospath()
        else:
            sys.exit()
else:
    ospath()

clear()
info()
x=0
inh=2
t=0
with open('API_AKUN.txt', 'r') as f:
    data = f.readlines()
v=int(len(data)/2)
for s in range(v):
    api_id = data[t]
    api_hash = data[t+1]
    print(a+ ' \nMencoba Untuk Menghubungkan {} \n'.format(x+1)+y+ ' \n api {}= '.format(x+1) +m+ api_id +'\n' +y+ ' api hash {} = '.format(x+1) +m+ api_hash)
    Sleep(1)
    client = TelegramClient("Daeng{}".format(x), api_id, api_hash)
    client.start()
    name=utils.get_display_name(client.get_me())
    print(a+" \n\n  ❤SUKSES as {}❤\n\n".format(name))
    t+=2
    lines=[]
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
    for chat in chats:
        try:
            if chat.megagroup==True:
                groups.append(chat)
        except:
            continue
    print(b+' Pilih Group Yang Akan Di Scrape:')
    i=0
    for g in groups:
        print(m+str(i) +y+ ' - '+a + g.title)
        i+=1
    g_index = input(b+' Masukkan Pilihan (Atau Tekan Enter Untuk Skip): ')
    if g_index == '' :
        info()
        print(m+" Ok. SKIP...")
        Sleep(1)
    else:
        info()
        target_group=groups[int(g_index)]
        print(y+' Scrape Members...')
        all_participants = []
        all_participants = client.get_participants(target_group)
        print(y+' Tersimpan Di File...')
        with open("Members.csv","w",encoding='UTF-8') as f:
            writer=csv.writer(f,delimiter=",",lineterminator="\n")
            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id,user.phone])
        print(a+' Scrape Member SUKSES.')
        Sleep(1)
    info()
    print(b+'Pilih Group Target Untuk DiTambahkan Member :')
    i=0
    for group in groups:
        print(m+str(i) +y+ ' - ' +a+ group.title)
        i+=1
    g_index = input(b+' Masukkan Pilihan : ')
    if g_index=='':
        print(m+" \n Anda Menekan Enter,Keluar Sekarang...")
        sys.exit()  
    users = []  
    with open('Members.csv', encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        for row in rows:
            lines.append(row)
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['name'] = row[3]
            users.append(user)
    my_participants = client.get_participants(groups[int(g_index)])
    target_group=groups[int(g_index)]

    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
    my_participants_id = []
    for my_participant in my_participants:
        my_participants_id.append(my_participant.id)
    info()
    n,q=0,0
    for user in users:
        usR=str(user['id'])
        n += 1
        if n % 20 == 0:
            info()
            print (y+' Tunggu 20 Detik Untuk Menghindari Banned....')
            Sleep(20)  
        elif q>= 9:
            client.disconnect()
            if x<v:             
                x+=1
                inh+=1
                break
            else:
                print(b+" Tidak Ada Member Di Temukan, Keluar Sekarang..")
                Sleep(1)
                sys.exit()
        if user['id'] in my_participants_id:
            print(a+' Member Sudah Ada, SKIP...')
            n-=1
            with open('Members.csv', 'r',encoding='UTF-8') as f:
                dat = csv.reader(f,delimiter=",",lineterminator="\n")
                for tad in dat:
                    if usR in tad:
                        lines.remove(tad)
                        break
            Sleep(1)       
            continue
        else:
            try:
                print (a+' Menambahkan {}'.format(user['name']))
                if True :
                    if user['username'] == "":
                        continue
                user_to_add = client.get_input_entity(user['username'])
                client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                print(m+" Tunggu 2 - 4 Detik...")
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                with open("Members.csv","w",encoding='UTF-8') as f:
                    writer=csv.writer(f,delimiter=",",lineterminator="\n")
                    for line in lines:
                        writer.writerow(line)        
                             
                time.sleep(random.randrange(2,4))
                
                q=0
            except PeerFloodError:
                print(r+' Terdeteksi Flood Oleh Telegram, Tools Akan Berhenti Dan Silahkan Coba Lagi Seteleh Beberapa Saat.')
                Sleep(1)
                q+= 1
            except UserPrivacyRestrictedError:
                print(r+' Member Menggunakan Privacy. SKIP.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserBotError:
                print(r+' Jangan ADD Bot. SKIP...')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break    
            except InputUserDeactivatedError:
                print(r+' Member Tidak Aktif. SKIP...')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserChannelsTooMuchError:
                print(r+' Member Over Group. SKIP.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserNotMutualContactError:
                print(r+' Member Tidak Ada. SKIP.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except KeyboardInterrupt:
                i=0
                kst=["Stop","Lanjut","Ganti Dengan Akun Lain"]
                for ks in kst:
                    print('\n'+m+ str(i) +y+ ' - ' +a+ ks)
                    i+=1
                keyb=int(input(y+" Masukkan Pilihan : "))
                if keyb==1:
                    print(a+" Ok Lanjutkan...")
                    Sleep(1)
                elif keyb==0:
                    print(y+" Keluar Sekarang...")
                    sys.exit(1)
                else:
                    print(a+ " \n\nGanti... Ke Akun Berikutnya\n\n")
                    x+=1
                    break                
            except Exception as e:
                print(r+' Error:', e)
                print('Mencoba Melanjutkan...')
                q += 1
                Sleep(1)
                continue
    
    
    
